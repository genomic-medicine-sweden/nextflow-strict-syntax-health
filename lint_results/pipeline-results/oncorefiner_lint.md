# Nextflow lint results

- Generated: 2026-06-04T00:46:40.799803347Z
- Nextflow version: 26.04.3
- Summary: 7 warnings

## :warning: Warnings

- Warning: `main.nf:79:5`: Variable was declared but not used

  ```nextflow
      ch_svdb_dbs        = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `main.nf:186:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      multiqc_report = ONCOREFINER.out.multiqc_report // channel: /path/to/multiqc_report.html
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_references/main.nf:32:9`: Emit name should be omitted when there is only one emit

  ```nextflow
          vep_resources = ch_vep_resources // channel: [vep_cache_files]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:43:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      dummy_emit = true
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:20:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      valid_config = valid_config
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfschema_plugin/main.nf:72:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      dummy_emit = true
      ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/oncorefiner.nf:23:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_samplesheet                  // channel: [mandatory] samplesheet read in from --input
          ^^^^^^^^^^^^^^
  ```
