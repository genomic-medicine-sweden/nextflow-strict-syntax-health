# Nextflow lint results

- Generated: 2026-03-18T00:12:09.617285+00:00
- Nextflow version: 26.02.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/sanger-tol/gnk/fastasort/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix  = task.ext.prefix   ?: "${meta.id}"
          ^^^^^^^^^^
  ```
