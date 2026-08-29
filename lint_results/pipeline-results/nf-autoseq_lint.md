# Nextflow lint results

- Generated: 2026-08-29T00:16:49.977119921Z
- Nextflow version: 26.08.0-edge
- Summary: 18 warnings

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:33:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect { "--INPUT ${it}" }.join(' ')
                                                ^^
  ```

- Warning: `modules/nf-core/gridss/call/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gridss/preprocess/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/gridss/preprocess/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/vt/normalize/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:18:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions  = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:67:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bam ->
                       ^^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:85:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { id, meta, bam ->
                 ^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:92:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_genome_fasta.collect{it[1]},
                                  ^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:93:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_genome_fai.collect{it[1]}
                                ^^
  ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:33:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:81:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_sage_pon.collect{it[1]},
                              ^^
  ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:82:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_sage_known_hotspots_somatic.collect{it[1]},
                                                 ^^
  ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:83:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_sage_highconf_regions.collect{it[1]},
                                           ^^
  ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:84:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_ensembl_data_resources.collect{it[1]},
                                            ^^
  ```

- Warning: `subworkflows/local/qc_alignment/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_alignment/main.nf:33:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bam, bai, meta2, interval_list ->
                                 ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_autoseq_pipeline/main.nf:104:21`: Variable was declared but not used

  ```nextflow
                  def readgroup = "${meta.case_id}_${meta.sample_name}_${meta.lane}".toString()
                      ^^^^^^^^^
  ```
