# Nextflow lint results

- Generated: 2026-07-29T00:26:31.254921744Z
- Nextflow version: 26.07.0-edge
- Summary: 98 warnings

## :warning: Warnings

- Warning: `modules/local/drop/drop_sample_annot/main.nf:25:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sex_drop = sex.collect { it.replace("1","M").replace("2","F").replace("0","NA").replace("other","NA") }.join(' ')
                                   ^^
  ```

- Warning: `modules/local/drop/drop_sample_annot/main.nf:30:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def dna_vcf_clean = vcf.collect { it.toString() == "" || it.toString().trim() == "" ? "NA" : it }.join(' ')
                                        ^^
  ```

- Warning: `modules/local/drop/drop_sample_annot/main.nf:30:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def dna_vcf_clean = vcf.collect { it.toString() == "" || it.toString().trim() == "" ? "NA" : it }.join(' ')
                                                               ^^
  ```

- Warning: `modules/local/drop/drop_sample_annot/main.nf:30:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def dna_vcf_clean = vcf.collect { it.toString() == "" || it.toString().trim() == "" ? "NA" : it }.join(' ')
                                                                                                   ^^
  ```

- Warning: `modules/nf-core/bcftools/merge/main.nf:28:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = (vcfs.collect().size() > 1) ? vcfs.sort{ it.name } : vcfs
                                                           ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:56:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          if (['--write-index=tbi', '-W=tbi'].any { args.contains(it) }  && extension == 'vcf.gz') {
                                                                  ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:58:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          } else if (['--write-index=tbi', '-W=tbi', '--write-index=csi', '-W=csi', '--write-index', '-W'].any { args.contains(it) }) {
                                                                                                                               ^^
  ```

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

- Warning: `modules/nf-core/gawk/main.nf:26:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix    = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}" // use the first extension of the input files
                                                       ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                      ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                                                         ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:31:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_cmd  = input.collect { it.toString() - ~/\.gz$/ }.join(" ")
                                   ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:34:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      cleanup    = lst_gz ? "rm ${lst_gz.collect{ it - ~/\.gz$/ }.join(" ")}" : ""
                                                  ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${suffix}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:26:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:30:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def args_sorted = args.replaceAll(/(.*)(-[wxy])(.*)/) { all, pre, param, post -> "$pre $post $param" }.trim()
                                                              ^^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:49:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/salmon/quant/main.nf:35:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each { reads1 << it } : reads.eachWithIndex { v, ix -> (ix & 1 ? reads2 : reads1) << v }
                                                           ^^
  ```

- Warning: `modules/nf-core/star/align/main.nf:46:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:32:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:37:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_inputs_branched = ch_all_inputs.branch { meta, files ->
                                                        ^^^^^
  ```

- Warning: `subworkflows/local/alignment/main.nf:99:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_cram_crai = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/allele_specific_calling/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/allele_specific_calling/main.nf:59:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect{it[1]}
                   ^^
  ```

- Warning: `subworkflows/local/allele_specific_calling/main.nf:65:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect{it[2]}
                   ^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:41:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:48:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it.sort { a, b -> a[0] <=> b[0] } } // Sort on ID
                 ^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:49:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it.transpose() }
                 ^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:60:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, bai ->
                          ^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:60:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, bai ->
                               ^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:63:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bam, bai ->
                       ^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:63:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bam, bai ->
                            ^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:137:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              : Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:139:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              : Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:141:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              : Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:187:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:190:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:193:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:196:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:199:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:202:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:205:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:208:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:211:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:214:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:217:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:220:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:223:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/analyse_transcripts/main.nf:226:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/annotate_snv/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/annotate_snv/main.nf:74:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_vcf_clin = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_qc/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:25:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_vcf = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:26:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tbi = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:27:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_stats = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants_gatk/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:27:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_downloaded_fasta = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:28:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_downloaded_gtf = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:29:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_built_vep_cache = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:30:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_built_vep_plugin_file = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:31:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_high_q_vcf_tbi = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:58:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          WGET_DOWNLOAD(ch_vep_refs_download.filter{ it != null })
                                                     ^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:68:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_input_hg38 = Channel.of( tuple('qc_vcf_1000G_hg38.vcf.gz', 'https://www.cmm.in.tum.de/public/paper/drop_analysis/resource/qc_vcf_1000G_hg38.vcf.gz') )
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:69:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_input_hg38_tbi = Channel.of( tuple('qc_vcf_1000G_hg38.vcf.gz.tbi', 'https://www.cmm.in.tum.de/public/paper/drop_analysis/resource/qc_vcf_1000G_hg38.vcf.gz.tbi') )
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:73:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_input_hg19 = Channel.of( tuple('qc_vcf_1000G_hg19.vcf.gz', 'https://www.cmm.in.tum.de/public/paper/drop_analysis/resource/qc_vcf_1000G_hg19.vcf.gz') )
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/download_references/main.nf:74:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_input_hg19_tbi = Channel.of( tuple('qc_vcf_1000G_hg19.vcf.gz.tbi', 'https://www.cmm.in.tum.de/public/paper/drop_analysis/resource/qc_vcf_1000G_hg19.vcf.gz.tbi') )
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/igv_tracks/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_references/main.nf:195:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (ch.flatten().count().map{it == (1)}) {
                                   ^^
  ```

- Warning: `subworkflows/local/prepare_references/main.nf:202:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      } else if (ch.flatten().count().map{it == (2)}) {
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:71:143`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          after_text = """${workflow.manifest.doi ? "* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { " https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:112:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:159:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `workflows/tomte.nf:45:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      outdir
      ^^^^^^
  ```

- Warning: `workflows/tomte.nf:54:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_case_info      = ch_samples.toList().map { create_case_channel(it) }
                                                                        ^^
  ```

- Warning: `workflows/tomte.nf:111:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          row.vep_files.split(',').collect { file(it.trim()) }
                                                  ^^
  ```

- Warning: `workflows/tomte.nf:153:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq: it[1].any { it.toString().endsWith('.fastq.gz') || it.toString().endsWith('.fq.gz') }
                     ^^
  ```

- Warning: `workflows/tomte.nf:153:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq: it[1].any { it.toString().endsWith('.fastq.gz') || it.toString().endsWith('.fq.gz') }
                                 ^^
  ```

- Warning: `workflows/tomte.nf:153:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq: it[1].any { it.toString().endsWith('.fastq.gz') || it.toString().endsWith('.fq.gz') }
                                                                        ^^
  ```

- Warning: `workflows/tomte.nf:154:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              cram:  it[1].any { it.toString().endsWith('.cram') }
                     ^^
  ```

- Warning: `workflows/tomte.nf:154:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              cram:  it[1].any { it.toString().endsWith('.cram') }
                                 ^^
  ```

- Warning: `workflows/tomte.nf:155:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam:   it[1].any { it.toString().endsWith('.bam') }
                     ^^
  ```

- Warning: `workflows/tomte.nf:155:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam:   it[1].any { it.toString().endsWith('.bam') }
                                 ^^
  ```

- Warning: `workflows/tomte.nf:170:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/tomte.nf:259:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(ANNOTATE_SNV.out.report.collect{it[1]}.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/tomte.nf:262:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(CALL_VARIANTS.out.stats.collect{it[1]}.ifEmpty([]))
                                                                                  ^^
  ```

- Warning: `workflows/tomte.nf:337:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]}.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/tomte.nf:338:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.fastp_report.collect{it[1]}.ifEmpty([]))
                                                                                                      ^^
  ```

- Warning: `workflows/tomte.nf:339:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.star_log_final.collect{it[1]}.ifEmpty([]))
                                                                                                        ^^
  ```

- Warning: `workflows/tomte.nf:340:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.gene_counts.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/tomte.nf:341:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.salmon_info.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/tomte.nf:342:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(BAM_QC.out.metrics_general_rna.collect{it[1]}.ifEmpty([]))
                                                                                                          ^^
  ```

- Warning: `workflows/tomte.nf:343:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(BAM_QC.out.metrics_insert_size.collect{it[1]}.ifEmpty([]))
                                                                                                          ^^
  ```

- Warning: `workflows/tomte.nf:344:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ANALYSE_TRANSCRIPTS.out.stats_gtf.collect{it[1]}.ifEmpty([]))
                                                                                                             ^^
  ```
