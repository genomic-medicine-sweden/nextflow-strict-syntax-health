# Nextflow lint results

- Generated: 2026-03-20T17:27:59.913562254Z
- Nextflow version: 26.03.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `workflows/curationpretext.nf:209:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { mapped_meta, bam, ref_meta, ref_fasta ->
                                   ^^^^^^^^
  ```

- Warning: `workflows/curationpretext.nf:209:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { mapped_meta, bam, ref_meta, ref_fasta ->
                                             ^^^^^^^^^
  ```
