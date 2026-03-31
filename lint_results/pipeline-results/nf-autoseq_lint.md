# Nextflow lint results

- Generated: 2026-03-31T07:43:08.522580319Z
- Nextflow version: 26.03.1-edge
- Summary: 31 warnings

## :warning: Warnings

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                               ^^
    ```

- Warning: `modules/nf-core/cat/fastq/main.nf:58:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                               ^^
    ```

- Warning: `modules/nf-core/fgbio/fastqtobam/main.nf:58:9`: Variable was declared but not used

    ```nextflow
        def args = task.ext.args ?: ''
            ^^^^
    ```

- Warning: `modules/nf-core/fgbio/zipperbams/main.nf:25:9`: Variable was declared but not used

    ```nextflow
        def args2 = task.ext.args2 ?: ''
            ^^^^^
    ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:29:117`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def orientationbias_command = orientationbias ? orientationbias.collect { "--orientation-bias-artifact-priors ${it}" }.join(' ') : ''
                                                                                                                        ^^
    ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:30:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def segmentation_command = segmentation ? segmentation.collect { "--tumor-segmentation ${it}" }.join(' ') : ''
                                                                                                 ^^
    ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:32:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def table_command = table ? table.collect { "--contamination-table ${it}" }.join(' ') : ''
                                                                             ^^
    ```

- Warning: `modules/nf-core/gatk4/learnreadorientationmodel/main.nf:23:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def input_list = f1r2.collect { "--input ${it}" }.join(' ')
                                                   ^^
    ```

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:33:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def input_list = bam.collect { "--INPUT ${it}" }.join(' ')
                                                  ^^
    ```

- Warning: `modules/nf-core/gatk4/mutect2/main.nf:33:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def inputs = input.collect { "--input ${it}" }.join(" ")
                                                ^^
    ```

- Warning: `modules/nf-core/vt/normalize/main.nf:53:9`: Variable was declared but not used

    ```nextflow
        def args = task.ext.args ?: ''
            ^^^^
    ```

- Warning: `subworkflows/local/bam_qc_picard_samtools/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        ch_versions = Channel.empty()
                      ^^^^^^^
    ```

- Warning: `subworkflows/local/bam_qc_picard_samtools/main.nf:33:32`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
            .map { meta, bam, bai, meta2, interval_list ->
                                   ^^^^^
    ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:33:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        versions = Channel.empty()
                   ^^^^^^^
    ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:74:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
            ch_sage_pon.collect{it[1]},
                                ^^
    ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:75:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
            ch_sage_known_hotspots_somatic.collect{it[1]},
                                                   ^^
    ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:76:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
            ch_sage_highconf_regions.collect{it[1]},
                                             ^^
    ```

- Warning: `subworkflows/local/call_somatic_snvs/main.nf:77:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
            ch_ensembl_data_resources.collect{it[1]},
                                              ^^
    ```

- Warning: `subworkflows/local/fastq_align_bwamem2/main.nf:18:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        ch_versions  = Channel.empty()
                       ^^^^^^^
    ```

- Warning: `subworkflows/local/fastq_align_bwamem2/main.nf:67:22`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
            .map { meta, bam ->
                         ^^^
    ```

- Warning: `subworkflows/local/fastq_align_bwamem2/main.nf:85:16`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
            .map { id, meta, bam ->
                   ^^
    ```

- Warning: `subworkflows/local/fastq_align_bwamem2/main.nf:92:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
            ch_genome_fasta.collect{it[1]},
                                    ^^
    ```

- Warning: `subworkflows/local/fastq_align_bwamem2/main.nf:93:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
            ch_genome_fai.collect{it[1]}
                                  ^^
    ```

- Warning: `subworkflows/local/utils_nfcore_autoseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
        monochrome_logs   // boolean: Do not use coloured log outputs
        ^^^^^^^^^^^^^^^
    ```

- Warning: `subworkflows/local/utils_nfcore_autoseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
        input             //  string: Path to input samplesheet
        ^^^^^
    ```

- Warning: `subworkflows/local/utils_nfcore_autoseq_pipeline/main.nf:104:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        input_samples =  Channel
                         ^^^^^^^
    ```

- Warning: `subworkflows/local/utils_nfcore_autoseq_pipeline/main.nf:114:21`: Variable was declared but not used

    ```nextflow
                    def readgroup = "${meta.case_id}_${meta.sample_name}_${meta.lane}".toString()
                        ^^^^^^^^^
    ```

- Warning: `subworkflows/nf-core/bam_tumor_normal_somatic_variant_calling_gatk/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        versions = Channel.empty()
                   ^^^^^^^
    ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:39:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        ch_versions = Channel.empty()
                      ^^^^^^^
    ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:58:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        aligned_bam = Channel.empty()
                      ^^^^^^^
    ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:108:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        consensus_bam = Channel.empty()
                        ^^^^^^^
    ```
