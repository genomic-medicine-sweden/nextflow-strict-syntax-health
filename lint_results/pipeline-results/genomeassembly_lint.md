# Nextflow lint results

- Generated: 2026-03-06T00:13:31.748498212Z
- Nextflow version: 26.02.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/local/organelle_assembly/main.nf:17:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          spec.stages.collect { stageName, stageData -> setupStage(spec, stageName) }
                                           ^^^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/main.nf:66:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { spec, fasta, bed_chunks, lr_bam, lr_bai, lr_csv, vcf, tbi ->
                                  ^^^^^^^^^^
  ```
