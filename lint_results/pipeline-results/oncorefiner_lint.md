# Nextflow lint results

- Generated: 2026-07-31T00:30:22.320272343Z
- Nextflow version: 26.07.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:277:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ].findAll { key, value -> value != null }
                  ^^^
  ```
