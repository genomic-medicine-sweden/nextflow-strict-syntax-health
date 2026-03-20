# Nextflow lint results

- Generated: 2026-03-20T15:16:33.740979266Z
- Nextflow version: 26.03.0-edge
- Summary: 21 warnings

## :warning: Warnings

- Warning: `modules/local/microfinder_filter/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/microfinder_filter/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix      = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/microfinder_filter/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/sort_fasta/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/sort_fasta/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix      = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/sort_fasta/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def VERSION     = "2.2.3"
          ^^^^^^^
  ```

- Warning: `modules/local/sort_fasta/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/sort_fasta/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def prefix      = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/microfinder_map/main.nf:27:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/microfinder_map/main.nf:45:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .multiMap { pep_meta, pep_file, miniprot_meta, miniprot_index ->
                                          ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/microfinder_map/main.nf:101:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          tsv_branched.has_content.map { meta, tsv_file, ref_meta, ref_file -> tuple(meta, tsv_file) },
                                                         ^^^^^^^^
  ```

- Warning: `subworkflows/local/microfinder_map/main.nf:101:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          tsv_branched.has_content.map { meta, tsv_file, ref_meta, ref_file -> tuple(meta, tsv_file) },
                                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/microfinder_map/main.nf:102:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          tsv_branched.has_content.map { meta, tsv_file, ref_meta, ref_file -> ref_file },
                                         ^^^^
  ```

- Warning: `subworkflows/local/microfinder_map/main.nf:102:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          tsv_branched.has_content.map { meta, tsv_file, ref_meta, ref_file -> ref_file },
                                               ^^^^^^^^
  ```

- Warning: `subworkflows/local/microfinder_map/main.nf:102:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          tsv_branched.has_content.map { meta, tsv_file, ref_meta, ref_file -> ref_file },
                                                         ^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nfmicrofinder_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nfmicrofinder_pipeline/main.nf:85:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nfmicrofinder_pipeline/main.nf:89:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nfmicrofinder_pipeline/main.nf:94:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nfmicrofinder_pipeline/main.nf:98:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/nfmicrofinder.nf:49:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
