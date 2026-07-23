# Nextflow lint results

- Generated: 2026-07-23T00:29:00.800473609Z
- Nextflow version: 26.07.0-edge
- Summary: 9 errors

## :x: Errors

- Error: `modules/nf-core/hiphase/main.nf:69:28`: Unexpected character: '\'

  ```nextflow
          ${blocks_file_arg} \ \
                             ^
  ```

- Error: `subworkflows/local/hiphase/main.nf:1:1`: Module could not be parsed: '/home/runner/work/nextflow-strict-syntax-health/nextflow-strict-syntax-health/pipelines/nallo/modules/nf-core/hiphase/main.nf'

  ```nextflow
  include { HIPHASE as RUN_HIPHASE } from '../../../modules/nf-core/hiphase/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hiphase/main.nf:38:5`: `RUN_HIPHASE` is not defined

  ```nextflow
      RUN_HIPHASE(
      ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hiphase/main.nf:53:30`: `RUN_HIPHASE` is not defined

  ```nextflow
      ch_haplotagged_bam_bai = RUN_HIPHASE.out.bams
                               ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hiphase/main.nf:54:15`: `RUN_HIPHASE` is not defined

  ```nextflow
          .join(RUN_HIPHASE.out.bams_indexes, failOnMismatch: true, failOnDuplicate: true)
                ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hiphase/main.nf:65:27`: `RUN_HIPHASE` is not defined

  ```nextflow
      phased_snvs         = RUN_HIPHASE.out.vcfs // channel: [ val(meta), path(vcf) ]
                            ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hiphase/main.nf:66:27`: `RUN_HIPHASE` is not defined

  ```nextflow
      phased_snvs_tbi     = RUN_HIPHASE.out.vcfs_indexes // channel: [ val(meta), path(tbi) ]
                            ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hiphase/main.nf:67:44`: `RUN_HIPHASE` is not defined

  ```nextflow
      phased_svs          = phase_with_svs ? RUN_HIPHASE.out.sv_vcfs : ch_sv_vcf // channel: [ val(meta), path(vcf) ]
                                             ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hiphase/main.nf:68:44`: `RUN_HIPHASE` is not defined

  ```nextflow
      phased_svs_tbi      = phase_with_svs ? RUN_HIPHASE.out.sv_vcfs_indexes : ch_sv_vcf_index // channel: [ val(meta), path(tbi) ]
                                             ^^^^^^^^^^^
  ```
