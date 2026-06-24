# Nextflow lint results

- Generated: 2026-06-24T00:33:23.411961199Z
- Nextflow version: 26.05.0-edge
- Summary: 7 warnings

## :warning: Warnings

- Warning: `main.nf:106:5`: Variable was declared but not used

  ```nextflow
      ch_svdb_dbs        = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_references/main.nf:32:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      vep_resources = ch_vep_resources // channel: [vep_cache_files]
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:83:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      versions = ch_versions
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:277:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ].findAll { key, value -> value != null }
                  ^^^
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
