# Nextflow lint results

- Generated: 2026-03-07T00:07:47.028412+00:00
- Nextflow version: 26.02.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/sanger-tol/gnk/fastasort/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix  = task.ext.prefix   ?: "${meta.id}"
          ^^^^^^^^^^
  ```
