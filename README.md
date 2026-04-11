# genomic-medicine-sweden Strict Syntax Health Report

This repository tracks the health of genomic-medicine-sweden pipelines, modules, and subworkflows with respect to Nextflow's _strict syntax_ linting.
It is a mere genomic-medicine-sweden-ification of the upstream nf-core <https://github.com/nf-core/strict-syntax-health>.

The [Nextflow docs](https://www.nextflow.io/docs/latest/strict-syntax.html) describes the differences from standard Nextflow syntax and includes many examples to help with migration and fixing errors.
Strict syntax is backwards compatible with existing Nextflow code, but enforces stricter rules to catch common errors and improve code quality.

The goal is for all genomic-medicine-sweden pipelines to run without errors using strict syntax.

> [!IMPORTANT]
> See the [nf-core blog post](https://nf-co.re/blog/2025/nextflow_syntax_nf-core_roadmap) for details on the migration timeline.
> **Fixing all errors from `nextflow lint` will be a requirement by early spring 2026.**

- **Last updated:** 2026-04-11 00:21:32 UTC
- **Nextflow version:** 26.03.2-edge

## Pipelines

- **Strict syntax:** 0 parse errors, 137 errors, 599 warnings across 12 pipelines
- **Versions Mix:** 4/12 (33.3%) pipelines do not use the `ch_versions += +ch_versions.mix` anti-pattern
- **Zero issues:** 0 pipelines (0.0%)

|                    Errors                    |                     Warnings                     |
| :------------------------------------------: | :----------------------------------------------: |
| ![Errors](lint_results/pipelines_errors.png) | ![Warnings](lint_results/pipelines_warnings.png) |

|                  Pipeline Versions Mix                   |
| :------------------------------------------------------: |
| ![Versions Mix](lint_results/pipelines_versions_mix.png) |

<details>
<summary>Pipeline Results (12 pipelines)</summary>

| Pipeline                                                                          | Parse Error | Errors | Warnings | Prints Help |         Versions Mix          |                          Lint Output                          |                          Help Output                          |
| --------------------------------------------------------------------------------- | :---------: | -----: | -------: | :---------: | :---------------------------: | :-----------------------------------------------------------: | :-----------------------------------------------------------: |
| :x: [jasen](https://github.com/genomic-medicine-sweden/jasen)                     |     No      |     74 |       25 |      -      | :negative_squared_cross_mark: |      [View](lint_results/pipeline-results/jasen_lint.md)      |                               -                               |
| :x: [metaval](https://github.com/genomic-medicine-sweden/metaval)                 |     No      |     35 |      114 |      -      | :negative_squared_cross_mark: |     [View](lint_results/pipeline-results/metaval_lint.md)     |                               -                               |
| :x: [rnafusion](https://github.com/nf-core/rnafusion)                             |     No      |     13 |      116 |      -      | :negative_squared_cross_mark: |    [View](lint_results/pipeline-results/rnafusion_lint.md)    |                               -                               |
| :x: [tomte](https://github.com/genomic-medicine-sweden/tomte)                     |     No      |      8 |      148 |      -      | :negative_squared_cross_mark: |      [View](lint_results/pipeline-results/tomte_lint.md)      |                               -                               |
| :x: [TRANA](https://github.com/genomic-medicine-sweden/TRANA)                     |     No      |      4 |       16 |      -      | :negative_squared_cross_mark: |      [View](lint_results/pipeline-results/TRANA_lint.md)      |                               -                               |
| :x: [nallorefs](https://github.com/genomic-medicine-sweden/nallorefs)             |     No      |      1 |       31 |      -      | :negative_squared_cross_mark: |    [View](lint_results/pipeline-results/nallorefs_lint.md)    |                               -                               |
| :x: [rarediseaserefs](https://github.com/genomic-medicine-sweden/rarediseaserefs) |     No      |      1 |        5 |      -      |      :white_check_mark:       | [View](lint_results/pipeline-results/rarediseaserefs_lint.md) |                               -                               |
| :x: [raredisease](https://github.com/nf-core/raredisease)                         |     No      |      1 |        5 |      -      |      :white_check_mark:       |   [View](lint_results/pipeline-results/raredisease_lint.md)   |                               -                               |
| :x: [taxprofiler](https://github.com/nf-core/taxprofiler)                         |     No      |      0 |       99 |     Yes     | :negative_squared_cross_mark: |   [View](lint_results/pipeline-results/taxprofiler_lint.md)   | [View](lint_results/prints-help-results/taxprofiler_help.txt) |
| :x: [nf-autoseq](https://github.com/genomic-medicine-sweden/nf-autoseq)           |     No      |      0 |       32 |     No      | :negative_squared_cross_mark: |   [View](lint_results/pipeline-results/nf-autoseq_lint.md)    | [View](lint_results/prints-help-results/nf-autoseq_help.txt)  |
| :x: [oncorefiner](https://github.com/clinical-genomics/oncorefiner)               |     No      |      0 |        7 |     No      |      :white_check_mark:       |   [View](lint_results/pipeline-results/oncorefiner_lint.md)   | [View](lint_results/prints-help-results/oncorefiner_help.txt) |
| :x: [nallo](https://github.com/genomic-medicine-sweden/nallo)                     |     No      |      0 |        1 |     Yes     |      :white_check_mark:       |      [View](lint_results/pipeline-results/nallo_lint.md)      |    [View](lint_results/prints-help-results/nallo_help.txt)    |

</details>

## About

This report is generated daily by running `nextflow lint` on each genomic-medicine-sweden pipeline, module, and subworkflow.
The linting checks for strict syntax compliance in Nextflow DSL2 code.

- **Parse errors** indicate items where `nextflow lint` could not run at all, typically due to syntax errors that prevent Nextflow from parsing the code
- **Errors** indicate syntax issues that will cause problems in future Nextflow versions
- **Warnings** indicate deprecated patterns that should be updated, but having warnings is fine (though it's nice to fix those as well if possible)
- **Prints Help** (pipelines only) tests whether the pipeline can print its help message using the v2 syntax parser (`NXF_SYNTAX_PARSER=v2 nextflow run . --help`). This test only runs for pipelines with zero lint errors.

## Running Locally

You can run `nextflow lint` on your own pipeline to check for strict syntax issues:

```bash
nextflow lint .
```

> **Note:** Until [this fix](https://github.com/nextflow-io/nextflow/pull/6716) is included in a Nextflow edge release, you may need to exclude nf-test files manually:
>
> ```bash
> nextflow lint . -exclude ".git,.nf-test,nf-test.config"
> ```

See the [strict syntax documentation](https://www.nextflow.io/docs/latest/strict-syntax.html) for more information about the rules being checked.

## Getting Help

If you need help fixing strict syntax errors in your pipeline, the [Nextflow community forum](https://community.seqera.io/) is a great place to ask questions.
