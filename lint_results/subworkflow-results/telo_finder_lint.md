# Nextflow lint results

- Generated: 2026-03-26T00:13:01.030685+00:00
- Nextflow version: 26.03.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `subworkflows/sanger-tol/telo_finder/main.nf:92:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_regions_for_extraction.filter { meta, file -> meta.direction == 0 }
                                                   ^^^^^^^^^^
  ```
