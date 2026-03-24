# Nextflow lint results

- Generated: 2026-03-24T10:46:51.323647744Z
- Nextflow version: 26.03.0-edge
- Summary: 5 warnings

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_purging_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_purging_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/purging.nf:19:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_samplesheet // channel: samplesheet read in from --input
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/purging.nf:27:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/purging.nf:51:17`: Variable was declared but not used

  ```nextflow
          ).set { ch_collated_versions }
                  ^^^^^^^^^^^^^^^^^^^^
  ```
