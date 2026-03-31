# Nextflow lint results

- Generated: 2026-03-31T07:42:57.761858524Z
- Nextflow version: 26.03.1-edge
- Summary: 4 errors, 16 warnings

## :x: Errors

- Error: `conf/SGE__NGP_trana_resource_20250325.config:41:18`: `workDir` is not defined

  ```nextflow
      workDir = "${workDir}"
                   ^^^^^^^
  ```

- Error: `conf/SGE__NGP_trana_resource_20250325.config:42:19`: `workDir` is not defined

  ```nextflow
      cacheDir = "${workDir}"
                    ^^^^^^^
  ```

- Error: `conf/SGE__NGP_trana_resource_20250325.config:56:23`: `workDir` is not defined

  ```nextflow
          cacheDir = "${workDir}/"
                        ^^^^^^^
  ```

- Error: `conf/SGE__NGP_trana_resource_20250325.config:66:23`: `workDir` is not defined

  ```nextflow
          cacheDir = "${workDir}/"
                        ^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:113:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it }.join(' ').trim() } // Remove empty strings and join arguments
                      ^^
  ```

- Warning: `modules/nf-core/porechop/abi/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def adapters_list = custom_adapters ? "--custom_adapters ${custom_adapters}" : ""
          ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:37:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs         // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:77:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      checkPathParamList.findAll { it }.each { path ->
                                   ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:119:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { validateInputSamplesheet( it ) }
                                           ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/trana.nf:53:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]}.ifEmpty([]))
                                                                     ^^
  ```

- Warning: `workflows/trana.nf:62:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              NANOPLOT_UNPROCESSED_READS.out.txt.collect{ it[1] }
                                                          ^^
  ```

- Warning: `workflows/trana.nf:76:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PORECHOP_ABI.out.log.collect{ it[1] }
                                                ^^
  ```

- Warning: `workflows/trana.nf:100:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  FILTLONG.out.log.collect{ it[1] }
                                            ^^
  ```

- Warning: `workflows/trana.nf:114:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  CUTADAPT.out.log.collect{ it[1] }
                                            ^^
  ```

- Warning: `workflows/trana.nf:137:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          NANOPLOT_PROCESSED_READS.out.txt.collect{ it[1] }
                                                    ^^
  ```

- Warning: `workflows/trana.nf:166:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }  // Extract only the file path from the tuple (meta, path)
                 ^^
  ```

- Warning: `workflows/trana.nf:182:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, path -> path }
                     ^^^^
  ```

- Warning: `workflows/trana.nf:239:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, reads -> meta
                    ^^^^^
  ```

- Warning: `workflows/trana.nf:248:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, assignment_heatmap -> [ meta, file(outdir).toAbsolutePath().toString() ]
                    ^^^^^^^^^^^^^^^^^^
  ```
