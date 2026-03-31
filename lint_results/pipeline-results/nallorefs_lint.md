# Nextflow lint results

- Generated: 2026-03-31T07:43:30.388584670Z
- Nextflow version: 26.03.1-edge
- Summary: 1 error, 31 warnings

## :x: Errors

- Error: `modules/nf-core/bcftools/view/main.nf:60:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index=tbi") || args.contains("-W=tbi") ? "tbi" :
          ^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/cadd2vcf.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cadd2vcf.nf:62:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/downloadgnomad.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/echtvar/encode/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/extract_header_dbnsfp.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/gunzip_remove_header_sort_dbnsfp.nf:66:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/clinvar/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gnomad_snvs/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/gnomad_snvs/main.nf:59:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.from(gnomad_checksums.collect { key, value -> [ ['id': key ], value ] } )
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nallorefs_pipeline/main.nf:29:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nallorefs_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nallorefs_pipeline/main.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nallorefs_pipeline/main.nf:68:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nallorefs_pipeline/main.nf:102:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      outdir          //    path: Path to output directory where results will be published
      ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nallorefs_pipeline/main.nf:106:5`: Variable was declared but not used

  ```nextflow
      summary_params = paramsSummaryMap(workflow, parameters_schema: "nextflow_schema.json")
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:52:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_samplesheet // channel: mock samplesheet read in from --input
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:108:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gnomad_snvs_per_chr = Channel.fromList(chromosomes)
                               ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:119:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_echtvar_local_databases = params.local_echtvar_databases ? Channel.fromList(samplesheetToList(params.local_echtvar_databases, 'assets/schema_local_echtvar_databases.json'))
                                                                    ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:121:64`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              [ meta + [ 'id': file(vcf).name ], vcf, json ] } : Channel.empty()
                                                                 ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:128:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                  = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:129:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_general_files_to_download = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:130:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_echtvar_encode_files      = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:222:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_echtvar_encode_files.map { meta, vcf, json -> [ meta, vcf ] },
                                                       ^^^^
  ```

- Warning: `workflows/nallorefs.nf:257:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter { meta, file ->
                            ^^^^
  ```

- Warning: `workflows/nallorefs.nf:266:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter { meta, file ->
                            ^^^^
  ```

- Warning: `workflows/nallorefs.nf:425:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.of(path)
      ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:430:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromPath(path)
      ^^^^^^^
  ```

- Warning: `workflows/nallorefs.nf:436:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.of(path)
      ^^^^^^^
  ```
