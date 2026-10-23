# Nextflow lint results

- Generated: 2026-10-23T00:18:17.012443696Z
- Nextflow version: 26.10.3
- Summary: 4 errors, 34 warnings

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

- Warning: `conf/modules.config:94:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it }.join(' ').trim() } // Remove empty strings and join arguments
                      ^^
  ```

- Warning: `modules/local/assignment_heatmap/main.nf:28:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/local/ctrl_comparison/main.nf:30:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/local/emu/abundance/main.nf:45:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/local/emu/combine_outputs/main.nf:43:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/local/translate_taxids/main.nf:30:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:17:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:18:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/cutadapt/main.nf:18:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:18:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/filtlong/main.nf:18:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/krona/ktimporttaxonomy/main.nf:19:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/multiqc/main.nf:23:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/nanoplot/main.nf:19:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/porechop/abi/main.nf:19:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/porechop/abi/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def adapters_list = custom_adapters ? "--custom_adapters ${custom_adapters}" : ""
          ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/seqtk/sample/main.nf:17:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs         // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:75:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      checkPathParamList.findAll { it }.each { path ->
                                   ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:87:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:94:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_trana_pipeline/main.nf:122:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { validateInputSamplesheet( it ) }
                                               ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/trana.nf:52:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]}.ifEmpty([]))
                                                                     ^^
  ```

- Warning: `workflows/trana.nf:61:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              NANOPLOT_UNPROCESSED_READS.out.txt.collect{ it[1] }
                                                          ^^
  ```

- Warning: `workflows/trana.nf:75:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PORECHOP_ABI.out.log.collect{ it[1] }
                                                ^^
  ```

- Warning: `workflows/trana.nf:99:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  FILTLONG.out.log.collect{ it[1] }
                                            ^^
  ```

- Warning: `workflows/trana.nf:113:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  CUTADAPT.out.log.collect{ it[1] }
                                            ^^
  ```

- Warning: `workflows/trana.nf:136:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          NANOPLOT_PROCESSED_READS.out.txt.collect{ it[1] }
                                                    ^^
  ```

- Warning: `workflows/trana.nf:171:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }  // Extract only the file path from the tuple (meta, path)
                 ^^
  ```

- Warning: `workflows/trana.nf:187:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, path -> path }
                     ^^^^
  ```

- Warning: `workflows/trana.nf:244:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, reads -> meta
                    ^^^^^
  ```

- Warning: `workflows/trana.nf:250:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, reads -> meta.id
                    ^^^^^
  ```

- Warning: `workflows/trana.nf:259:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, assignment_heatmap -> [ meta, file(outdir).toAbsolutePath().toString() ]
                    ^^^^^^^^^^^^^^^^^^
  ```
