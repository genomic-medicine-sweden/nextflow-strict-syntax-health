# Nextflow lint results

- Generated: 2026-03-24T10:44:10.320183390Z
- Nextflow version: 26.03.0-edge
- Summary: 1 error, 7 warnings

## :x: Errors

- Error: `main.nf:161:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/blast/blastn/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/blast/makeblastdb/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args           = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/sanger-tol/samtools/mergedup/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args  ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/generate_genomes/main.nf:10:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      barcodes
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/generate_html_report/main.nf:20:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      params_file                // channel: [ params_file ]
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ascc_pipeline/main.nf:39:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ascc_pipeline/main.nf:209:5`: Variable was declared but not used

  ```nextflow
      versions = ch_versions.mix(PREPARE_BLASTDB.out.versions)
      ^^^^^^^^
  ```
