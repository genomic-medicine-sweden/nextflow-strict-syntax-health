"""CLI for strict-syntax-health."""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx
import plotly.graph_objects as go
import rich_click as click
from rich.console import Console
from rich.table import Table

# API URLs
PIPELINES_URL = "https://pipelines.tol.sanger.ac.uk/pipelines.json"
MODULES_REPO_URL = "https://github.com/sanger-tol/nf-core-modules.git"
NFCORE_MODULES_REPO_URL = "https://github.com/nf-core/modules.git"

# Directory paths
PIPELINES_DIR = Path("pipelines")
MODULES_DIR = Path("modules")
NFCORE_MODULES_DIR = Path("nf-core-modules")
LINT_RESULTS_DIR = Path("lint_results")

# Pipelines.json now lives inside pipelines/
PIPELINES_JSON_PATH = PIPELINES_DIR / "pipelines.json"

# README path
README_PATH = Path("README.md")

# Lint results subdirectories (named to avoid gitignore patterns matching "pipelines/" and "modules/")
PIPELINES_LINT_RESULTS_DIR = LINT_RESULTS_DIR / "pipeline-results"
MODULES_LINT_RESULTS_DIR = LINT_RESULTS_DIR / "module-results"
SUBWORKFLOWS_LINT_RESULTS_DIR = LINT_RESULTS_DIR / "subworkflow-results"
PRINTS_HELP_RESULTS_DIR = LINT_RESULTS_DIR / "prints-help-results"

# Base URL for linking to files in this repository (used in Slack reports)
REPO_BASE_URL = "https://github.com/nf-core/strict-syntax-health/blob/main"

# Saved meta.yml stats (reloaded in --generate-charts-only mode)
MODULES_META_STATS_PATH = LINT_RESULTS_DIR / "modules_meta_stats.json"

console = Console()


# ============================================================================
# Git commit hash utilities for caching
# ============================================================================


def get_remote_commit_hash(repo_url: str, branch: str = "HEAD") -> str | None:
    """Get the latest commit hash from a remote repository without cloning.

    Uses `git ls-remote` which only queries the remote server - no download needed.
    This is the key optimization for skipping unchanged repos.

    Args:
        repo_url: The URL of the git repository
        branch: The branch/ref to check (default: HEAD). Use "refs/heads/dev" for dev branch.

    Returns:
        The commit hash string, or None if the query fails.
    """
    try:
        result = subprocess.run(
            ["git", "ls-remote", repo_url, branch],
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
        if result.stdout:
            return result.stdout.split()[0]
        return None
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None


def get_local_commit_hash(repo_path: Path) -> str:
    """Get the current HEAD commit hash of a cloned repository.

    Args:
        repo_path: Path to the cloned git repository.

    Returns:
        The commit hash string.
    """
    result = subprocess.run(
        ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


# ============================================================================
# Result sorting and utilities
# ============================================================================


def _sort_results(results: list[dict]) -> list[dict]:
    """Sort results by parse_error first, then errors (descending), then warnings (descending)."""
    return sorted(results, key=lambda x: (not x.get("parse_error", False), -x["errors"], -x["warnings"]))


def update_pipelines_json() -> None:
    """Download the latest pipelines.json from nf-co.re."""
    console.print(f"Downloading {PIPELINES_URL}...")
    PIPELINES_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    response = httpx.get(PIPELINES_URL, timeout=60)
    response.raise_for_status()
    PIPELINES_JSON_PATH.write_bytes(response.content)
    console.print(f"Updated {PIPELINES_JSON_PATH}")


def load_pipelines() -> list[dict]:
    """Load pipelines from the local pipelines.json file."""
    if not PIPELINES_JSON_PATH.exists():
        console.print(f"[red]{PIPELINES_JSON_PATH} not found. Run with --update-pipelines first.[/red]")
        sys.exit(1)

    console.print(f"Loading pipelines from {PIPELINES_JSON_PATH}...")
    data = json.loads(PIPELINES_JSON_PATH.read_text())

    pipelines = []
    for pipeline in data.get("remote_workflows", []):
        if pipeline.get("archived", False):
            continue
        pipelines.append(
            {
                "name": pipeline["name"],
                "full_name": pipeline["full_name"],
                "html_url": f"https://github.com/{pipeline['full_name']}",
            }
        )

    console.print(f"Found {len(pipelines)} active pipelines")
    return pipelines


def check_modules_repo_unchanged(
    url: str,
    prefix: str = "",
    branch: str = "refs/heads/main",
    no_cache: bool = False,
    check_modules: bool = True,
    check_subworkflows: bool = True,
) -> tuple[bool, str | None]:
    """Check if the repo is unchanged from cache (without cloning).

    Args:
        no_cache: If True, always return False (treat as changed)
        check_modules: Whether to check the modules cache
        check_subworkflows: Whether to check the subworkflows cache

    Returns:
        Tuple of (is_unchanged, remote_commit_hash)
        - is_unchanged: True if repo hasn't changed and we can use cached results
        - remote_commit_hash: The remote commit hash (for updating cache later)
    """
    if no_cache:
        return False, None

    # Get remote commit hash WITHOUT cloning
    remote_commit = get_remote_commit_hash(url, branch)
    if remote_commit is None:
        return False, None

    # Check caches for the types being linted
    cache_matches = True

    if check_modules:
        modules_cache = load_results_dict_for_type(f"{prefix}modules")
        modules_repo_commit = modules_cache.get("_repo_commit")
        if modules_repo_commit != remote_commit:
            cache_matches = False

    if check_subworkflows:
        subworkflows_cache = load_results_dict_for_type(f"{prefix}subworkflows")
        subworkflows_repo_commit = subworkflows_cache.get("_repo_commit")
        if subworkflows_repo_commit != remote_commit:
            cache_matches = False

    return cache_matches, remote_commit


def clone_nfcore_modules_repo() -> str:
    """Clone or update the nf-core/modules repository.

    Returns:
        The current commit hash of the cloned/updated repository.
    """
    if NFCORE_MODULES_DIR.exists():
        console.print("Updating nf-core/modules repository...")
        subprocess.run(
            ["git", "-C", str(NFCORE_MODULES_DIR), "fetch", "--quiet", "origin", "master"],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(NFCORE_MODULES_DIR), "checkout", "--quiet", "master"],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(NFCORE_MODULES_DIR), "pull", "--quiet"],
            check=True,
            capture_output=True,
        )
    else:
        console.print("Cloning nf-core/modules repository...")
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", NFCORE_MODULES_REPO_URL, str(NFCORE_MODULES_DIR)],
            check=True,
            capture_output=True,
        )

    commit_hash = get_local_commit_hash(NFCORE_MODULES_DIR)
    console.print(f"nf-core/modules repository ready at {NFCORE_MODULES_DIR} ({commit_hash[:8]})")
    return commit_hash


def link_nfcore_modules():
    nfcore_link = MODULES_DIR / "modules" / "nf-core"
    nfcore_target = NFCORE_MODULES_DIR / "modules" / "nf-core"
    # Use a relative target for portability
    relative_target = os.path.relpath(nfcore_target, nfcore_link.parent)
    if nfcore_link.is_symlink():
        nfcore_link.unlink()
    elif nfcore_link.exists():
        console.print(f"[red]Error: {nfcore_link} exists and is not a symlink[/red]")
        sys.exit(1)
    nfcore_link.symlink_to(relative_target, target_is_directory=True)


def clone_modules_repo() -> str:
    """Clone or update the sanger-tol/nf-core-modules repository.

    Returns:
        The current commit hash of the cloned/updated repository.
    """
    if MODULES_DIR.exists():
        console.print("Updating sanger-tol/nf-core-modules repository...")
        subprocess.run(
            ["git", "-C", str(MODULES_DIR), "fetch", "--quiet", "origin", "main"],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(MODULES_DIR), "checkout", "--quiet", "main"],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(MODULES_DIR), "pull", "--quiet"],
            check=True,
            capture_output=True,
        )
    else:
        console.print("Cloning sanger-tol/nf-core-modules repository...")
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", MODULES_REPO_URL, str(MODULES_DIR)],
            check=True,
            capture_output=True,
        )

    commit_hash = get_local_commit_hash(MODULES_DIR)
    console.print(f"sanger-tol/nf-core-modules repository ready at {MODULES_DIR} ({commit_hash[:8]})")
    return commit_hash


def discover_modules() -> list[dict]:
    """Discover all modules in the sanger-tol/nf-core-modules repository."""
    modules_path = MODULES_DIR / "modules" / "sanger-tol"
    if not modules_path.exists():
        console.print(f"[red]Modules path not found: {modules_path}[/red]")
        return []

    modules = []
    # Walk through tool directories
    for tool_dir in sorted(modules_path.iterdir()):
        if not tool_dir.is_dir() or tool_dir.name.startswith("."):
            continue
        # Walk through subcommand directories
        for subcommand_dir in sorted(tool_dir.iterdir()):
            if not subcommand_dir.is_dir() or subcommand_dir.name.startswith("."):
                continue
            main_nf = subcommand_dir / "main.nf"
            if main_nf.exists():
                # Module name is tool_subcommand (e.g., bwa_mem)
                name = f"{tool_dir.name}_{subcommand_dir.name}"
                modules.append(
                    {
                        "name": name,
                        "path": subcommand_dir,
                        "html_url": (
                            f"https://github.com/sanger-tol/nf-core-modules/tree/main/modules/sanger-tol/"
                            f"{tool_dir.name}/{subcommand_dir.name}"
                        ),
                    }
                )

    console.print(f"Found {len(modules)} modules")
    return modules


def scan_modules_meta_yml_stats() -> dict:
    """Scan sanger-tol modules and subworkflows for topic/version usage.

    For **modules**: checks each ``meta.yml`` for the presence of both ``topics:`` and
    ``versions:`` fields, mirroring the check performed by the nf-core stats pipeline.

    For **subworkflows**: checks the ``main.nf`` for a ``versions`` output channel
    (an emit assignment matching ``versions = …``).
    Subworkflows do not support a ``topics`` field.

    Returns:
        Dict with keys:
        - ``total``, ``with_topic_versions``, ``without_topic_versions``: combined counts
          (modules only contribute to ``with_topic_versions`` because subworkflows have no topics).
        - ``subworkflow_with_versions``, ``subworkflow_without_versions``: subworkflow-specific counts.
        - ``details``: list of per-component dicts, each with ``type``, ``name``, ``html_url``,
          ``has_topics`` (modules only), and ``has_versions``.
    """
    import re as _re

    base_url_modules = "https://github.com/sanger-tol/nf-core-modules/blob/main/modules/sanger-tol"
    base_url_subworkflows = "https://github.com/sanger-tol/nf-core-modules/blob/main/subworkflows/sanger-tol"
    total = 0
    with_topic_versions = 0  # modules: topics + versions
    swf_with_versions = 0
    details: list[dict] = []

    # Scan modules — meta.yml must have both topics: and versions:
    modules_path = MODULES_DIR / "modules" / "sanger-tol"
    if modules_path.exists():
        for meta_yml in sorted(modules_path.rglob("meta.yml")):
            total += 1
            try:
                content = meta_yml.read_text(errors="replace")
            except OSError:
                details.append(
                    {
                        "name": meta_yml.parent.name,
                        "html_url": "",
                        "has_topics": False,
                        "has_versions": False,
                        "type": "module",
                    }
                )
                continue

            has_topics = "topics:" in content
            has_versions = "versions:" in content

            # Derive module name (tool_subcommand) and URL from the path
            parts = meta_yml.parts
            try:
                idx = list(parts).index("sanger-tol")
                tool = parts[idx + 1]
                subcommand = parts[idx + 2]
                name = f"{tool}_{subcommand}"
                html_url = f"{base_url_modules}/{tool}/{subcommand}/meta.yml"
            except (ValueError, IndexError):
                name = meta_yml.parent.name
                html_url = ""

            if has_topics and has_versions:
                with_topic_versions += 1

            details.append(
                {
                    "name": name,
                    "html_url": html_url,
                    "has_topics": has_topics,
                    "has_versions": has_versions,
                    "type": "module",
                }
            )

    # Scan subworkflows — main.nf must emit a `versions` output channel
    subworkflows_path = MODULES_DIR / "subworkflows" / "sanger-tol"
    if subworkflows_path.exists():
        for subworkflow_dir in sorted(subworkflows_path.iterdir()):
            if not subworkflow_dir.is_dir() or subworkflow_dir.name.startswith("."):
                continue
            main_nf = subworkflow_dir / "main.nf"
            total += 1
            # Subworkflows are one level deep: subworkflows/sanger-tol/<name>/
            name = subworkflow_dir.name
            html_url = f"{base_url_subworkflows}/{name}/main.nf"

            if not main_nf.exists():
                details.append({"name": name, "html_url": html_url, "has_versions": False, "type": "subworkflow"})
                continue

            try:
                content = main_nf.read_text(errors="replace")
            except OSError:
                details.append({"name": name, "html_url": html_url, "has_versions": False, "type": "subworkflow"})
                continue

            # A subworkflow passes if its emit block contains a `versions` channel:
            # matches lines like "    versions = ch_versions"
            has_versions = bool(_re.search(r"^\s+versions\s*=", content, _re.MULTILINE))

            if has_versions:
                swf_with_versions += 1

            details.append({"name": name, "html_url": html_url, "has_versions": has_versions, "type": "subworkflow"})

    if total == 0:
        return {
            "total": 0,
            "with_topic_versions": 0,
            "without_topic_versions": 0,
            "subworkflow_with_versions": 0,
            "subworkflow_without_versions": 0,
            "details": [],
        }

    module_total = sum(1 for d in details if d["type"] == "module")
    swf_total = sum(1 for d in details if d["type"] == "subworkflow")
    console.print(
        f"meta.yml scan: {with_topic_versions}/{module_total} modules have topics + versions; "
        f"{swf_with_versions}/{swf_total} subworkflows emit versions"
    )
    return {
        "total": total,
        "with_topic_versions": with_topic_versions,
        "without_topic_versions": module_total - with_topic_versions,
        "subworkflow_with_versions": swf_with_versions,
        "subworkflow_without_versions": swf_total - swf_with_versions,
        "details": details,
    }


def discover_subworkflows() -> list[dict]:
    """Discover all subworkflows in the sanger-tol/nf-core-modules repository."""
    subworkflows_path = MODULES_DIR / "subworkflows" / "sanger-tol"
    if not subworkflows_path.exists():
        console.print(f"[red]Subworkflows path not found: {subworkflows_path}[/red]")
        return []

    subworkflows = []
    for subworkflow_dir in sorted(subworkflows_path.iterdir()):
        if not subworkflow_dir.is_dir() or subworkflow_dir.name.startswith("."):
            continue
        main_nf = subworkflow_dir / "main.nf"
        if main_nf.exists():
            subworkflows.append(
                {
                    "name": subworkflow_dir.name,
                    "path": subworkflow_dir,
                    "html_url": (
                        f"https://github.com/sanger-tol/nf-core-modules/tree/main/subworkflows/sanger-tol/{subworkflow_dir.name}"
                    ),
                }
            )

    console.print(f"Found {len(subworkflows)} subworkflows")
    return subworkflows


def clone_pipeline(pipeline: dict) -> Path:
    """Clone a pipeline repository, preferring the 'dev' branch."""
    repo_path = PIPELINES_DIR / pipeline["name"]

    if repo_path.exists():
        console.print(f"  Pipeline already cloned: {pipeline['name']}")
        # Try to checkout dev branch, fall back to default if it doesn't exist
        try:
            subprocess.run(
                ["git", "-C", str(repo_path), "fetch", "--quiet", "origin", "dev"],
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "-C", str(repo_path), "checkout", "--quiet", "dev"],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError:
            # dev branch doesn't exist, stay on current branch
            pass
        # Pull latest changes
        subprocess.run(
            ["git", "-C", str(repo_path), "pull", "--quiet"],
            check=True,
            capture_output=True,
        )
    else:
        console.print(f"  Cloning {pipeline['full_name']}...")
        PIPELINES_DIR.mkdir(parents=True, exist_ok=True)
        # Try to clone dev branch first
        try:
            subprocess.run(
                ["git", "clone", "--quiet", "--depth", "1", "--branch", "dev", pipeline["html_url"], str(repo_path)],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError:
            # dev branch doesn't exist, clone default branch
            subprocess.run(
                ["git", "clone", "--quiet", "--depth", "1", pipeline["html_url"], str(repo_path)],
                check=True,
                capture_output=True,
            )

    return repo_path


def get_nextflow_version() -> str:
    """Get the current nextflow version."""
    result = subprocess.run(
        ["nextflow", "-version"],
        capture_output=True,
        text=True,
    )
    # Parse version from output like "nextflow version 24.10.0.5928"
    for line in result.stdout.split("\n"):
        if "version" in line.lower():
            parts = line.split()
            for i, part in enumerate(parts):
                if part.lower() == "version" and i + 1 < len(parts):
                    return parts[i + 1]
    return "unknown"


def lint_component(repo_path: Path, target_path: Path | None = None) -> dict:
    """Run nextflow lint on a component (JSON output for parsing).

    Args:
        repo_path: The repository root path (used as cwd)
        target_path: Optional specific path to lint (relative to repo_path or absolute)
    """
    if target_path:
        # Make path relative to repo_path if it's absolute or inside repo_path
        try:
            relative_path = target_path.relative_to(repo_path)
        except ValueError:
            relative_path = target_path
        cmd = ["nextflow", "lint", str(relative_path), "-o", "json"]
    else:
        cmd = ["nextflow", "lint", ".", "-o", "json"]

    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    # nextflow lint returns non-zero exit code if there are errors
    # but we still want to parse the output
    try:
        lint_result = json.loads(result.stdout)
        lint_result["parse_error"] = False
        return lint_result
    except json.JSONDecodeError:
        name = target_path.name if target_path else repo_path.name
        console.print(f"[red]Failed to parse lint output for {name}[/red]")
        console.print(f"stdout: {result.stdout}")
        console.print(f"stderr: {result.stderr}")
        return {"summary": {"errors": 0}, "errors": [], "warnings": [], "parse_error": True}


def lint_directory_bulk(repo_path: Path, target_path: Path) -> dict:
    """Run nextflow lint on a directory containing multiple components (JSON output).

    This runs lint once on the entire directory and returns all results,
    which is much faster than running lint on each component individually.

    Args:
        repo_path: The repository root path (used as cwd)
        target_path: The directory to lint (e.g., modules/sanger-tol or subworkflows/sanger-tol)
    """
    try:
        relative_path = target_path.relative_to(repo_path)
    except ValueError:
        relative_path = target_path

    cmd = ["nextflow", "lint", str(relative_path), "-o", "json"]

    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        console.print(f"[red]Failed to parse bulk lint output for {target_path}[/red]")
        console.print(f"stdout: {result.stdout[:500]}...")
        console.print(f"stderr: {result.stderr}")
        return {"errors": [], "warnings": []}


def _extract_component_name_from_path(filepath: str, component_type: str) -> str | None:
    """Extract component name from a file path.

    Args:
        filepath: Path like 'modules/sanger-tol/bwa/mem/main.nf' or 'subworkflows/sanger-tol/foo/main.nf'
        component_type: Either 'modules' or 'subworkflows'

    Returns:
        Component name like 'bwa_mem' for modules or 'foo' for subworkflows, or None if not matched
    """
    parts = Path(filepath).parts

    # Find the sanger-tol part and extract the component name
    try:
        sanger_tol_idx = parts.index("sanger-tol")
    except ValueError:
        return None

    if component_type == "modules":
        # modules/sanger-tol/tool/subcommand/main.nf -> tool_subcommand
        if len(parts) > sanger_tol_idx + 2:
            return f"{parts[sanger_tol_idx + 1]}_{parts[sanger_tol_idx + 2]}"
    else:
        # subworkflows/sanger-tol/name/main.nf -> name
        if len(parts) > sanger_tol_idx + 1:
            return parts[sanger_tol_idx + 1]

    return None


def _group_lint_results_by_component(
    lint_result: dict,
    component_type: str,
) -> dict[str, dict]:
    """Group lint errors and warnings by component name.

    Args:
        lint_result: The JSON output from nextflow lint
        component_type: Either 'modules' or 'subworkflows'

    Returns:
        Dict mapping component name to {"errors": [...], "warnings": [...]}
    """
    grouped: dict[str, dict] = {}

    for error in lint_result.get("errors", []):
        filename = error.get("filename", "")
        name = _extract_component_name_from_path(filename, component_type)
        if name:
            if name not in grouped:
                grouped[name] = {"errors": [], "warnings": []}
            grouped[name]["errors"].append(error)

    for warning in lint_result.get("warnings", []):
        filename = warning.get("filename", "")
        name = _extract_component_name_from_path(filename, component_type)
        if name:
            if name not in grouped:
                grouped[name] = {"errors": [], "warnings": []}
            grouped[name]["warnings"].append(warning)

    return grouped


def _get_code_snippet(repo_path: Path, filename: str, line_num: int, column: int) -> str | None:
    """Read a code snippet from a file for display in markdown.

    Args:
        repo_path: Base repository path
        filename: Relative path to the file
        line_num: Line number (1-indexed)
        column: Column number (1-indexed)

    Returns:
        Formatted code snippet with caret marker, or None if file not found
    """
    try:
        file_path = repo_path / filename
        if not file_path.exists():
            return None

        source_lines = file_path.read_text().splitlines()
        if line_num < 1 or line_num > len(source_lines):
            return None

        source_line = source_lines[line_num - 1]
        # Create caret marker line pointing to the column
        # Account for the column being 1-indexed
        caret_line = " " * (column - 1) + "^" * max(1, min(10, len(source_line) - column + 1))

        return f"    ```nextflow\n    {source_line}\n    {caret_line}\n    ```"
    except Exception:
        return None


def _generate_markdown_from_issues(
    errors: list[dict],
    warnings: list[dict],
    nextflow_version: str,
    repo_path: Path | None = None,
) -> str:
    """Generate markdown output matching nextflow lint markdown format.

    Args:
        errors: List of error dicts with filename, startLine, startColumn, message
        warnings: List of warning dicts with same structure
        nextflow_version: Nextflow version string
        repo_path: Optional repository path for reading source code snippets

    Returns:
        Markdown string matching nextflow lint output format
    """
    now = datetime.now(timezone.utc).isoformat()
    error_count = len(errors)
    warning_count = len(warnings)

    lines = [
        "# Nextflow lint results",
        "",
        f"- Generated: {now}",
        f"- Nextflow version: {nextflow_version}",
    ]

    if error_count == 0 and warning_count == 0:
        lines.append("- Summary: No issues found")
        return "\n".join(lines)

    summary_parts = []
    if error_count > 0:
        summary_parts.append(f"{error_count} error{'s' if error_count != 1 else ''}")
    if warning_count > 0:
        summary_parts.append(f"{warning_count} warning{'s' if warning_count != 1 else ''}")
    lines.append(f"- Summary: {', '.join(summary_parts)}")

    if errors:
        lines.extend(["", "## :x: Errors", ""])
        for error in errors:
            filename = error.get("filename", "unknown")
            line_num = error.get("startLine", 0)
            col = error.get("startColumn", 0)
            message = error.get("message", "")
            lines.append(f"- Error: `{filename}:{line_num}:{col}`: {message}")
            lines.append("")
            if repo_path:
                snippet = _get_code_snippet(repo_path, filename, line_num, col)
                if snippet:
                    lines.append(snippet)
                    lines.append("")

    if warnings:
        lines.extend(["", "## :warning: Warnings", ""])
        for warning in warnings:
            filename = warning.get("filename", "unknown")
            line_num = warning.get("startLine", 0)
            col = warning.get("startColumn", 0)
            message = warning.get("message", "")
            lines.append(f"- Warning: `{filename}:{line_num}:{col}`: {message}")
            lines.append("")
            if repo_path:
                snippet = _get_code_snippet(repo_path, filename, line_num, col)
                if snippet:
                    lines.append(snippet)
                    lines.append("")

    return "\n".join(lines)


def lint_pipeline(repo_path: Path) -> dict:
    """Run nextflow lint on a pipeline (JSON output for parsing)."""
    return lint_component(repo_path)


def test_prints_help(repo_path: Path, name: str) -> bool:
    """Test if a pipeline can print help using the v2 syntax parser.

    Runs: NXF_SYNTAX_PARSER=v2 nextflow run . --help

    Args:
        repo_path: Path to the cloned pipeline repository.
        name: Pipeline name (used for saving output file).

    Returns:
        True if the command succeeds (exit code 0), False otherwise.
    """
    PRINTS_HELP_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    output_file = PRINTS_HELP_RESULTS_DIR / f"{name}_help.txt"

    try:
        env = {**os.environ, "NXF_SYNTAX_PARSER": "v2"}
        # Use stderr=STDOUT to interleave stdout and stderr as they would appear in a terminal
        result = subprocess.run(
            ["nextflow", "run", ".", "--help"],
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=120,
            env=env,
        )

        # Save combined output to file
        output_content = f"$ NXF_SYNTAX_PARSER=v2 nextflow run . --help\n\n{result.stdout}"
        output_file.write_text(output_content)

        return result.returncode == 0
    except subprocess.TimeoutExpired:
        console.print("[dim]  --help test timed out[/dim]")
        output_file.write_text("$ NXF_SYNTAX_PARSER=v2 nextflow run . --help\n\nError: Timeout after 120s\n")
        return False
    except Exception as e:
        console.print(f"[dim]  --help test failed: {e}[/dim]")
        output_file.write_text(f"$ NXF_SYNTAX_PARSER=v2 nextflow run . --help\n\nError: {e}\n")
        return False


def lint_component_markdown(repo_path: Path, name: str, output_dir: Path, target_path: Path | None = None) -> None:
    """Run nextflow lint on a component and save markdown output to file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{name}_lint.md"

    # Build command - if target_path specified, lint that specific path
    if target_path:
        # Make path relative to repo_path if it's absolute or inside repo_path
        try:
            relative_path = target_path.relative_to(repo_path)
        except ValueError:
            relative_path = target_path
        cmd = ["nextflow", "lint", str(relative_path), "-o", "markdown"]
    else:
        cmd = ["nextflow", "lint", ".", "-o", "markdown"]

    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    # Combine stdout and stderr for full output
    output = result.stdout
    if result.stderr:
        output += "\n" + result.stderr

    output_file.write_text(output)
    console.print(f"  Saved lint output to {output_file}")


def run_pipeline_lint(pipelines: list[dict], no_cache: bool = False) -> list[dict]:
    """Clone and lint all pipelines, using commit cache to skip unchanged repos.

    Args:
        pipelines: List of pipeline dicts with name, full_name, html_url
        no_cache: If True, ignore cache and re-lint everything
    """
    commits_cache = load_results_dict_for_type("pipelines")
    results = []
    skipped_count = 0
    linted_count = 0

    for pipeline in pipelines:
        name = pipeline["name"]
        cached = commits_cache.get(name)

        # BEFORE cloning: check if we can skip by comparing remote commit hash
        if not no_cache and cached:
            # Try dev branch first, then HEAD (default branch)
            remote_commit = get_remote_commit_hash(pipeline["html_url"], "refs/heads/dev")
            if remote_commit is None:
                remote_commit = get_remote_commit_hash(pipeline["html_url"], "HEAD")

            # Check if we need to run prints_help test for pipelines with zero errors
            # that were cached before this feature was added
            needs_prints_help = (
                cached.get("errors", 0) == 0
                and not cached.get("parse_error", False)
                and cached.get("prints_help") is None
            )

            if remote_commit and remote_commit == cached.get("commit") and not needs_prints_help:
                console.print(f"[dim]Skipping {name} (unchanged at {remote_commit[:8]})[/dim]")
                results.append(
                    {
                        "name": name,
                        "full_name": pipeline["full_name"],
                        "html_url": pipeline["html_url"],
                        "commit": remote_commit,
                        "errors": cached["errors"],
                        "warnings": cached["warnings"],
                        "parse_error": cached.get("parse_error", False),
                        "prints_help": cached.get("prints_help"),
                        "lint_details": {},  # Don't store full details in cache
                    }
                )
                skipped_count += 1
                continue

        # Cache miss or commit changed - need to clone and lint
        console.print(f"Processing pipeline {name}...")

        try:
            repo_path = clone_pipeline(pipeline)
            commit_hash = get_local_commit_hash(repo_path)
            lint_result = lint_pipeline(repo_path)
            lint_component_markdown(repo_path, name, PIPELINES_LINT_RESULTS_DIR)

            error_count = lint_result.get("summary", {}).get("errors", 0)
            warning_count = len(lint_result.get("warnings", []))
            parse_error = lint_result.get("parse_error", False)

            # Run prints_help test only if there are no errors
            prints_help = None
            if not parse_error and error_count == 0:
                console.print("  Testing --help with v2 parser...")
                prints_help = test_prints_help(repo_path, name)
                if prints_help:
                    console.print("  [green]--help test passed[/green]")
                else:
                    console.print("  [yellow]--help test failed[/yellow]")

            results.append(
                {
                    "name": name,
                    "full_name": pipeline["full_name"],
                    "html_url": pipeline["html_url"],
                    "commit": commit_hash,
                    "errors": error_count,
                    "warnings": warning_count,
                    "parse_error": parse_error,
                    "prints_help": prints_help,
                    "lint_details": lint_result,
                }
            )
            linted_count += 1

        except subprocess.CalledProcessError as e:
            console.print(f"[red]Failed to process {name}: {e}[/red]")
            results.append(
                {
                    "name": name,
                    "full_name": pipeline["full_name"],
                    "html_url": pipeline["html_url"],
                    "errors": 0,
                    "warnings": 0,
                    "parse_error": True,
                    "prints_help": None,
                    "lint_details": {},
                }
            )
            linted_count += 1

    if skipped_count > 0:
        console.print(f"[green]Skipped {skipped_count} unchanged pipelines, linted {linted_count}[/green]")

    return results


def run_modules_lint(modules: list[dict], nextflow_version: str = "unknown") -> list[dict]:
    """Lint all modules using bulk lint for efficiency.

    Args:
        modules: List of module dicts with name, path, html_url
        nextflow_version: Nextflow version string for markdown output
    """
    # Check if we're filtering to specific modules (small list)
    # If so, use individual linting for accuracy; otherwise use bulk
    if len(modules) <= 5:
        results = _run_modules_lint_individual(modules, nextflow_version)
    else:
        results = _run_modules_lint_bulk(modules, nextflow_version)

    return results


def load_cached_modules_results(modules: list[dict]) -> list[dict]:
    """Load cached lint results for modules when repo is unchanged.

    Args:
        modules: List of module dicts with name, path, html_url

    Returns:
        List of result dicts with cached error/warning counts
    """
    results_cache = load_results_dict_for_type("modules")
    results = []

    for module in modules:
        name = module["name"]
        cached = results_cache.get(name, {})
        results.append(
            {
                "name": name,
                "html_url": module["html_url"],
                "errors": cached.get("errors", 0),
                "warnings": cached.get("warnings", 0),
                "parse_error": cached.get("parse_error", False),
                "lint_details": {},
            }
        )

    return results


def _run_modules_lint_individual(modules: list[dict], nextflow_version: str) -> list[dict]:
    """Lint modules individually (used when filtering to specific modules)."""
    results = []

    for module in modules:
        console.print(f"Processing module {module['name']}...")

        try:
            lint_result = lint_component(MODULES_DIR, module["path"])
            lint_component_markdown(MODULES_DIR, module["name"], MODULES_LINT_RESULTS_DIR, module["path"])

            results.append(
                {
                    "name": module["name"],
                    "html_url": module["html_url"],
                    "errors": lint_result.get("summary", {}).get("errors", 0),
                    "warnings": len(lint_result.get("warnings", [])),
                    "parse_error": lint_result.get("parse_error", False),
                    "lint_details": lint_result,
                }
            )
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Failed to process module {module['name']}: {e}[/red]")
            results.append(
                {
                    "name": module["name"],
                    "html_url": module["html_url"],
                    "errors": 0,
                    "warnings": 0,
                    "parse_error": True,
                    "lint_details": {},
                }
            )

    return results


def _run_modules_lint_bulk(modules: list[dict], nextflow_version: str) -> list[dict]:
    """Lint all modules at once using bulk lint (much faster)."""
    console.print(f"Running bulk lint on {len(modules)} modules...")

    # Run lint once on the entire modules/sanger-tol directory
    modules_path = MODULES_DIR / "modules" / "sanger-tol"
    bulk_result = lint_directory_bulk(MODULES_DIR, modules_path)

    # Group results by component name
    grouped = _group_lint_results_by_component(bulk_result, "modules")

    # Generate results and markdown files for each module
    results = []
    MODULES_LINT_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    for module in modules:
        name = module["name"]
        component_issues = grouped.get(name, {"errors": [], "warnings": []})
        errors = component_issues["errors"]
        warnings = component_issues["warnings"]

        # Generate markdown file
        markdown_content = _generate_markdown_from_issues(errors, warnings, nextflow_version, MODULES_DIR)
        output_file = MODULES_LINT_RESULTS_DIR / f"{name}_lint.md"
        output_file.write_text(markdown_content)

        results.append(
            {
                "name": name,
                "html_url": module["html_url"],
                "errors": len(errors),
                "warnings": len(warnings),
                "parse_error": False,
                "lint_details": {"errors": errors, "warnings": warnings},
            }
        )

    console.print(f"Generated {len(results)} module lint reports")
    return results


def run_subworkflows_lint(subworkflows: list[dict], nextflow_version: str = "unknown") -> list[dict]:
    """Lint all subworkflows using bulk lint for efficiency.

    Args:
        subworkflows: List of subworkflow dicts with name, path, html_url
        nextflow_version: Nextflow version string for markdown output
    """
    # Check if we're filtering to specific subworkflows (small list)
    # If so, use individual linting for accuracy; otherwise use bulk
    if len(subworkflows) <= 5:
        results = _run_subworkflows_lint_individual(subworkflows, nextflow_version)
    else:
        results = _run_subworkflows_lint_bulk(subworkflows, nextflow_version)

    return results


def load_cached_subworkflows_results(subworkflows: list[dict]) -> list[dict]:
    """Load cached lint results for subworkflows when repo is unchanged.

    Args:
        subworkflows: List of subworkflow dicts with name, path, html_url

    Returns:
        List of result dicts with cached error/warning counts
    """
    results_cache = load_results_dict_for_type("subworkflows")
    results = []

    for subworkflow in subworkflows:
        name = subworkflow["name"]
        cached = results_cache.get(name, {})
        results.append(
            {
                "name": name,
                "html_url": subworkflow["html_url"],
                "errors": cached.get("errors", 0),
                "warnings": cached.get("warnings", 0),
                "parse_error": cached.get("parse_error", False),
                "lint_details": {},
            }
        )

    return results


def _run_subworkflows_lint_individual(subworkflows: list[dict], nextflow_version: str) -> list[dict]:
    """Lint subworkflows individually (used when filtering to specific subworkflows)."""
    results = []

    for subworkflow in subworkflows:
        console.print(f"Processing subworkflow {subworkflow['name']}...")

        try:
            lint_result = lint_component(MODULES_DIR, subworkflow["path"])
            lint_component_markdown(
                MODULES_DIR, subworkflow["name"], SUBWORKFLOWS_LINT_RESULTS_DIR, subworkflow["path"]
            )

            results.append(
                {
                    "name": subworkflow["name"],
                    "html_url": subworkflow["html_url"],
                    "errors": lint_result.get("summary", {}).get("errors", 0),
                    "warnings": len(lint_result.get("warnings", [])),
                    "parse_error": lint_result.get("parse_error", False),
                    "lint_details": lint_result,
                }
            )
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Failed to process subworkflow {subworkflow['name']}: {e}[/red]")
            results.append(
                {
                    "name": subworkflow["name"],
                    "html_url": subworkflow["html_url"],
                    "errors": 0,
                    "warnings": 0,
                    "parse_error": True,
                    "lint_details": {},
                }
            )

    return results


def _run_subworkflows_lint_bulk(subworkflows: list[dict], nextflow_version: str) -> list[dict]:
    """Lint all subworkflows at once using bulk lint (much faster)."""
    console.print(f"Running bulk lint on {len(subworkflows)} subworkflows...")

    # Run lint once on the entire subworkflows/sanger-tol directory
    subworkflows_path = MODULES_DIR / "subworkflows" / "sanger-tol"
    bulk_result = lint_directory_bulk(MODULES_DIR, subworkflows_path)

    # Group results by component name
    grouped = _group_lint_results_by_component(bulk_result, "subworkflows")

    # Generate results and markdown files for each subworkflow
    results = []
    SUBWORKFLOWS_LINT_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    for subworkflow in subworkflows:
        name = subworkflow["name"]
        component_issues = grouped.get(name, {"errors": [], "warnings": []})
        errors = component_issues["errors"]
        warnings = component_issues["warnings"]

        # Generate markdown file
        markdown_content = _generate_markdown_from_issues(errors, warnings, nextflow_version, MODULES_DIR)
        output_file = SUBWORKFLOWS_LINT_RESULTS_DIR / f"{name}_lint.md"
        output_file.write_text(markdown_content)

        results.append(
            {
                "name": name,
                "html_url": subworkflow["html_url"],
                "errors": len(errors),
                "warnings": len(warnings),
                "parse_error": False,
                "lint_details": {"errors": errors, "warnings": warnings},
            }
        )

    console.print(f"Generated {len(results)} subworkflow lint reports")
    return results


def display_results(results: list[dict], type_name: str, show_prints_help: bool = False) -> None:
    """Display results in a rich table."""
    table = Table(f"sanger-tol {type_name.capitalize()} Strict Syntax Health")
    table.add_column(type_name.capitalize(), style="cyan")
    table.add_column("Parse Error", justify="right")
    table.add_column("Errors", justify="right")
    table.add_column("Warnings", justify="right")
    if show_prints_help:
        table.add_column("Prints Help", justify="right")

    sorted_results = _sort_results(results)

    total_errors = 0
    total_warnings = 0
    total_parse_errors = 0

    for result in sorted_results:
        errors = result["errors"]
        warnings = result["warnings"]
        parse_error = result.get("parse_error", False)

        if parse_error:
            total_parse_errors += 1
            parse_error_str = "[red]Yes[/red]"
            error_str = "-"
            warning_str = "-"
        else:
            total_errors += errors
            total_warnings += warnings
            parse_error_str = "[green]No[/green]"
            error_str = f"[red]{errors}[/red]" if errors > 0 else "[green]0[/green]"
            warning_str = f"[yellow]{warnings}[/yellow]" if warnings > 0 else "[green]0[/green]"

        if show_prints_help:
            prints_help = result.get("prints_help")
            if prints_help is None:
                prints_help_str = "-"
            elif prints_help:
                prints_help_str = "[green]Yes[/green]"
            else:
                prints_help_str = "[red]No[/red]"
            table.add_row(result["name"], parse_error_str, error_str, warning_str, prints_help_str)
        else:
            table.add_row(result["name"], parse_error_str, error_str, warning_str)

    console.print(table)
    console.print(
        f"\n[bold]Total: {total_parse_errors} parse errors, {total_errors} errors, {total_warnings} warnings[/bold]"
    )


def display_meta_stats(meta_stats: dict) -> None:
    """Display topic/version usage as two separate rich tables (modules and subworkflows)."""
    details = meta_stats.get("details", [])

    # --- Modules table (topics: + versions: in meta.yml) ---
    mod_details = [d for d in details if d.get("type", "module") == "module"]
    if mod_details:
        mod_total = len(mod_details)
        mod_pass = meta_stats.get("with_topic_versions", 0)
        mod_fail = meta_stats.get("without_topic_versions", 0)
        mod_pct = mod_pass / mod_total * 100 if mod_total else 0

        mod_table = Table("sanger-tol Modules — topic + version usage (meta.yml)")
        mod_table.add_column("Module", style="cyan")
        mod_table.add_column("topics:", justify="center")
        mod_table.add_column("versions:", justify="center")
        for d in sorted(mod_details, key=lambda x: (x["has_topics"] and x["has_versions"], x["name"])):
            t = "[green]Yes[/green]" if d["has_topics"] else "[red]No[/red]"
            v = "[green]Yes[/green]" if d["has_versions"] else "[red]No[/red]"
            mod_table.add_row(d["name"], t, v)
        console.print(mod_table)
        console.print(f"[bold]modules: {mod_pass}/{mod_total} ({mod_pct:.1f}%) passing, {mod_fail} missing[/bold]")

    # --- Subworkflows table (main.nf must NOT emit a versions channel) ---
    swf_details = [d for d in details if d.get("type") == "subworkflow"]
    if swf_details:
        swf_total = len(swf_details)
        # passing = no versions channel (has_versions=False)
        swf_pass = meta_stats.get("subworkflow_without_versions", 0)
        swf_fail = meta_stats.get("subworkflow_with_versions", 0)
        swf_pct = swf_pass / swf_total * 100 if swf_total else 0

        swf_table = Table("sanger-tol Subworkflows — versions channel (main.nf emit)")
        swf_table.add_column("versions channel")  # subworkflow name, coloured by status
        # Bad ones (has versions) first, then good ones; within each group alphabetical
        for d in sorted(swf_details, key=lambda x: (not x["has_versions"], x["name"])):
            if d["has_versions"]:
                swf_table.add_row(f"[red]{d['name']}[/red]")  # has versions = bad
            else:
                swf_table.add_row(f"[green]{d['name']}[/green]")  # no versions = good
        console.print(swf_table)
        console.print(
            f"[bold]subworkflows: {swf_pass}/{swf_total} ({swf_pct:.1f}%) passing"
            f" (no versions channel), {swf_fail} failing[/bold]"
        )


def _get_type_dir(type_name: str) -> Path:
    """Get the lint results directory for a specific type."""
    type_dirs = {
        "pipelines": PIPELINES_LINT_RESULTS_DIR,
        "modules": MODULES_LINT_RESULTS_DIR,
        "subworkflows": SUBWORKFLOWS_LINT_RESULTS_DIR,
    }
    return type_dirs[type_name]


def _get_history_path_for_type(type_name: str) -> Path:
    """Get the history file path for a specific type (stored in lint_results/ root)."""
    return LINT_RESULTS_DIR / f"{type_name}_history.json"


def _get_results_path_for_type(type_name: str) -> Path:
    """Get the results file path for a specific type (stored in lint_results/ root)."""
    return LINT_RESULTS_DIR / f"{type_name}_results.json"


def save_results_for_type(type_name: str, results: list[dict], repo_commit: str | None = None) -> None:
    """Save lint results for a specific type (includes commit cache data).

    Results are stored as a dict keyed by component name for efficient lookup.
    Each entry contains: commit, errors, warnings, parse_error, full_name/html_url.

    Args:
        type_name: One of "pipelines", "modules", "subworkflows"
        results: List of result dicts from linting
        repo_commit: For modules/subworkflows, the shared repo commit hash
    """
    path = _get_results_path_for_type(type_name)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Convert list to dict keyed by name, stripping lint_details
    results_dict = {}

    # For modules/subworkflows, store the shared repo commit
    if repo_commit:
        results_dict["_repo_commit"] = repo_commit

    for r in results:
        name = r["name"]
        entry = {k: v for k, v in r.items() if k not in ("lint_details", "name")}
        results_dict[name] = entry

    path.write_text(json.dumps(results_dict, indent=2) + "\n")
    console.print(f"Saved results to {path}")


def load_results_for_type(type_name: str) -> list[dict]:
    """Load lint results for a specific type as a list.

    Converts the dict format back to a list for compatibility with existing code.
    """
    results_dict = load_results_dict_for_type(type_name)
    results = []
    for name, data in results_dict.items():
        if name.startswith("_"):  # Skip metadata keys like _repo_commit
            continue
        entry = {"name": name, **data}
        results.append(entry)
    return results


def load_results_dict_for_type(type_name: str) -> dict:
    """Load lint results for a specific type as a dict (for cache lookups).

    Returns dict keyed by component name with commit, errors, warnings, parse_error, etc.
    """
    path = _get_results_path_for_type(type_name)
    if path.exists():
        try:
            data = json.loads(path.read_text())
            # Handle both old list format and new dict format
            if isinstance(data, list):
                # Convert old list format to dict
                return {r["name"]: {k: v for k, v in r.items() if k != "name"} for r in data}
            return data
        except json.JSONDecodeError:
            return {}
    return {}


def load_history_for_type(type_name: str) -> list[dict]:
    """Load historical results for a specific type."""
    path = _get_history_path_for_type(type_name)
    if path.exists():
        return json.loads(path.read_text())
    return []


def save_history_for_type(type_name: str, history: list[dict]) -> None:
    """Save historical results for a specific type."""
    path = _get_history_path_for_type(type_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, indent=2) + "\n")
    console.print(f"Updated {path}")


def load_history() -> dict:
    """Load historical results from all per-type history files."""
    return {
        "pipelines": load_history_for_type("pipelines"),
        "modules": load_history_for_type("modules"),
        "subworkflows": load_history_for_type("subworkflows"),
    }


def _create_history_entry(
    results: list[dict],
    include_prints_help: bool = False,
    meta_stats: dict | None = None,
) -> dict:
    """Create a history entry from results.

    Args:
        results: List of lint results
        include_prints_help: If True, include prints_help statistics (for pipelines only)
        meta_stats: Optional dict from scan_modules_meta_yml_stats (for modules only)
    """
    valid_results = [r for r in results if not r.get("parse_error", False)]
    parse_error_results = [r for r in results if r.get("parse_error", False)]

    entry = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total": len(results),
        "parse_errors": len(parse_error_results),
        "errors_zero": sum(1 for r in valid_results if r["errors"] == 0),
        "errors_low": sum(1 for r in valid_results if 0 < r["errors"] <= 5),
        "errors_high": sum(1 for r in valid_results if r["errors"] > 5),
        "warnings_zero": sum(1 for r in valid_results if r["warnings"] == 0),
        "warnings_low": sum(1 for r in valid_results if 0 < r["warnings"] <= 20),
        "warnings_high": sum(1 for r in valid_results if r["warnings"] > 20),
    }

    if include_prints_help:
        # Count prints_help results (only for pipelines with zero errors)
        # prints_help is True/False/None - None means test wasn't run (has errors)
        entry["prints_help_pass"] = sum(1 for r in valid_results if r.get("prints_help") is True)
        entry["prints_help_fail"] = sum(1 for r in valid_results if r.get("prints_help") is False)

    if meta_stats:
        entry["meta_with_topic_versions"] = meta_stats.get("with_topic_versions", 0)
        entry["meta_without_topic_versions"] = meta_stats.get("without_topic_versions", 0)

    return entry


def _update_history_for_type(history_list: list[dict], entry: dict) -> list[dict]:
    """Update history list for a specific type, replacing today's entry if it exists."""
    today = entry["date"]
    for i, h in enumerate(history_list):
        if h["date"] == today:
            history_list[i] = entry
            return history_list
    history_list.append(entry)
    return history_list


def update_history(
    pipeline_results: list[dict] | None = None,
    module_results: list[dict] | None = None,
    subworkflow_results: list[dict] | None = None,
    module_meta_stats: dict | None = None,
) -> dict:
    """Add current results to history and return updated history.

    Each type's history is stored in its own file to allow parallel updates.

    Args:
        pipeline_results: List of pipeline lint results.
        module_results: List of module lint results.
        subworkflow_results: List of subworkflow lint results.
        module_meta_stats: Optional dict from scan_modules_meta_yml_stats to include
            topics/versions coverage in the modules history entry.
    """
    history = {}

    if pipeline_results is not None:
        pipelines_history = load_history_for_type("pipelines")
        entry = _create_history_entry(pipeline_results, include_prints_help=True)
        pipelines_history = _update_history_for_type(pipelines_history, entry)
        save_history_for_type("pipelines", pipelines_history)
        history["pipelines"] = pipelines_history

    if module_results is not None:
        modules_history = load_history_for_type("modules")
        entry = _create_history_entry(module_results, meta_stats=module_meta_stats)
        modules_history = _update_history_for_type(modules_history, entry)
        save_history_for_type("modules", modules_history)
        history["modules"] = modules_history

    if subworkflow_results is not None:
        subworkflows_history = load_history_for_type("subworkflows")
        entry = _create_history_entry(subworkflow_results)
        subworkflows_history = _update_history_for_type(subworkflows_history, entry)
        save_history_for_type("subworkflows", subworkflows_history)
        history["subworkflows"] = subworkflows_history

    return history


def _create_stacked_chart(
    dates: list[str],
    series: list[tuple[list[int], str, str, str]],  # (values, name, line_color, fill_color)
    title: str,
    output_path: Path,
    y_label: str = "Number of Items",
) -> None:
    """Create a stacked area chart and save it to a file."""
    fig = go.Figure()
    for i, (values, name, line_color, fill_color) in enumerate(series):
        fig.add_trace(
            go.Scatter(
                x=dates,
                y=values,
                name=name,
                fill="tozeroy" if i == 0 else "tonexty",
                mode="lines",
                line={"width": 0.5, "color": line_color},
                fillcolor=fill_color,
                stackgroup="stack",
            )
        )
    fig.update_layout(
        title={"text": title, "x": 0.5, "xanchor": "center", "font": {"size": 20}},
        xaxis_title="Date",
        yaxis_title=y_label,
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "center", "x": 0.5},
        template="plotly_white",
        hovermode="x unified",
        width=1000,
        height=500,
    )
    fig.write_image(str(output_path), scale=2)
    console.print(f"Generated {output_path}")


def generate_charts_for_type(history: list[dict], output_dir: Path, type_name: str) -> None:
    """Generate error and warning charts for a specific type (pipelines, modules, subworkflows).

    Charts are saved to LINT_RESULTS_DIR with type-prefixed filenames (e.g., pipelines_errors.png).
    """
    if not history:
        console.print(f"[yellow]Not enough history to generate {type_name} charts[/yellow]")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    dates = [h["date"] for h in history]
    y_label = f"Number of {type_name.title()}"

    # Build error chart series - pipelines include prints_help breakdown for zero-error items
    if type_name == "pipelines":
        # For pipelines, break down "No errors" into prints_help pass/fail
        error_series = [
            (
                [h.get("prints_help_pass", 0) for h in history],
                "No errors, prints help",
                "#2ecc71",
                "rgba(46, 204, 113, 0.7)",
            ),
            (
                [h.get("prints_help_fail", 0) for h in history],
                "No errors, help fails",
                "#e67e22",
                "rgba(230, 126, 34, 0.7)",
            ),
            ([h["errors_low"] for h in history], "1-5 errors", "#f39c12", "rgba(243, 156, 18, 0.7)"),
            ([h["errors_high"] for h in history], ">5 errors", "#e74c3c", "rgba(231, 76, 60, 0.7)"),
            ([h.get("parse_errors", 0) for h in history], "Parse errors", "#8e44ad", "rgba(142, 68, 173, 0.7)"),
        ]
    else:
        error_series = [
            ([h["errors_zero"] for h in history], "No errors", "#2ecc71", "rgba(46, 204, 113, 0.7)"),
            ([h["errors_low"] for h in history], "1-5 errors", "#f39c12", "rgba(243, 156, 18, 0.7)"),
            ([h["errors_high"] for h in history], ">5 errors", "#e74c3c", "rgba(231, 76, 60, 0.7)"),
            ([h.get("parse_errors", 0) for h in history], "Parse errors", "#8e44ad", "rgba(142, 68, 173, 0.7)"),
        ]

    _create_stacked_chart(
        dates,
        error_series,
        f"{type_name.title()} Errors Over Time",
        LINT_RESULTS_DIR / f"{type_name}_errors.png",
        y_label,
    )

    _create_stacked_chart(
        dates,
        [
            ([h["warnings_zero"] for h in history], "No warnings", "#1abc9c", "rgba(26, 188, 156, 0.7)"),
            ([h["warnings_low"] for h in history], "1-20 warnings", "#3498db", "rgba(52, 152, 219, 0.7)"),
            ([h["warnings_high"] for h in history], ">20 warnings", "#9b59b6", "rgba(155, 89, 182, 0.7)"),
            ([h.get("parse_errors", 0) for h in history], "Parse errors", "#8e44ad", "rgba(142, 68, 173, 0.7)"),
        ],
        f"{type_name.title()} Warnings Over Time",
        LINT_RESULTS_DIR / f"{type_name}_warnings.png",
        y_label,
    )

    # For modules: generate an additional chart tracking topic version usage
    if type_name == "modules" and any("meta_with_topic_versions" in h for h in history):
        _create_stacked_chart(
            dates,
            [
                (
                    [h.get("meta_with_topic_versions", 0) for h in history],
                    "Has topic version",
                    "#2ecc71",
                    "rgba(46, 204, 113, 0.7)",
                ),
                (
                    [h.get("meta_without_topic_versions", 0) for h in history],
                    "Missing topic version",
                    "#e74c3c",
                    "rgba(231, 76, 60, 0.7)",
                ),
            ],
            "Module Topic Version Usage Over Time",
            LINT_RESULTS_DIR / "modules_topic_versions.png",
            y_label,
        )


def generate_all_charts(history: dict) -> None:
    """Generate charts for all types (pipelines, modules, subworkflows)."""
    if history.get("pipelines"):
        generate_charts_for_type(history["pipelines"], PIPELINES_LINT_RESULTS_DIR, "pipelines")
    if history.get("modules"):
        generate_charts_for_type(history["modules"], MODULES_LINT_RESULTS_DIR, "modules")
    if history.get("subworkflows"):
        generate_charts_for_type(history["subworkflows"], SUBWORKFLOWS_LINT_RESULTS_DIR, "subworkflows")


def _generate_results_section(
    results: list[dict],
    type_name: str,
    type_singular: str,
    lint_results_dir: Path,
    include_charts: bool,
    show_only_errors: bool = False,
    show_prints_help: bool = False,
    module_meta_stats: dict | None = None,
) -> list[str]:
    """Generate a results section for a specific type (pipelines, modules, subworkflows).

    Args:
        results: List of lint results
        type_name: Type name (pipelines, modules, subworkflows)
        type_singular: Singular form (pipeline, module, subworkflow)
        lint_results_dir: Path to lint results directory
        include_charts: Whether to include chart images
        show_only_errors: If True, only show items with errors in the table (for modules/subworkflows)
        show_prints_help: If True, show the "Prints Help" column (for pipelines only)
        module_meta_stats: Optional dict from scan_modules_meta_yml_stats (modules only)
    """
    if not results:
        return []

    sorted_results = _sort_results(results)
    valid_results = [r for r in results if not r.get("parse_error", False)]
    parse_error_count = sum(1 for r in results if r.get("parse_error", False))
    total_errors = sum(r["errors"] for r in valid_results)
    total_warnings = sum(r["warnings"] for r in valid_results)
    zero_error_count = sum(1 for r in valid_results if r["errors"] == 0)
    zero_error_percentage = (zero_error_count / len(results) * 100) if results else 0

    lines = [
        f"## {type_name.title()}",
        "",
        f"- **Total:** {parse_error_count} parse errors, {total_errors} errors, "
        f"{total_warnings} warnings across {len(results)} {type_name}",
        f"- **Zero errors:** {zero_error_count} {type_name} ({zero_error_percentage:.1f}%)",
    ]

    if type_name == "modules" and module_meta_stats and module_meta_stats.get("details"):
        _meta_mod = [d for d in module_meta_stats["details"] if d.get("type", "module") == "module"]
        _tv_pass = sum(1 for d in _meta_mod if d["has_topics"] and d["has_versions"])
        _tv_pct = _tv_pass / len(_meta_mod) * 100 if _meta_mod else 0
        lines.append(
            f"- **Topic + Version:** {_tv_pass}/{len(_meta_mod)} ({_tv_pct:.1f}%) modules have "
            "`topics:` and `versions:` in meta.yml"
        )

    if type_name == "subworkflows" and module_meta_stats and module_meta_stats.get("details"):
        _meta_swf = [d for d in module_meta_stats["details"] if d.get("type") == "subworkflow"]
        _v_pass = sum(1 for d in _meta_swf if not d["has_versions"])
        _v_pct = _v_pass / len(_meta_swf) * 100 if _meta_swf else 0
        lines.append(
            f"- **Versions channel:** {_v_pass}/{len(_meta_swf)} ({_v_pct:.1f}%) subworkflows "
            "do not emit a `versions` output channel"
        )

    lines.append("")

    # Build per-row meta lookup
    meta_lookup: dict[str, dict] = {}
    if module_meta_stats and module_meta_stats.get("details"):
        for _d in module_meta_stats["details"]:
            meta_lookup[_d["name"]] = _d

    # Add charts in a side-by-side table (charts are in LINT_RESULTS_DIR with type-prefixed names)
    errors_chart = LINT_RESULTS_DIR / f"{type_name}_errors.png"
    warnings_chart = LINT_RESULTS_DIR / f"{type_name}_warnings.png"
    if include_charts and errors_chart.exists() and warnings_chart.exists():
        lines.extend(
            [
                "| Errors | Warnings |",
                "|:------:|:--------:|",
                f"| ![Errors]({errors_chart}) | ![Warnings]({warnings_chart}) |",
                "",
            ]
        )

    # For modules: add meta.yml topic version chart if it exists
    meta_chart = LINT_RESULTS_DIR / "modules_topic_versions.png"
    if include_charts and type_name == "modules" and meta_chart.exists():
        lines.extend(
            [
                "| Module Topic Version Usage |",
                "|:---------------------------:|",
                f"| ![Topic Version Usage]({meta_chart}) |",
                "",
            ]
        )

    # Filter results for table display if show_only_errors is True
    if show_only_errors:
        table_results = [r for r in sorted_results if r.get("parse_error", False) or r["errors"] > 0]
        table_count = len(table_results)
        summary_text = f"{type_singular.title()} Results ({table_count} {type_name} with errors)"
    else:
        table_results = sorted_results
        table_count = len(results)
        summary_text = f"{type_singular.title()} Results ({table_count} {type_name})"

    # Results table in a collapsible details section
    if show_prints_help:
        table_header = (
            f"| {type_singular.title()} | Parse Error | Errors | Warnings | Prints Help | Lint Output | Help Output |"
        )
        table_separator = "|----------|:-----------:|-------:|---------:|:-----------:|:-----------:|:-----------:|"
    elif type_name == "modules":
        table_header = (
            f"| {type_singular.title()} | Parse Error | Errors | Warnings | `topics:` | `versions:` | Lint Output |"
        )
        table_separator = "|----------|:-----------:|-------:|---------:|:---------:|:----------:|:-----------:|"
    elif type_name == "subworkflows":
        table_header = f"| {type_singular.title()} | Parse Error | Errors | Warnings | versions channel | Lint Output |"
        table_separator = "|----------|:-----------:|-------:|---------:|:----------------:|:-----------:|"
    else:
        table_header = f"| {type_singular.title()} | Parse Error | Errors | Warnings | Lint Output |"
        table_separator = "|----------|:-----------:|-------:|---------:|:-----------:|:-----------:|"

    lines.extend(
        [
            "<details>",
            f"<summary>{summary_text}</summary>",
            "",
            table_header,
            table_separator,
        ]
    )

    for result in table_results:
        errors = result["errors"]
        warnings = result["warnings"]
        parse_error = result.get("parse_error", False)
        prints_help = result.get("prints_help")

        if parse_error:
            parse_error_str = "Yes"
            error_str = "-"
            warning_str = "-"
            status_emoji = ":x:"
        else:
            parse_error_str = "No"
            error_str = str(errors)
            warning_str = str(warnings)
            # For pipelines: only show checkmark if no errors AND prints_help passes
            # For other types (no prints_help test): show checkmark if no errors
            if show_prints_help:
                status_emoji = ":white_check_mark:" if errors == 0 and prints_help is True else ":x:"
            else:
                status_emoji = ":white_check_mark:" if errors == 0 else ":x:"

        name_link = f"{status_emoji} [{result['name']}]({result['html_url']})"
        lint_file_link = f"[View]({lint_results_dir}/{result['name']}_lint.md)"

        if show_prints_help:
            if prints_help is None:
                prints_help_str = "-"
                help_file_link = "-"
            elif prints_help:
                prints_help_str = "Yes"
                help_file_link = f"[View]({PRINTS_HELP_RESULTS_DIR}/{result['name']}_help.txt)"
            else:
                prints_help_str = "No"
                help_file_link = f"[View]({PRINTS_HELP_RESULTS_DIR}/{result['name']}_help.txt)"
            row = (
                f"| {name_link} | {parse_error_str} | {error_str} | {warning_str} "
                f"| {prints_help_str} | {lint_file_link} | {help_file_link} |"
            )
            lines.append(row)
        elif type_name == "modules":
            meta = meta_lookup.get(result["name"], {})
            topics_str = ":white_check_mark:" if meta.get("has_topics") else ":x:"
            versions_str = ":white_check_mark:" if meta.get("has_versions") else ":x:"
            lines.append(
                f"| {name_link} | {parse_error_str} | {error_str} | {warning_str} "
                f"| {topics_str} | {versions_str} | {lint_file_link} |"
            )
        elif type_name == "subworkflows":
            meta = meta_lookup.get(result["name"], {})
            versions_str = ":x:" if meta.get("has_versions") else ":white_check_mark:"
            lines.append(
                f"| {name_link} | {parse_error_str} | {error_str} | {warning_str} | {versions_str} | {lint_file_link} |"
            )
        else:
            lines.append(f"| {name_link} | {parse_error_str} | {error_str} | {warning_str} | {lint_file_link} |")

    # Add note about hidden zero-error items if filtering
    if show_only_errors and zero_error_count > 0:
        lines.extend(
            [
                "",
                f"_{type_name.title()} with zero errors are not shown above ({zero_error_count} {type_name}). "
                f"They may still have warnings. See the [{type_name} results directory]({lint_results_dir}/) "
                "for all lint outputs._",
            ]
        )

    lines.extend(
        [
            "",
            "</details>",
            "",
        ]
    )

    return lines


def generate_readme(
    pipeline_results: list[dict] | None = None,
    module_results: list[dict] | None = None,
    subworkflow_results: list[dict] | None = None,
    include_charts: bool = False,
    nextflow_version: str = "unknown",
    module_meta_stats: dict | None = None,
) -> str:
    """Generate README content with results for all types."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "# sanger-tol Strict Syntax Health Report",
        "",
        "This repository tracks the health of sanger-tol pipelines, modules, and subworkflows "
        "with respect to Nextflow's _strict syntax_ linting.",
        "It is a mere sanger-tol-ification of the upstream nf-core <https://github.com/nf-core/strict-syntax-health>.",
        "",
        "The [Nextflow docs](https://www.nextflow.io/docs/latest/strict-syntax.html) describes the differences "
        "from standard Nextflow syntax and includes many examples to help with migration and fixing errors.",
        "Strict syntax is backwards compatible with existing Nextflow code, "
        "but enforces stricter rules to catch common errors and improve code quality.",
        "",
        "The goal is for all sanger-tol pipelines to run without errors using strict syntax.",
        "",
        "> [!IMPORTANT]",
        "> See the [nf-core blog post](https://nf-co.re/blog/2025/nextflow_syntax_nf-core_roadmap) "
        "for details on the migration timeline.",
        "> **Fixing all errors from `nextflow lint` will be a requirement by early spring 2026.**",
        "",
        f"- **Last updated:** {now}",
        f"- **Nextflow version:** {nextflow_version}",
        "",
    ]

    # Add sections for each type
    # Pipelines show all results; modules/subworkflows only show items with errors to reduce README size
    if pipeline_results:
        lines.extend(
            _generate_results_section(
                pipeline_results,
                "pipelines",
                "pipeline",
                PIPELINES_LINT_RESULTS_DIR,
                include_charts,
                show_prints_help=True,
            )
        )

    if module_results:
        lines.extend(
            _generate_results_section(
                module_results,
                "modules",
                "module",
                MODULES_LINT_RESULTS_DIR,
                include_charts,
                module_meta_stats=module_meta_stats,
            )
        )

    if subworkflow_results:
        lines.extend(
            _generate_results_section(
                subworkflow_results,
                "subworkflows",
                "subworkflow",
                SUBWORKFLOWS_LINT_RESULTS_DIR,
                include_charts,
                module_meta_stats=module_meta_stats,
            )
        )

    lines.extend(
        [
            "## About",
            "",
            "This report is generated daily by running `nextflow lint` on each sanger-tol pipeline, module, "
            "and subworkflow.",
            "The linting checks for strict syntax compliance in Nextflow DSL2 code.",
            "",
            "- **Parse errors** indicate items where `nextflow lint` could not run at all, "
            "typically due to syntax errors that prevent Nextflow from parsing the code",
            "- **Errors** indicate syntax issues that will cause problems in future Nextflow versions",
            "- **Warnings** indicate deprecated patterns that should be updated, "
            "but having warnings is fine (though it's nice to fix those as well if possible)",
            "- **Prints Help** (pipelines only) tests whether the pipeline can print its help message "
            "using the v2 syntax parser (`NXF_SYNTAX_PARSER=v2 nextflow run . --help`). "
            "This test only runs for pipelines with zero lint errors.",
            "",
            "## Running Locally",
            "",
            "You can run `nextflow lint` on your own pipeline to check for strict syntax issues:",
            "",
            "```bash",
            "nextflow lint .",
            "```",
            "",
            "> **Note:** Until [this fix](https://github.com/nextflow-io/nextflow/pull/6716) is included "
            "in a Nextflow edge release, you may need to exclude nf-test files manually:",
            "> ```bash",
            '> nextflow lint . -exclude ".git,.nf-test,nf-test.config"',
            "> ```",
            "",
            "See the [strict syntax documentation](https://www.nextflow.io/docs/latest/strict-syntax.html) "
            "for more information about the rules being checked.",
            "",
            "## Getting Help",
            "",
            "If you need help fixing strict syntax errors in your pipeline, "
            "the [Nextflow community forum](https://community.seqera.io/) is a great place to ask questions.",
            "",
        ]
    )

    return "\n".join(lines)


def send_slack_report(
    module_results: list[dict] | None,
    subworkflow_results: list[dict] | None,
    slack_webhook_url: str,
    module_meta_stats: dict | None = None,
) -> None:
    """Send a Slack report of lint errors and warnings for modules and subworkflows.

    Uses a Slack Incoming Webhook URL, which is pre-configured for a specific channel
    and does not require a separate channel parameter.

    Args:
        module_results: List of module lint result dicts (or None if not linted).
        subworkflow_results: List of subworkflow lint result dicts (or None if not linted).
        slack_webhook_url: Slack Incoming Webhook URL (pre-configured for the target channel).
        module_meta_stats: Optional dict from scan_modules_meta_yml_stats with topics/versions coverage.
    """
    components_with_errors: list[str] = []
    components_with_warnings: list[str] = []
    total_errors = 0
    total_warnings = 0

    lint_dirs = {
        "module": MODULES_LINT_RESULTS_DIR,
        "subworkflow": SUBWORKFLOWS_LINT_RESULTS_DIR,
    }

    for type_label, results in [("module", module_results or []), ("subworkflow", subworkflow_results or [])]:
        lint_dir = lint_dirs[type_label]
        for r in results:
            lint_url = f"{REPO_BASE_URL}/{lint_dir}/{r['name']}_lint.md"
            if r.get("parse_error"):
                components_with_errors.append(f":x: [{type_label}] {r['name']} (parse error)")
                continue
            if r["errors"] > 0:
                components_with_errors.append(
                    f":x: [{type_label}] <{lint_url}|{r['name']}> — {r['errors']} error(s), {r['warnings']} warning(s)"
                )
                total_errors += r["errors"]
                total_warnings += r["warnings"]
            elif r["warnings"] > 0:
                components_with_warnings.append(
                    f":warning: [{type_label}] <{lint_url}|{r['name']}> — {r['warnings']} warning(s)"
                )
                total_warnings += r["warnings"]

    # Build summary text
    if total_errors == 0 and total_warnings == 0:
        summary = ":white_check_mark: No errors or warnings in modules/subworkflows."
    else:
        parts = []
        if total_errors:
            parts.append(f"*{total_errors} error(s)*")
        if total_warnings:
            parts.append(f"*{total_warnings} warning(s)*")
        summary = " | ".join(parts)

    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":mag: Strict Syntax Health — Modules & Subworkflows",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": summary},
        },
    ]

    MAX_ITEMS = 20  # Slack block text limit is 3 000 chars; cap list length for safety

    if components_with_errors:
        blocks.append({"type": "divider"})
        listed = "\n".join(components_with_errors[:MAX_ITEMS])
        overflow = len(components_with_errors) - MAX_ITEMS
        if overflow > 0:
            listed += f"\n_…and {overflow} more_"
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": f"*Components with errors:*\n{listed}"}})

    if components_with_warnings:
        blocks.append({"type": "divider"})
        listed = "\n".join(components_with_warnings[:MAX_ITEMS])
        overflow = len(components_with_warnings) - MAX_ITEMS
        if overflow > 0:
            listed += f"\n_…and {overflow} more_"
        blocks.append(
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*Components with warnings only:*\n{listed}"}}
        )

    if module_meta_stats and module_meta_stats.get("total", 0) > 0:
        details = module_meta_stats.get("details", [])

        # Modules: topics + versions in meta.yml
        mod_total = sum(1 for d in details if d.get("type", "module") == "module")
        mod_pass = module_meta_stats.get("with_topic_versions", 0)
        mod_fail = module_meta_stats.get("without_topic_versions", 0)
        mod_pct = mod_pass / mod_total * 100 if mod_total else 0
        mod_text = f":books: *Modules topic+versions:* {mod_pass}/{mod_total} ({mod_pct:.1f}%)"
        if mod_fail > 0:
            mod_text += f" — {mod_fail} missing"

        # Subworkflows: passing = no versions channel (has_versions=False)
        swf_total = sum(1 for d in details if d.get("type") == "subworkflow")
        swf_pass = module_meta_stats.get("subworkflow_without_versions", 0)
        swf_fail = module_meta_stats.get("subworkflow_with_versions", 0)
        swf_pct = swf_pass / swf_total * 100 if swf_total else 0
        swf_text = f":no_entry_sign: *Subworkflows without versions channel:* {swf_pass}/{swf_total} ({swf_pct:.1f}%)"
        if swf_fail > 0:
            swf_text += f" — {swf_fail} still emit versions"

        blocks.append({"type": "divider"})
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": f"{mod_text}\n{swf_text}"}})

        if mod_fail > 0:
            missing_mods = [
                d
                for d in details
                if d.get("type", "module") == "module" and not (d["has_topics"] and d["has_versions"])
            ]
            missing_mods.sort(key=lambda x: x["name"])
            capped = missing_mods[:MAX_ITEMS]
            mod_lines = [f"• <{d['html_url']}|{d['name']}>" if d["html_url"] else f"• {d['name']}" for d in capped]
            overflow = len(missing_mods) - MAX_ITEMS
            if overflow > 0:
                mod_lines.append(f"_…and {overflow} more_")
            blocks.append(
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "*Modules missing topics/versions:*\n" + "\n".join(mod_lines)},
                }
            )

        if swf_fail > 0:
            # failing = those that still emit a versions channel (has_versions=True)
            offending_swf = [d for d in details if d.get("type") == "subworkflow" and d["has_versions"]]
            offending_swf.sort(key=lambda x: x["name"])
            capped = offending_swf[:MAX_ITEMS]
            swf_lines = [f"• <{d['html_url']}|{d['name']}>" if d["html_url"] else f"• {d['name']}" for d in capped]
            overflow = len(offending_swf) - MAX_ITEMS
            if overflow > 0:
                swf_lines.append(f"_…and {overflow} more_")
            blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Subworkflows still emitting a versions channel:*\n" + "\n".join(swf_lines),
                    },
                }
            )

    fallback_text = (
        f"Strict Syntax Health: {total_errors} error(s), {total_warnings} warning(s) in modules/subworkflows"
    )
    # Incoming Webhook payload: no channel field needed — it is baked into the webhook URL
    payload = {"text": fallback_text, "blocks": blocks}

    try:
        response = httpx.post(
            slack_webhook_url,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        if response.text == "ok":
            console.print("[green]Slack report sent successfully[/green]")
        else:
            console.print(f"[red]Unexpected Slack webhook response: {response.text}[/red]")
    except httpx.HTTPStatusError as exc:
        console.print(f"[red]Slack webhook returned HTTP {exc.response.status_code}[/red]")
    except httpx.HTTPError as exc:
        console.print(f"[red]HTTP error while sending Slack report: {exc}[/red]")


@click.command()
@click.option(
    "--update-readme",
    is_flag=True,
    help="Update the README.md file with the results",
)
@click.option(
    "--update-pipelines",
    is_flag=True,
    help="Download the latest pipelines.json from nf-co.re before running",
)
@click.option(
    "--pipeline",
    "-p",
    multiple=True,
    help="Only process specific pipeline(s) by name (can be used multiple times)",
)
@click.option(
    "--module",
    "-m",
    multiple=True,
    help="Only process specific module(s) by name (can be used multiple times)",
)
@click.option(
    "--subworkflow",
    "-s",
    multiple=True,
    help="Only process specific subworkflow(s) by name (can be used multiple times)",
)
@click.option(
    "--skip-pipelines",
    is_flag=True,
    help="Skip linting pipelines",
)
@click.option(
    "--skip-modules",
    is_flag=True,
    help="Skip linting modules",
)
@click.option(
    "--skip-subworkflows",
    is_flag=True,
    help="Skip linting subworkflows",
)
@click.option(
    "--generate-charts-only",
    is_flag=True,
    help="Only generate charts and README from existing history files (no linting)",
)
@click.option(
    "--no-cache",
    is_flag=True,
    help="Ignore commit cache and re-lint everything (by default, unchanged repos are skipped)",
)
@click.option(
    "--slack-webhook",
    envvar="SLACK_WEBHOOK_URL",
    default=None,
    show_envvar=True,
    help=(
        "Slack Incoming Webhook URL (pre-configured for the target channel). "
        "Can also be set via the SLACK_WEBHOOK_URL env var — preferred in CI to avoid "
        "the URL appearing in process lists or log output."
    ),
)
def main(
    update_readme: bool,
    update_pipelines: bool,
    pipeline: tuple[str, ...],
    module: tuple[str, ...],
    subworkflow: tuple[str, ...],
    skip_pipelines: bool,
    skip_modules: bool,
    skip_subworkflows: bool,
    generate_charts_only: bool,
    no_cache: bool,
    slack_webhook: str | None,
) -> None:
    """Check sanger-tol pipelines, modules, and subworkflows for Nextflow strict syntax linting issues."""
    if update_pipelines:
        update_pipelines_json()

    # Get nextflow version
    nextflow_version = get_nextflow_version()
    console.print(f"Using Nextflow version: {nextflow_version}")

    # Generate charts only mode - skip linting, load existing results and generate outputs
    if generate_charts_only:
        console.print("[bold]Generate charts only mode - loading existing data...[/bold]")

        # Load results from JSON files (saved by lint jobs)
        pipeline_results = load_results_for_type("pipelines") or None
        module_results = load_results_for_type("modules") or None
        subworkflow_results = load_results_for_type("subworkflows") or None

        # Load history and generate charts
        history = load_history()
        generate_all_charts(history)

        # Load saved meta stats if available
        saved_meta_stats = None
        if MODULES_META_STATS_PATH.exists():
            try:
                saved_meta_stats = json.loads(MODULES_META_STATS_PATH.read_text())
            except json.JSONDecodeError:
                pass

        if update_readme:
            readme_content = generate_readme(
                pipeline_results=pipeline_results,
                module_results=module_results,
                subworkflow_results=subworkflow_results,
                include_charts=True,
                nextflow_version=nextflow_version,
                module_meta_stats=saved_meta_stats,
            )
            README_PATH.write_text(readme_content)
            console.print(f"\n[green]Updated {README_PATH}[/green]")
        return

    pipeline_results: list[dict] | None = None
    module_results: list[dict] | None = None
    subworkflow_results: list[dict] | None = None

    # Lint pipelines
    if not skip_pipelines:
        pipelines = load_pipelines()

        if pipeline:
            pipeline_names = set(pipeline)
            pipelines = [p for p in pipelines if p["name"] in pipeline_names]
            if not pipelines:
                console.print(f"[red]No matching pipelines found for: {', '.join(pipeline_names)}[/red]")
                sys.exit(1)
            console.print(f"Filtering to {len(pipelines)} pipeline(s): {', '.join(p['name'] for p in pipelines)}")

        pipeline_results = run_pipeline_lint(pipelines, no_cache=no_cache)
        display_results(pipeline_results, type_name="pipeline", show_prints_help=True)
        # Save results for aggregation (only when not filtering specific pipelines)
        if not pipeline:
            save_results_for_type("pipelines", pipeline_results)

    # Lint modules and subworkflows (requires modules repo)
    if not skip_modules or not skip_subworkflows:
        # Check if we can skip cloning by using cached results
        # Only use cache when linting ALL modules/subworkflows (no -m/-s filters)
        use_modules_cache = not module and not subworkflow and not no_cache
        modules_repo_unchanged, remote_commit = check_modules_repo_unchanged(
            MODULES_REPO_URL,
            no_cache=not use_modules_cache,
            check_modules=not skip_modules,
            check_subworkflows=not skip_subworkflows,
        ) and check_modules_repo_unchanged(
            NFCORE_MODULES_REPO_URL,
            prefix="nfcore",
            no_cache=not use_modules_cache,
            check_modules=not skip_modules,
            check_subworkflows=False,
        )

        if modules_repo_unchanged:
            console.print(f"[dim]modules repos unchanged at {remote_commit[:8]} - using cached results[/dim]")
            repo_commit = remote_commit
        else:
            # Clone/update the sanger-tol repo
            repo_commit = clone_modules_repo()
            # Clone/update the nf-core repo
            clone_nfcore_modules_repo()
            # Setup the symlink
            link_nfcore_modules()

        if not skip_modules:
            if modules_repo_unchanged:
                # Use cached results - need to load module list for the cache lookup
                # We need the modules repo to be present for discover_modules, but since it's unchanged
                # we can just use the cached results directly
                modules_cache = load_results_dict_for_type("modules")
                # Build modules list from cache keys (excluding _repo_commit)
                base_url = "https://github.com/sanger-tol/nf-core-modules/tree/main/modules/sanger-tol"
                modules = [
                    {"name": name, "html_url": f"{base_url}/{name.replace('_', '/')}"}
                    for name in modules_cache.keys()
                    if name != "_repo_commit"
                ]
                module_results = load_cached_modules_results(modules)
                console.print(f"[dim]Loaded {len(module_results)} cached module results[/dim]")
            else:
                modules = discover_modules()

                if module:
                    module_names = set(module)
                    modules = [m for m in modules if m["name"] in module_names]
                    if not modules:
                        console.print(f"[red]No matching modules found for: {', '.join(module_names)}[/red]")
                        sys.exit(1)
                    console.print(f"Filtering to {len(modules)} module(s): {', '.join(m['name'] for m in modules)}")

                module_results = run_modules_lint(modules, nextflow_version)

            display_results(module_results, type_name="module")
            # Save results for aggregation (only when not filtering specific modules)
            if not module:
                save_results_for_type("modules", module_results, repo_commit=repo_commit)

        if not skip_subworkflows:
            if modules_repo_unchanged:
                # Use cached results
                subworkflows_cache = load_results_dict_for_type("subworkflows")
                base_url = "https://github.com/sanger-tol/nf-core-modules/tree/main/subworkflows/sanger-tol"
                subworkflows = [
                    {"name": name, "html_url": f"{base_url}/{name}"}
                    for name in subworkflows_cache.keys()
                    if name != "_repo_commit"
                ]
                subworkflow_results = load_cached_subworkflows_results(subworkflows)
                console.print(f"[dim]Loaded {len(subworkflow_results)} cached subworkflow results[/dim]")
            else:
                subworkflows = discover_subworkflows()

                if subworkflow:
                    subworkflow_names = set(subworkflow)
                    subworkflows = [s for s in subworkflows if s["name"] in subworkflow_names]
                    if not subworkflows:
                        console.print(f"[red]No matching subworkflows found for: {', '.join(subworkflow_names)}[/red]")
                        sys.exit(1)
                    console.print(
                        f"Filtering to {len(subworkflows)} subworkflow(s): {', '.join(s['name'] for s in subworkflows)}"
                    )

                subworkflow_results = run_subworkflows_lint(subworkflows, nextflow_version)

            display_results(subworkflow_results, type_name="subworkflow")
            # Save results for aggregation (only when not filtering specific subworkflows)
            if not subworkflow:
                save_results_for_type("subworkflows", subworkflow_results, repo_commit=repo_commit)

    # Update history and generate charts
    # History is updated per-type when all items of that type are linted (no -p/-m/-s filters)
    include_charts = False

    # Scan meta.yml topics and versions usage (only when all modules or all subworkflows were linted)
    module_meta_stats: dict | None = None
    if MODULES_DIR.exists() and (
        (module_results is not None and not module) or (subworkflow_results is not None and not subworkflow)
    ):
        module_meta_stats = scan_modules_meta_yml_stats()
        display_meta_stats(module_meta_stats)
        # Save for --generate-charts-only reuse
        MODULES_META_STATS_PATH.parent.mkdir(parents=True, exist_ok=True)
        MODULES_META_STATS_PATH.write_text(json.dumps(module_meta_stats, indent=2) + "\n")
        console.print(f"Saved meta stats to {MODULES_META_STATS_PATH}")

    # Update history for each type that was fully linted
    if pipeline_results is not None and not pipeline:
        update_history(pipeline_results=pipeline_results)

    if module_results is not None and not module:
        update_history(module_results=module_results, module_meta_stats=module_meta_stats)

    if subworkflow_results is not None and not subworkflow:
        update_history(subworkflow_results=subworkflow_results)

    # Generate charts if any results were produced
    if pipeline_results is not None or module_results is not None or subworkflow_results is not None:
        full_history = load_history()
        generate_all_charts(full_history)
        include_charts = True

    if update_readme:
        readme_content = generate_readme(
            pipeline_results=pipeline_results,
            module_results=module_results,
            subworkflow_results=subworkflow_results,
            include_charts=include_charts,
            nextflow_version=nextflow_version,
            module_meta_stats=module_meta_stats,
        )
        README_PATH.write_text(readme_content)
        console.print(f"\n[green]Updated {README_PATH}[/green]")

    # Send Slack report for modules/subworkflows when a webhook URL is configured
    if slack_webhook:
        if module_results is not None or subworkflow_results is not None:
            send_slack_report(module_results, subworkflow_results, slack_webhook, module_meta_stats=module_meta_stats)
        else:
            console.print("[dim]Slack report skipped: no module/subworkflow results to report.[/dim]")


if __name__ == "__main__":
    main()
