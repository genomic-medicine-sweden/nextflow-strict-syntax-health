# Nextflow lint results

- Generated: 2026-03-20T17:32:02.205475379Z
- Nextflow version: 26.03.0-edge
- Summary: 5 errors, 15 warnings

## :x: Errors

- Error: `subworkflows/local/zippypretext_map/main.nf:33:49`: `agp` is already declared

  ```nextflow
      PRETEXT_TO_ASM.out.correctedagp.map{ agpid, agp -> agp}.set{agp}
                                                  ^^^
  ```

- Error: `workflows/zippypretext.nf:32:33`: `input` is already declared

  ```nextflow
      input.combine(sample).map { input, sample -> tuple ( [ id: sample], input)}.set { fasta_tuple }
                                  ^^^^^
  ```

- Error: `workflows/zippypretext.nf:32:40`: `sample` is already declared

  ```nextflow
      input.combine(sample).map { input, sample -> tuple ( [ id: sample], input)}.set { fasta_tuple }
                                         ^^^^^^
  ```

- Error: `workflows/zippypretext.nf:33:34`: `hicmap` is already declared

  ```nextflow
      hicmap.combine(sample).map { hicmap, sample -> tuple ( [ id: sample], hicmap)}.set { hicmap_tuple }
                                   ^^^^^^
  ```

- Error: `workflows/zippypretext.nf:33:42`: `sample` is already declared

  ```nextflow
      hicmap.combine(sample).map { hicmap, sample -> tuple ( [ id: sample], hicmap)}.set { hicmap_tuple }
                                           ^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/juicerc.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args     ?: ''
          ^^^^
  ```

- Warning: `modules/local/make_header.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args     ?: ''
          ^^^^
  ```

- Warning: `modules/local/make_pairs.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args     ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_zippypretext_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_zippypretext_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_zippypretext_pipeline/main.nf:74:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      input     = Channel.fromPath(
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_zippypretext_pipeline/main.nf:82:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      agp        = Channel.fromPath(
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_zippypretext_pipeline/main.nf:88:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      idxfile    = Channel.fromPath(
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_zippypretext_pipeline/main.nf:94:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      hicmap    = Channel.fromPath(
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/zippypretext_map/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/zippypretext_map/main.nf:33:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      PRETEXT_TO_ASM.out.correctedagp.map{ agpid, agp -> agp}.set{agp}
                                           ^^^^^
  ```

- Warning: `subworkflows/local/zippypretext_map/main.nf:45:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map{ outlog, fa_id, fa ->
                                       ^^
  ```

- Warning: `subworkflows/local/zippypretext_map/main.nf:60:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      MAKE_HEADER.out.header.map{ header_id, header -> header}.set{ch_header}
                                  ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/zippypretext.nf:30:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```
