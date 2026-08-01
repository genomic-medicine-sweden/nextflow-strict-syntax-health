# Nextflow lint results

- Generated: 2026-08-01T00:26:36.488408095Z
- Nextflow version: 26.07.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:277:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ].findAll { key, value -> value != null }
                  ^^^
  ```
