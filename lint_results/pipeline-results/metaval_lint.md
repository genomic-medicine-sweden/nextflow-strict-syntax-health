# Nextflow lint results

- Generated: 2026-04-16T00:26:56.917584906Z
- Nextflow version: 26.03.2-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/local/blast/main.nf:68:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_query_for_blastx = query.filter { meta, fasta -> meta.tool != 'diamond' }
                                                     ^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:16:5`: Variable was declared but not used

  ```nextflow
      valid_config = checkConfigProvided()
      ^^^^^^^^^^^^
  ```
