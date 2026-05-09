# Nextflow lint results

- Generated: 2026-05-09T00:29:48.167486806Z
- Nextflow version: 26.04.0
- Summary: 5 warnings

## :warning: Warnings

- Warning: `main.nf:74:5`: Variable was declared but not used

  ```nextflow
      ch_svdb_dbs        = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:16:5`: Variable was declared but not used

  ```nextflow
      valid_config = checkConfigProvided()
      ^^^^^^^^^^^^
  ```

- Warning: `workflows/oncorefiner.nf:40:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_samplesheet           // channel: [mandatory] samplesheet read in from --input
          ^^^^^^^^^^^^^^
  ```
