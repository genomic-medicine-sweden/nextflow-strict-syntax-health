# Nextflow lint results

- Generated: 2026-03-31T12:57:03.985010198Z
- Nextflow version: 26.03.1-edge
- Summary: 8 errors, 149 warnings

## :x: Errors

- Error: `modules/local/drop/drop_config_runMAE/main.nf:8:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(dict)
                ^^^^
  ```

- Error: `nextflow.config:323:34`: `manifest` is not defined

  ```nextflow
          command = "nextflow run $manifest.name -profile <docker/singularity/.../institute> --input samplesheet.csv --outdir <OUTDIR>"
                                   ^^^^^^^^
  ```

- Error: `nextflow.config:338:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { " https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:338:67`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { " https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                    ^^^^^^^^
  ```

- Error: `nextflow.config:338:181`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { " https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:342:26`: `manifest` is not defined

  ```nextflow
      https://github.com/${manifest.name}/blob/master/CITATIONS.md
                           ^^^^^^^^
  ```

- Error: `nextflow.config:348:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:349:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/drop/drop_config_runMAE/main.nf:6:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(fasta), path(fai)
                ^^^^
  ```

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

- Warning: `nextflow.config:338:124`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { " https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
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

- Warning: `subworkflows/local/prepare_references/main.nf:45:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_references/main.nf:190:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (ch.flatten().count().map{it == (1)}) {
                                   ^^
  ```

- Warning: `subworkflows/local/prepare_references/main.nf:197:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      } else if (ch.flatten().count().map{it == (2)}) {
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tomte_pipeline/main.nf:122:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:44:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:45:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:49:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_case_info      = ch_samples.toList().map { create_case_channel(it) }
                                                                        ^^
  ```

- Warning: `workflows/tomte.nf:50:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_platform       = Channel.from(params.platform).collect()
                          ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:53:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_vep_refs_download_unprocessed = params.vep_refs_download         ? Channel.fromPath(params.vep_refs_download)
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:54:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:70:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta                      = params.fasta                        ? Channel.fromPath(params.fasta).map {it -> [[id:it.getSimpleName()], it]}.collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:72:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf                        = params.gtf                          ? Channel.fromPath(params.gtf).map {it -> [[id:it.getSimpleName()], it]}.collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:74:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_drop_mae_high_q_vcf_tbi    = params.drop_mae_high_q_vcf          ? Channel.fromPath(params.drop_mae_high_q_vcf).concat(Channel.fromPath(params.drop_mae_high_q_vcf_tbi)).collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:74:127`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_drop_mae_high_q_vcf_tbi    = params.drop_mae_high_q_vcf          ? Channel.fromPath(params.drop_mae_high_q_vcf).concat(Channel.fromPath(params.drop_mae_high_q_vcf_tbi)).collect()
                                                                                                                                ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:76:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_vep_cache_unprocessed      = params.vep_cache                    ? Channel.fromPath(params.vep_cache)
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:77:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty().mix(downloads.vep_cache)
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:78:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_vep_extra_files_unsplit    = params.vep_plugin_files             ? Channel.fromPath(params.vep_plugin_files)
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:79:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty().mix(downloads.vep_plugin)
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:80:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fai                        = params.fai                          ? Channel.fromPath(params.fai).map {it -> [[id:it.getSimpleName()], it]}.collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:81:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:82:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_panel_clinical_filter = params.gene_panel_clinical_filter   ? Channel.fromPath(params.gene_panel_clinical_filter).collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:83:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:84:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ref_drop_annot_file        = params.reference_drop_annot_file    ? Channel.fromPath(params.reference_drop_annot_file).collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:85:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:86:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ref_drop_count_file        = params.reference_drop_count_file    ? Channel.fromPath(params.reference_drop_count_file).collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:87:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:88:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ref_drop_splice_folder     = params.reference_drop_splice_folder ? Channel.fromPath(params.reference_drop_splice_folder).collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:89:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:90:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_salmon_index               = params.salmon_index                 ? Channel.fromPath(params.salmon_index)
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:91:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:92:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index                 = params.star_index                   ? Channel.fromPath(params.star_index).map {it -> [[id:it.getSimpleName()], it]}.collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:93:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:94:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcript_fasta           = params.transcript_fasta             ? Channel.fromPath(params.transcript_fasta)
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:95:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:96:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sequence_dict              = params.sequence_dict                ? Channel.fromPath(params.sequence_dict).map{ it -> [[id:it.getSimpleName()], it] }.collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:97:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:98:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_subsample_bed              = params.subsample_bed                ? Channel.fromPath(params.subsample_bed).collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:99:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:100:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hb_genes                   = params.hb_genes                     ? Channel.fromPath(params.hb_genes).collect()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:101:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                                                          : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:106:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          row.vep_files.split(',').collect { file(it.trim()) }
                                                  ^^
  ```

- Warning: `workflows/tomte.nf:148:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq: it[1].any { it.toString().endsWith('.fastq.gz') || it.toString().endsWith('.fq.gz') }
                     ^^
  ```

- Warning: `workflows/tomte.nf:148:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq: it[1].any { it.toString().endsWith('.fastq.gz') || it.toString().endsWith('.fq.gz') }
                                 ^^
  ```

- Warning: `workflows/tomte.nf:148:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq: it[1].any { it.toString().endsWith('.fastq.gz') || it.toString().endsWith('.fq.gz') }
                                                                        ^^
  ```

- Warning: `workflows/tomte.nf:149:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              cram:  it[1].any { it.toString().endsWith('.cram') }
                     ^^
  ```

- Warning: `workflows/tomte.nf:149:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              cram:  it[1].any { it.toString().endsWith('.cram') }
                                 ^^
  ```

- Warning: `workflows/tomte.nf:150:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam:   it[1].any { it.toString().endsWith('.bam') }
                     ^^
  ```

- Warning: `workflows/tomte.nf:150:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam:   it[1].any { it.toString().endsWith('.bam') }
                                 ^^
  ```

- Warning: `workflows/tomte.nf:165:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/tomte.nf:255:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(ANNOTATE_SNV.out.report.collect{it[1]}.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/tomte.nf:258:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(CALL_VARIANTS.out.stats.collect{it[1]}.ifEmpty([]))
                                                                                  ^^
  ```

- Warning: `workflows/tomte.nf:260:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_vcf_tbi = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:273:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_junction_bed = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:274:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bigwig = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:287:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_pedfile = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:295:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_hb_estimates = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:318:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                              ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:319:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config                     = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                              ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:320:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                      ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:320:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:321:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:321:128`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                                                 ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:323:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                              ^^^^^^^
  ```

- Warning: `workflows/tomte.nf:327:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]}.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/tomte.nf:328:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.fastp_report.collect{it[1]}.ifEmpty([]))
                                                                                                      ^^
  ```

- Warning: `workflows/tomte.nf:329:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.star_log_final.collect{it[1]}.ifEmpty([]))
                                                                                                        ^^
  ```

- Warning: `workflows/tomte.nf:330:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.gene_counts.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/tomte.nf:331:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ALIGNMENT.out.salmon_info.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/tomte.nf:332:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(BAM_QC.out.metrics_general_rna.collect{it[1]}.ifEmpty([]))
                                                                                                          ^^
  ```

- Warning: `workflows/tomte.nf:333:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(BAM_QC.out.metrics_insert_size.collect{it[1]}.ifEmpty([]))
                                                                                                          ^^
  ```

- Warning: `workflows/tomte.nf:334:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files                      = ch_multiqc_files.mix(ANALYSE_TRANSCRIPTS.out.stats_gtf.collect{it[1]}.ifEmpty([]))
                                                                                                             ^^
  ```
