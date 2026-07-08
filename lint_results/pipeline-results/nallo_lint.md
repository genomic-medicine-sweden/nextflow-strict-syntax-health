# Nextflow lint results

- Generated: 2026-07-08T00:26:20.151082774Z
- Nextflow version: 26.06.0-edge
- Summary: 7 warnings

## :warning: Warnings

- Warning: `subworkflows/local/annotate_methylation/main.nf:35:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      methylation_annotation = CSVTK_SORT.out.sorted // channel: [ val(meta), path(tsv) ]
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/chromograph/main.nf:100:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      chromograph_plots = RUN_CHROMOGRAPH.out.plots // channel: [ val(meta), path(plot) ]
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/split_multisample_vcf/main.nf:30:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      split_vcf = ch_split_vcf // channel: [ val(meta), path(vcf), val(variant_type) ]
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nallo_pipeline/main.nf:330:5`: Emit name should be omitted when there is only one emit

  ```nextflow
      samplesheet = ch_samplesheet
      ^^^^^^^^^^^^^^^^^^^^^^^^^^
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
