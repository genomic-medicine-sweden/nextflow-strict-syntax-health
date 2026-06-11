# Nextflow lint results

- Generated: 2026-06-11T00:42:22.766013168Z
- Nextflow version: 26.04.3
- Summary: 6 warnings

## :warning: Warnings

- Warning: `main.nf:47:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      multiqc_report = METAVAL.out.multiqc_report // channel: /path/to/multiqc_report.html
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/blast/main.nf:68:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_query_for_blastx = query.filter { meta, fasta -> meta.tool != 'diamond' }
                                                     ^^^^^
  ```

- Warning: `subworkflows/local/consensus/main.nf:52:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      consensus = ch_consensus // channel: [ val(meta), path(consensus) ]
      ^^^^^^^^^^^^^^^^^^^^^^
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
