# Nextflow lint results

- Generated: 2026-11-18T00:12:06.371768055Z
- Nextflow version: 26.11.0-edge
- Summary: 69 errors, 60 warnings

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

- Error: `main.nf:5:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (!nextflow.version.matches('>=25.04.0')) {
  ^
  ```

- Error: `main.nf:9:1`: Included name 'CALL_MYCOBACTERIUM_TUBERCULOSIS' is not defined in module '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/jasen/workflows/mycobacterium_tuberculosis.nf'

  ```nextflow
  include { CALL_MYCOBACTERIUM_TUBERCULOSIS   } from './workflows/mycobacterium_tuberculosis.nf'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:10:1`: Included name 'CALL_BACTERIAL_GENERAL' is not defined in module '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/jasen/workflows/bacterial_general.nf'

  ```nextflow
  include { CALL_BACTERIAL_GENERAL            } from './workflows/bacterial_general.nf'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:14:9`: `CALL_MYCOBACTERIUM_TUBERCULOSIS` is not defined

  ```nextflow
          CALL_MYCOBACTERIUM_TUBERCULOSIS()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:16:9`: `CALL_BACTERIAL_GENERAL` is not defined

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

- Error: `modules/nf-core/mlst/main.nf:14:11`: Unexpected input: ':'

  ```nextflow
      output:
            ^
  ```

- Error: `modules/nf-core/samtools/main.nf:27:13`: `sample_id` is not defined

  ```nextflow
      touch ${sample_id}.bam
              ^^^^^^^^^
  ```

- Error: `modules/nf-core/samtools/main.nf:28:13`: `sample_id` is not defined

  ```nextflow
      touch ${sample_id}.cram
              ^^^^^^^^^
  ```

- Error: `nextflow.config:16:34`: `outdir` is not defined

  ```nextflow
      tracedir                = "${outdir}/pipeline_info"
                                   ^^^^^^
  ```

- Error: `nextflow.config:23:34`: `workDir` is not defined

  ```nextflow
      workDir                 = "${workDir}"
                                   ^^^^^^^
  ```

- Error: `nextflow.config:39:34`: `assets_dir` is not defined

  ```nextflow
      amrfinder_db            = "${assets_dir}/amrfinder_db/latest"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:40:34`: `assets_dir` is not defined

  ```nextflow
      emmtyper_db             = "${assets_dir}/emmtyper_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:41:34`: `assets_dir` is not defined

  ```nextflow
      gambit_db               = "${assets_dir}/gambit_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:42:34`: `assets_dir` is not defined

  ```nextflow
      hostile_dir             = "${assets_dir}/hostile_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:44:34`: `assets_dir` is not defined

  ```nextflow
      mlst_blast_db           = "${assets_dir}/mlstdb/blast"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:45:34`: `assets_dir` is not defined

  ```nextflow
      plasmidfinder_db        = "${assets_dir}/plasmidfinder_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:46:34`: `assets_dir` is not defined

  ```nextflow
      pointfinder_db          = "${assets_dir}/pointfinder_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:47:34`: `assets_dir` is not defined

  ```nextflow
      pubmlst_db              = "${assets_dir}/mlstdb/pubmlst"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:48:34`: `assets_dir` is not defined

  ```nextflow
      resfinder_db            = "${assets_dir}/resfinder_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:49:34`: `assets_dir` is not defined

  ```nextflow
      serotypefinder_db       = "${assets_dir}/serotypefinder_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:51:34`: `assets_dir` is not defined

  ```nextflow
      virulencefinder_db      = "${assets_dir}/virulencefinder_db"
                                   ^^^^^^^^^^
  ```

- Error: `nextflow.config:334:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def trace_timestamp = new java.util.Date().format('yyyy-MM-dd_HH-mm-ss')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:337:60`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/execution_timeline_${trace_timestamp}.html"
                                                             ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:342:58`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/execution_report_${trace_timestamp}.html"
                                                           ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:347:57`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/execution_trace_${trace_timestamp}.txt"
                                                          ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:352:54`: `trace_timestamp` is not defined

  ```nextflow
      file        = "${params.tracedir}/pipeline_dag_${trace_timestamp}.html"
                                                       ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/preprocessing.nf:58:42`: `target_sample_size` is not defined

  ```nextflow
          seqtk_sample( ch_depleted_reads, target_sample_size ).reads.set{ ch_depleted_sampled_reads }
                                           ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/typing.nf:15:1`: Included name 'mlst' is not defined in module '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/jasen/modules/nf-core/mlst/main.nf'

  ```nextflow
  include { mlst                                      } from '../modules/nf-core/mlst/main.nf'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/typing.nf:42:9`: `mlst` is not defined

  ```nextflow
          mlst(ch_assembly, mlst_scheme, pubmlst_db, mlst_blast_db)
          ^^^^
  ```

- Error: `subworkflows/typing.nf:43:9`: `mlst` is not defined

  ```nextflow
          mlst.out.json.set{ ch_mlst }
          ^^^^
  ```

- Error: `subworkflows/typing.nf:168:5`: Workflow emit `serotypefinder` is already declared

  ```nextflow
      serotypefinder  = ch_serotypefinder_meta              // channel: [ val(meta), path(json) ]
      ^^^^^^^^^^^^^^
  ```

- Error: `workflows/bacterial_general.nf:53:9`: Unexpected input: ':'

  ```nextflow
      main:
          ^
  ```

- Error: `workflows/bacterial_general.nf:144:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `workflows/mycobacterium_tuberculosis.nf:53:9`: Unexpected input: ':'

  ```nextflow
      main:
          ^
  ```

- Error: `workflows/mycobacterium_tuberculosis.nf:141:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

## :warning: Warnings

- Warning: `methods/get_sample_data.nf:27:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def lines = file(samplesheet).readLines().findAll { it.trim() }
                                                          ^^
  ```

- Warning: `modules/local/chewbbaca/split/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/local/clean/main.nf:11:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/local/jasentool/main.nf:157:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/local/mask/main.nf:11:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

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

- Warning: `modules/nf-core/amrfinderplus/main.nf:16:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/bracken/main.nf:14:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/bwa/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/bwa/main.nf:45:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/chewbbaca/main.nf:14:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/clair3/main.nf:15:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/emmtyper/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:15:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/filtlong/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/flye/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/freebayes/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/hostile/main.nf:14:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/kleborate/main.nf:14:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/kleborate/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def file_name = task.ext.result_filename ?: ''
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken/main.nf:14:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/kraken/main.nf:78:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/medaka/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/minimap2/main.nf:13:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/minimap2/main.nf:43:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/mykrobe/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/nanoplot/main.nf:13:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/plasmidfinder/main.nf:19:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/resfinder/main.nf:22:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/samtools/main.nf:14:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/samtools/main.nf:43:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/samtools/main.nf:70:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/samtools/main.nf:146:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/samtools/main.nf:175:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/sccmec/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/seqtk/main.nf:13:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/serotypefinder/main.nf:16:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/shigatyper/main.nf:13:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/skesa/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/snippy/main.nf:15:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/spatyper/main.nf:12:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/tbprofiler/main.nf:15:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/trimmomatic/main.nf:13:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `modules/nf-core/virulencefinder/main.nf:16:5`: The `when` section is deprecated -- use conditional logic in the calling workflow, or the `process.when` config option to disable a process at runtime

  ```nextflow
      when:
      ^^^^
  ```

- Warning: `subworkflows/assembly.nf:24:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty()
      ^^^^^^^
  ```

- Warning: `subworkflows/postprocessing.nf:27:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.topic('versions')
      ^^^^^^^
  ```

- Warning: `subworkflows/postprocessing.nf:33:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it.join('\n') + '\n' }
                 ^^
  ```

- Warning: `subworkflows/postprocessing.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[0] }
                 ^^
  ```

- Warning: `subworkflows/postprocessing.nf:67:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[0] }
                 ^^
  ```

- Warning: `subworkflows/postprocessing.nf:69:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it] }
                  ^^
  ```

- Warning: `subworkflows/postprocessing.nf:70:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(create_yaml.out.yaml.map { it[0] }.toList().map { [it] })
                                              ^^
  ```

- Warning: `subworkflows/postprocessing.nf:70:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(create_yaml.out.yaml.map { it[0] }.toList().map { [it] })
                                                                      ^^
  ```

- Warning: `subworkflows/preprocessing.nf:31:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromList(samplesheetToList(input_samples, "${projectDir}/assets/schema_input.json"))
      ^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:77:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ id, sequencing_run, lims_id, sample_name -> [ id, lims_id, sample_name ]}
                    ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/preprocessing.nf:81:30`: Parameter was not used -- prefix with `_` to suppress warning

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

- Warning: `subworkflows/typing.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      species
      ^^^^^^^
  ```
