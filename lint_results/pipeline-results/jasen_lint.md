# Nextflow lint results

- Generated: 2026-05-01T00:30:33.277331065Z
- Nextflow version: 26.04.0
- Summary: 60 errors, 21 warnings

## :x: Errors

- Error: `conf/ngp.config:15:42`: `outdir` is not defined

  ```nextflow
      tracedir                        = "${outdir}/pipeline_info"
                                           ^^^^^^
  ```

- Error: `conf/ngp.config:16:42`: `root` is not defined

  ```nextflow
      containers_dir                  = "${root}/containers"
                                           ^^^^
  ```

- Error: `conf/ngp.config:17:42`: `root` is not defined

  ```nextflow
      amrfinder_db                    = "${root}/assets/amrfinder_db/latest"
                                           ^^^^
  ```

- Error: `conf/ngp.config:18:42`: `root` is not defined

  ```nextflow
      resfinder_db                    = "${root}/assets/resfinder_db"
                                           ^^^^
  ```

- Error: `conf/ngp.config:19:42`: `root` is not defined

  ```nextflow
      pointfinder_db                  = "${root}/assets/pointfinder_db"
                                           ^^^^
  ```

- Error: `conf/ngp.config:20:42`: `root` is not defined

  ```nextflow
      serotypefinder_db               = "${root}/assets/serotypefinder_db"
                                           ^^^^
  ```

- Error: `conf/ngp.config:21:42`: `root` is not defined

  ```nextflow
      virulencefinder_db              = "${root}/assets/virulencefinder_db"
                                           ^^^^
  ```

- Error: `conf/ngp.config:22:42`: `root` is not defined

  ```nextflow
      mlst_blast_db                   = "${root}/assets/mlst_db/blast"
                                           ^^^^
  ```

- Error: `conf/ngp.config:23:42`: `root` is not defined

  ```nextflow
      pubmlst_db                      = "${root}/assets/mlst_db/pubmlst"
                                           ^^^^
  ```

- Error: `conf/ngp.config:24:42`: `root` is not defined

  ```nextflow
      gambit_db                       = "${root}/assets/gambit_db"
                                           ^^^^
  ```

- Error: `conf/ngp.config:26:42`: `workDir` is not defined

  ```nextflow
      workDir                         = "${workDir}"
                                           ^^^^^^^
  ```

- Error: `main.nf:5:1`: Included name 'CALL_MYCOBACTERIUM_TUBERCULOSIS' is not defined in module '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/jasen/workflows/mycobacterium_tuberculosis.nf'

  ```nextflow
  include { CALL_MYCOBACTERIUM_TUBERCULOSIS   } from './workflows/mycobacterium_tuberculosis.nf'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:6:1`: Included name 'CALL_BACTERIAL_GENERAL' is not defined in module '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/jasen/workflows/bacterial_general.nf'

  ```nextflow
  include { CALL_BACTERIAL_GENERAL            } from './workflows/bacterial_general.nf'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:10:9`: `CALL_MYCOBACTERIUM_TUBERCULOSIS` is not defined

  ```nextflow
          CALL_MYCOBACTERIUM_TUBERCULOSIS()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:12:9`: `CALL_BACTERIAL_GENERAL` is not defined

  ```nextflow
          CALL_BACTERIAL_GENERAL()
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `methods/get_sample_data.nf:3:5`: `platforms` was assigned but not declared

  ```nextflow
      platforms = ["illumina", "nanopore", "pacbio", "iontorrent"]
      ^^^^^^^^^
  ```

- Error: `methods/get_sample_data.nf:4:25`: `platforms` is not defined

  ```nextflow
      if (row.platform in platforms) {
                          ^^^^^^^^^
  ```

- Error: `methods/get_sample_data.nf:5:9`: `meta` was assigned but not declared

  ```nextflow
          meta = tuple(row.id, row.platform)
          ^^^^
  ```

- Error: `methods/get_sample_data.nf:7:102`: `platforms` is not defined

  ```nextflow
          exit 1, "ERROR: Please check input samplesheet -> Platform is not one of the following:!\n-${platforms.join('\n-')}"
                                                                                                       ^^^^^^^^^
  ```

- Error: `methods/get_sample_data.nf:9:12`: `meta` is not defined

  ```nextflow
      return meta
             ^^^^
  ```

- Error: `methods/get_sample_data.nf:13:5`: `platforms` was assigned but not declared

  ```nextflow
      platforms = ["illumina", "nanopore", "pacbio", "iontorrent"]
      ^^^^^^^^^
  ```

- Error: `methods/get_sample_data.nf:14:25`: `platforms` is not defined

  ```nextflow
      if (row.platform in platforms) {
                          ^^^^^^^^^
  ```

- Error: `methods/get_sample_data.nf:16:13`: `reads` was assigned but not declared

  ```nextflow
              reads = tuple(row.id, tuple(file(row.read1), file(row.read2)))
              ^^^^^
  ```

- Error: `methods/get_sample_data.nf:18:13`: `reads` was assigned but not declared

  ```nextflow
              reads = tuple(row.id, tuple(file(row.read1)))
              ^^^^^
  ```

- Error: `methods/get_sample_data.nf:21:102`: `platforms` is not defined

  ```nextflow
          exit 1, "ERROR: Please check input samplesheet -> Platform is not one of the following:!\n-${platforms.join('\n-')}"
                                                                                                       ^^^^^^^^^
  ```

- Error: `methods/get_sample_data.nf:23:12`: `reads` is not defined

  ```nextflow
      return reads
             ^^^^^
  ```

- Error: `methods/get_seqrun_meta.nf:4:9`: `meta` was assigned but not declared

  ```nextflow
          meta = [row.id, row.sequencing_run]
          ^^^^
  ```

- Error: `methods/get_seqrun_meta.nf:8:9`: `meta` is not defined

  ```nextflow
          meta << row.clarity_sample_id
          ^^^^
  ```

- Error: `methods/get_seqrun_meta.nf:12:9`: `meta` is not defined

  ```nextflow
          meta << row.sample_name
          ^^^^
  ```

- Error: `methods/get_seqrun_meta.nf:16:18`: `meta` is not defined

  ```nextflow
      return tuple(meta)
                   ^^^^
  ```

- Error: `methods/get_taxon.nf:3:3`: `names` was assigned but not declared

  ```nextflow
    names = fullName.split(' ')
    ^^^^^
  ```

- Error: `methods/get_taxon.nf:5:12`: `names` is not defined

  ```nextflow
      return names[0].capitalize()
             ^^^^^
  ```

- Error: `methods/get_taxon.nf:9:10`: `names` is not defined

  ```nextflow
    return names[0].capitalize() + "_" + names[1]
           ^^^^^
  ```

- Error: `methods/get_taxon.nf:9:40`: `names` is not defined

  ```nextflow
    return names[0].capitalize() + "_" + names[1]
                                         ^^^^^
  ```

- Error: `modules/local/meta/main.nf:15:9`: `assay` is already declared

  ```nextflow
      def assay = assay ?: ""
          ^^^^^
  ```

- Error: `modules/local/meta/main.nf:17:9`: `lims_id` is already declared

  ```nextflow
      def lims_id = lims_id ?: ""
          ^^^^^^^
  ```

- Error: `modules/local/meta/main.nf:19:9`: `release_life_cycle` is already declared

  ```nextflow
      def release_life_cycle = release_life_cycle ?: ""
          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/meta/main.nf:21:9`: `sequencing_run` is already declared

  ```nextflow
      def sequencing_run = sequencing_run ?: ""
          ^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mlst/main.nf:1:1`: Invalid process definition -- check for missing or out-of-order section labels

  ```nextflow
  process mlst {
  ^
  ```

- Error: `modules/nf-core/samtools/main.nf:24:29`: `sample_id` is not defined

  ```nextflow
      cat <<-END_VERSIONS > ${sample_id}_${task.process}_versions.yml
                              ^^^^^^^^^
  ```

- Error: `modules/nf-core/samtools/main.nf:34:13`: `sample_id` is not defined

  ```nextflow
      touch ${sample_id}.bam
              ^^^^^^^^^
  ```

- Error: `modules/nf-core/samtools/main.nf:35:13`: `sample_id` is not defined

  ```nextflow
      touch ${sample_id}.cram
              ^^^^^^^^^
  ```

- Error: `modules/nf-core/samtools/main.nf:37:29`: `sample_id` is not defined

  ```nextflow
      cat <<-END_VERSIONS > ${sample_id}_${task.process}_versions.yml
                              ^^^^^^^^^
  ```

- Error: `nextflow.config:16:34`: `outdir` is not defined

  ```nextflow
      tracedir                = "${outdir}/pipeline_info"
                                   ^^^^^^
  ```

- Error: `nextflow.config:22:34`: `workDir` is not defined

  ```nextflow
      workDir                 = "${workDir}"
                                   ^^^^^^^
  ```

- Error: `nextflow.config:319:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def trace_timestamp = new java.util.Date().format('yyyy-MM-dd_HH-mm-ss')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:322:60`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/execution_timeline_${trace_timestamp}.html"
                                                             ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:327:58`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/execution_report_${trace_timestamp}.html"
                                                           ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:332:57`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/execution_trace_${trace_timestamp}.txt"
                                                          ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:337:54`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/pipeline_dag_${trace_timestamp}.html"
                                                       ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/preprocessing.nf:44:42`: `target_sample_size` is not defined

  ```nextflow
          seqtk_sample( ch_depleted_reads, target_sample_size ).reads.set{ ch_depleted_sampled_reads }
                                           ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/typing.nf:15:1`: Included name 'mlst' is not defined in module '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/jasen/modules/nf-core/mlst/main.nf'

  ```nextflow
  include { mlst                                      } from '../modules/nf-core/mlst/main.nf'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/typing.nf:45:9`: `mlst` is not defined

  ```nextflow
          mlst(ch_assembly, mlst_scheme, pubmlst_db, mlst_blast_db)
          ^^^^
  ```

- Error: `subworkflows/typing.nf:46:9`: `mlst` is not defined

  ```nextflow
          mlst.out.json.set{ ch_mlst }
          ^^^^
  ```

- Error: `subworkflows/typing.nf:47:39`: `mlst` is not defined

  ```nextflow
          ch_versions = ch_versions.mix(mlst.out.versions)
                                        ^^^^
  ```

- Error: `subworkflows/typing.nf:189:5`: Workflow emit `serotypefinder` is already declared

  ```nextflow
      serotypefinder  = ch_serotypefinder_meta              // channel: [ val(meta), path(json) ]
      ^^^^^^^^^^^^^^
  ```

- Error: `workflows/bacterial_general.nf:14:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow CALL_BACTERIAL_GENERAL {
  ^
  ```

- Error: `workflows/bacterial_general.nf:159:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `workflows/mycobacterium_tuberculosis.nf:14:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow CALL_MYCOBACTERIUM_TUBERCULOSIS {
  ^
  ```

- Error: `workflows/mycobacterium_tuberculosis.nf:147:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

## :warning: Warnings

- Warning: `modules/local/meta/main.nf:16:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def config_files = workflow.configFiles.collect { "\"${it.toString().trim()}\"" }.unique().join(", ")
                                                             ^^
  ```

- Warning: `modules/local/meta/main.nf:18:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def profiles = workflow.profile.split(",").collect { "\"${it.trim()}\"" }.join(", ")
                                                                ^^
  ```

- Warning: `modules/nf-core/kleborate/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def file_name = task.ext.result_filename ?: ''
          ^^^^^^^^^
  ```

- Warning: `subworkflows/assembly.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/assembly.nf:26:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty()
      ^^^^^^^
  ```

- Warning: `subworkflows/postprocessing.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:28:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromPath(input_samples)
      ^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:30:15`: Variable was declared but not used

  ```nextflow
          .tap{ ch_raw_input }
                ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:60:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromPath(input_samples).splitCsv(header:true)
      ^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:63:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ id, sequencing_run, lims_id, sample_name -> [ id, lims_id, sample_name ]}
                    ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:67:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reads.map{ sample_id, reads -> [ sample_id, [] ] }.set{ ch_sample_id }
                               ^^^^^
  ```

- Warning: `subworkflows/profiling.nf:12:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      core_loci_bed
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/profiling.nf:16:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_assembly
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/profiling.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/quality_control.nf:34:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/relatedness.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/screening.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/typing.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      species
      ^^^^^^^
  ```

- Warning: `subworkflows/typing.nf:41:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/variant_calling.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```
