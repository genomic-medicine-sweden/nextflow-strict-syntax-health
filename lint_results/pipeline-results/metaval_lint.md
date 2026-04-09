# Nextflow lint results

- Generated: 2026-04-09T00:18:22.213448980Z
- Nextflow version: 26.03.2-edge
- Summary: 35 errors, 113 warnings

## :x: Errors

- Error: `modules/local/rm_empty_bam/main.nf:13:10`: `folder` is not defined

  ```nextflow
      path folder, optional: true
           ^^^^^^
  ```

- Error: `modules/nf-core/diamond/blastx/main.nf:37:30`: Unexpected input: '='

  ```nextflow
          case "blast": outfmt = 0; break
                               ^
  ```

- Error: `modules/nf-core/igvreports/main.nf:24:9`: `fasta` is already declared

  ```nextflow
      def fasta = fasta ? "--fasta ${fasta}" : ""
          ^^^^^
  ```

- Error: `modules/nf-core/krakentools/extractkrakenreads/main.nf:14:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(classified_reads_fastq)
                ^^^^
  ```

- Error: `modules/nf-core/krakentools/extractkrakenreads/main.nf:15:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(report)
                ^^^^
  ```

- Error: `subworkflows/local/blast.nf:8:1`: Module could not be parsed: '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/metaval/modules/nf-core/diamond/blastx/main.nf'

  ```nextflow
  include { DIAMOND_BLASTX                                        } from '../../modules/nf-core/diamond/blastx/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/blast.nf:73:9`: `DIAMOND_BLASTX` is not defined

  ```nextflow
          DIAMOND_BLASTX (
          ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/blast.nf:79:40`: `DIAMOND_BLASTX` is not defined

  ```nextflow
          ch_versions = ch_versions.mix( DIAMOND_BLASTX.out.versions.first() )
                                         ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/blast.nf:82:26`: `DIAMOND_BLASTX` is not defined

  ```nextflow
          ch_blastx_hits = DIAMOND_BLASTX.out.txt.filter { meta, blastx_hits -> blastx_hits.size() > 0 }
                           ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/consensus.nf:42:97`: `bam` is already declared

  ```nextflow
              input_medaka  = ch_bam.longreads.combine( Channel.value(reference) ).map{ meta_bam, bam, meta_ref, ref -> [ meta_bam, bam, ref ]}
                                                                                                  ^^^
  ```

- Error: `subworkflows/local/fetch_blast_genomes.nf:32:20`: `blast_taxid` is already declared

  ```nextflow
              .map { blast_taxid, meta, available_taxids ->
                     ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fetch_blast_genomes.nf:41:23`: `blast_taxid` is already declared

  ```nextflow
              .filter { blast_taxid, meta, genome_taxid, organism, genome -> blast_taxid == genome_taxid } // Filter to keep only matching taxids
                        ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fetch_blast_genomes.nf:42:20`: `blast_taxid` is already declared

  ```nextflow
              .map { blast_taxid, meta, genome_taxid, organism, genome -> [blast_taxid, meta, organism, genome] }
                     ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fetch_blast_genomes.nf:49:16`: `blast_taxid` is already declared

  ```nextflow
          .map { blast_taxid, meta, organism, genome ->
                 ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fetch_blast_genomes.nf:56:29`: `blast_taxid` is already declared

  ```nextflow
          .map { meta_joined, blast_taxid, meta1, organism, genome, meta2, reads ->
                              ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:71:55`: `bam` is already declared

  ```nextflow
          .map { meta, accession_list, taxid, organism, bam, bam_index ->
                                                        ^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:77:19`: `bam` is already declared

  ```nextflow
              meta, bam, bam_index, accession_list ->
                    ^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:96:25`: `bam` is already declared

  ```nextflow
          .filter { meta, bam, mapped, pass -> pass }
                          ^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:97:22`: `bam` is already declared

  ```nextflow
          .map { meta, bam, mapped, pass -> [meta, bam] }
                       ^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:100:25`: `bai` is already declared

  ```nextflow
          .filter { meta, bai, mapped, pass -> pass }
                          ^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:101:22`: `bai` is already declared

  ```nextflow
          .map { meta, bai, mapped, pass -> [meta, bai] }
                       ^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:106:55`: `bam` is already declared

  ```nextflow
          .map { meta, accession_list, taxid, organism, bam, bam_index ->
                                                        ^^^
  ```

- Error: `subworkflows/local/taxid_bam_fasta.nf:112:19`: `bam` is already declared

  ```nextflow
              meta, bam, bam_index, accession_list ->
                    ^^^
  ```

- Error: `subworkflows/local/taxid_reads.nf:12:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow TAXID_READS {
  ^
  ```

- Error: `workflows/metaval.nf:8:1`: Included name 'TAXID_READS' is not defined in module '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/metaval/subworkflows/local/taxid_reads.nf'

  ```nextflow
  include { TAXID_READS                                           } from '../subworkflows/local/taxid_reads'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaval.nf:44:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def checkPathParamList = [ params.input, params.pathogens_genomes,
  ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaval.nf:50:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/metaval.nf:50:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaval.nf:50:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/metaval.nf:50:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/metaval.nf:50:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/metaval.nf:53:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if ( params.input ) {
  ^
  ```

- Error: `workflows/metaval.nf:111:9`: `TAXID_READS` is not defined

  ```nextflow
          TAXID_READS (
          ^^^^^^^^^^^
  ```

- Error: `workflows/metaval.nf:122:51`: `TAXID_READS` is not defined

  ```nextflow
          ch_versions            = ch_versions.mix( TAXID_READS.out.versions )
                                                    ^^^^^^^^^^^
  ```

- Error: `workflows/metaval.nf:125:26`: `TAXID_READS` is not defined

  ```nextflow
          ch_taxid_reads = TAXID_READS.out.reads
                           ^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/filter_consensus/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/rm_empty_bam/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/blast/blastn/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/igvreports/main.nf:26:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def track_arg = tracks ? "--tracks "+ tracks.collect { it.toString() }.join(' ') : ""
                                                             ^^
  ```

- Warning: `modules/nf-core/igvreports/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/krakentools/extractkrakenreads/main.nf:13:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(classified_reads_assignment)
                ^^^^
  ```

- Warning: `modules/nf-core/krakentools/extractkrakenreads/main.nf:14:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(classified_reads_fastq)
                ^^^^
  ```

- Warning: `modules/nf-core/krakentools/extractkrakenreads/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def input_reads_command = meta.single_end ? "-s $classified_reads_fastq" : "-s1 ${classified_reads_fastq[0]} -s2 ${classified_reads_fastq[1]}"
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/krakentools/extractkrakenreads/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def output_reads_command = meta.single_end ? "-o ${prefix}.extracted_kraken2_read.${extension}" : "-o ${prefix}.extracted_kraken2_read_1.${extension} -o2 ${prefix}.extracted_kraken2_read_2.${extension}"
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/krakentools/extractkrakenreads/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def report_option = report ? "-r ${report}" : ""
          ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/pigz/uncompress/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:78:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:80:9`: Variable was declared but not used

  ```nextflow
      def maxmem = task.memory.toGiga()
          ^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:84:9`: Variable was declared but not used

  ```nextflow
      def custom_hmms = hmm ? "--custom-hmms $hmm" : ""
          ^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:85:9`: Variable was declared but not used

  ```nextflow
      def reads = yml ? "--dataset $yml" : "$illumina_reads $pacbio_reads $nanopore_reads"
          ^^^^^
  ```

- Warning: `subworkflows/local/blast.nf:44:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_blastn_hits = BLAST_BLASTN.out.txt.filter { meta, blastn_hits -> blastn_hits.size() >0 }
                                                         ^^^^
  ```

- Warning: `subworkflows/local/blast.nf:54:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .unique { staxid, meta, blastn_hits -> [staxid, meta.id, meta.taxid, meta.tool]}
                                      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/blast.nf:55:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { staxid, meta, blastn_hits -> [ staxid, meta ] }
                                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/blast.nf:82:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_blastx_hits = DIAMOND_BLASTX.out.txt.filter { meta, blastx_hits -> blastx_hits.size() > 0 }
                                                           ^^^^
  ```

- Warning: `subworkflows/local/blast.nf:92:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .unique { staxid, meta, blastx_hits -> [staxid, meta.id, meta.taxid, meta.tool]}
                                      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/blast.nf:93:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { staxid, meta, blastx_hits -> [ staxid, meta ] }
                                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/consensus.nf:42:55`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              input_medaka  = ch_bam.longreads.combine( Channel.value(reference) ).map{ meta_bam, bam, meta_ref, ref -> [ meta_bam, bam, ref ]}
                                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/consensus.nf:42:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              input_medaka  = ch_bam.longreads.combine( Channel.value(reference) ).map{ meta_bam, bam, meta_ref, ref -> [ meta_bam, bam, ref ]}
                                                                                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:13:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_taxid2genome = Channel.fromPath ( taxid2genome, checkIfExists: true )
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:26:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { taxid, organism, genome -> taxid }
                            ^^^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:26:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { taxid, organism, genome -> taxid }
                                      ^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:28:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it.toSet() }  // Stores all taxids in a Set, automatically removing any duplicates.
                     ^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:39:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it != null }
                        ^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:41:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { blast_taxid, meta, genome_taxid, organism, genome -> blast_taxid == genome_taxid } // Filter to keep only matching taxids
                                     ^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:41:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { blast_taxid, meta, genome_taxid, organism, genome -> blast_taxid == genome_taxid } // Filter to keep only matching taxids
                                                         ^^^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:41:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { blast_taxid, meta, genome_taxid, organism, genome -> blast_taxid == genome_taxid } // Filter to keep only matching taxids
                                                                   ^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:42:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { blast_taxid, meta, genome_taxid, organism, genome -> [blast_taxid, meta, organism, genome] }
                                        ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:56:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta_joined, blast_taxid, meta1, organism, genome, meta2, reads ->
                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fetch_blast_genomes.nf:56:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta_joined, blast_taxid, meta1, organism, genome, meta2, reads ->
                                           ^^^^^
  ```

- Warning: `subworkflows/local/igv.nf:20:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_bam_bai_reference.map { meta, bam, bai, ref -> [ meta, bam, "1" ] },
                                                ^^^
  ```

- Warning: `subworkflows/local/igv.nf:20:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_bam_bai_reference.map { meta, bam, bai, ref -> [ meta, bam, "1" ] },
                                                     ^^^
  ```

- Warning: `subworkflows/local/igv.nf:29:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_bam_bai_reference.map { meta, bam, bai, ref -> [ meta, ref ] }
                                           ^^^
  ```

- Warning: `subworkflows/local/igv.nf:29:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_bam_bai_reference.map { meta, bam, bai, ref -> [ meta, ref ] }
                                                ^^^
  ```

- Warning: `subworkflows/local/igv.nf:37:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bam_bai = ch_bam_bai_reference.map { meta, bam, bai, ref -> [ meta, bam, bai ] }
                                                              ^^^
  ```

- Warning: `subworkflows/local/igv.nf:50:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_igv_input.map { meta, bed, bam, bai, fasta, fai ->
                                                  ^^^^^
  ```

- Warning: `subworkflows/local/igv.nf:50:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_igv_input.map { meta, bed, bam, bai, fasta, fai ->
                                                         ^^^
  ```

- Warning: `subworkflows/local/igv.nf:53:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_igv_input.map { meta, bed, bam, bai, fasta, fai ->
                                   ^^^
  ```

- Warning: `subworkflows/local/igv.nf:53:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_igv_input.map { meta, bed, bam, bai, fasta, fai ->
                                        ^^^
  ```

- Warning: `subworkflows/local/igv.nf:53:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_igv_input.map { meta, bed, bam, bai, fasta, fai ->
                                             ^^^
  ```

- Warning: `subworkflows/local/mapping_longread.nf:24:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads, ref -> [ meta, ref ] }
                       ^^^^^
  ```

- Warning: `subworkflows/local/mapping_longread.nf:31:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_reads_reference.map { meta, reads, ref -> [ meta, ref ] }
                                         ^^^^^
  ```

- Warning: `subworkflows/local/mapping_longread.nf:45:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads, ref -> [ meta, reads ] }
                              ^^^
  ```

- Warning: `subworkflows/local/mapping_longread.nf:78:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { it -> file("${params.outdir}/mapping/minimap2/align") }
                     ^^
  ```

- Warning: `subworkflows/local/mapping_longread.nf:85:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { it -> file("${params.outdir}/pathogens/mapping/minimap2/align") }
                     ^^
  ```

- Warning: `subworkflows/local/mapping_longread.nf:90:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BAM_SORT_STATS_SAMTOOLS.out.flagstat.collect{it[1]}.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `subworkflows/local/mapping_shortread.nf:22:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_reads_reference.map { meta, reads, ref -> [ meta, ref ] }
                                         ^^^^^
  ```

- Warning: `subworkflows/local/mapping_shortread.nf:29:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_reads_reference.map { meta, reads, ref -> [ meta, ref ] }
                                         ^^^^^
  ```

- Warning: `subworkflows/local/mapping_shortread.nf:43:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads, ref -> [ meta, reads ] }
                              ^^^
  ```

- Warning: `subworkflows/local/mapping_shortread.nf:65:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { it -> file("${params.outdir}/mapping/bowtie2/align") }
                     ^^
  ```

- Warning: `subworkflows/local/mapping_shortread.nf:72:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { it -> file("${params.outdir}/pathogens/mapping/bowtie2/align") }
                     ^^
  ```

- Warning: `subworkflows/local/mapping_shortread.nf:77:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix ( FASTQ_ALIGN_BOWTIE2.out.flagstat.collect{it[1]}.ifEmpty([]) )
                                                                                         ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:25:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_files   = channel.empty()
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:41:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .findAll { it[0] != "*" && it[2].toInteger() > 0 }
                             ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:41:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .findAll { it[0] != "*" && it[2].toInteger() > 0 }
                                             ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:42:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect{ [meta, it[0], it[2].toInteger()] }
                                   ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:42:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect{ [meta, it[0], it[2].toInteger()] }
                                          ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:51:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, accession, num_reads, ref_accession, taxid, organism ->
                    ^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:51:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, accession, num_reads, ref_accession, taxid, organism ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:51:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, accession, num_reads, ref_accession, taxid, organism ->
                                                               ^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:51:69`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, accession, num_reads, ref_accession, taxid, organism ->
                                                                      ^^^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:54:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, accession, num_reads, ref_accession, taxid, organism ->
                                             ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:62:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              pass: it[4] >= min_read_counts // The number of mapped reads to a taxID greater than params.min_read_counts
                    ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:63:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                          ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:63:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                                 ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:63:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                                        ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:63:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                                               ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:64:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fail: it[4] < min_read_counts  // The number of mapped reads to a taxID smaller than params.min_read_counts
                    ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:65:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                          ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:65:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                                 ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:65:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                                        ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:65:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [it[0], it[1], it[2], it[3]] // [meta, accession_list, taxid, organism]
                                               ^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:96:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, mapped, pass -> pass }
                    ^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:96:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, mapped, pass -> pass }
                          ^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:96:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, mapped, pass -> pass }
                               ^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:97:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bam, mapped, pass -> [meta, bam] }
                            ^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:97:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bam, mapped, pass -> [meta, bam] }
                                    ^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:100:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bai, mapped, pass -> pass }
                    ^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:100:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bai, mapped, pass -> pass }
                          ^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:100:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bai, mapped, pass -> pass }
                               ^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:101:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bai, mapped, pass -> [meta, bai] }
                            ^^^^^^
  ```

- Warning: `subworkflows/local/taxid_bam_fasta.nf:101:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, bai, mapped, pass -> [meta, bai] }
                                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metaval_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metaval_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metaval_pipeline/main.nf:254:9`: Variable was declared but not used

  ```nextflow
      def logname = flagstat_file.getBaseName() - 'flagstat'
          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:18:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, bam, fasta, fai -> [meta, bam]},
                                       ^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:18:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, bam, fasta, fai -> [meta, bam]},
                                              ^^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:19:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, bam, fasta, fai -> [meta, fasta, fai]},
                                  ^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bowtie2/main.nf:21:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta = ch_fasta_fai.map { meta, fasta, fai -> [meta, fasta]}
                                                 ^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:16:5`: Variable was declared but not used

  ```nextflow
      valid_config = checkConfigProvided()
      ^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:54:5`: Variable was declared but not used

  ```nextflow
      ch_input              = file(params.input, checkIfExists: true)
      ^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                 ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                                 ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:96`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                                                 ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:114`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                                                                   ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:133`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                                                                                      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:152`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                                                                                                         ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:173`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                                                                                                                              ^^^^^^^
  ```

- Warning: `workflows/metaval.nf:76:182`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_input = ch_samplesheet.branch { meta, fastq_1, fastq_2, kraken2_report, kraken2_result, kraken2_taxpasta, centrifuge_report, centrifuge_result, centrifuge_taxpasta, diamond, diamond_taxpasta ->
                                                                                                                                                                                       ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:207:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads, filtered_blast -> [ meta, reads ] }
                                  ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:211:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads, filtered_blast -> [ meta, reads ] }
                                  ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaval.nf:246:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, bam,bai, mapped, pass -> if (pass) [meta, bam, bai ] }
                                        ^^^^^^
  ```

- Warning: `workflows/metaval.nf:260:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, bam,bai, mapped, pass -> if (pass) [meta, bam, bai ] }
                                        ^^^^^^
  ```

- Warning: `workflows/metaval.nf:299:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_accession2taxid = Channel.fromPath ( params.accession2taxid, checkIfExists: true )
                               ^^^^^^^
  ```

- Warning: `workflows/metaval.nf:332:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads ->
                        ^^^^
  ```

- Warning: `workflows/metaval.nf:337:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads ->
                        ^^^^
  ```

- Warning: `workflows/metaval.nf:352:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix( FASTQC.out.zip.collect{it[1]} )
                                                                      ^^
  ```

- Warning: `workflows/metaval.nf:358:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
