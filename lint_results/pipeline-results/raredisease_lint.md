# Nextflow lint results

- Generated: 2026-07-16T00:28:19.157272627Z
- Nextflow version: 26.07.0-edge
- Summary: 12 warnings

## :warning: Warnings

- Warning: `subworkflows/local/call_snv_sentieon/main.nf:67:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def sorted = [vcfs, idxs].transpose().sort { it[0].name }
                                                               ^^
  ```

- Warning: `subworkflows/local/call_snv_sentieon/main.nf:68:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [meta, sorted.collect { it[0] }, sorted.collect { it[1] }]
                                                 ^^
  ```

- Warning: `subworkflows/local/call_snv_sentieon/main.nf:68:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [meta, sorted.collect { it[0] }, sorted.collect { it[1] }]
                                                                           ^^
  ```

- Warning: `subworkflows/local/call_sv_MT/main.nf:145:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { !it.isEmpty() }
                             ^^
  ```

- Warning: `subworkflows/local/contamination_check/main.nf:32:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { vcf, tbi -> vcf }
                      ^^^
  ```

- Warning: `subworkflows/local/contamination_check/main.nf:36:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { vcf, tbi -> tbi }
                 ^^^
  ```

- Warning: `workflows/raredisease.nf:433:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_contamination_mqc    = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:434:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_contamination_table  = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:435:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_contamination_pileup = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:1069:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_config        = channel.fromPath(
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:1071:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_custom_config = val_multiqc_config ?
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:1074:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_logo          = val_multiqc_logo ?
      ^^^^^^^^^^^^^^^
  ```
