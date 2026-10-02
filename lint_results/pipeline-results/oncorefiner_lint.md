# Nextflow lint results

- Generated: 2026-10-02T00:18:55.145993372Z
- Nextflow version: 26.09.1-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `main.nf:137:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_cadd_header = Channel.value(
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/process_svs/main.nf:48:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_sv_vcf_tbi             // channel: [required]  [val(meta), path(vcf.tbi)]
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:299:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ].findAll { key, value -> value != null }
                  ^^^
  ```

- Warning: `subworkflows/local/vcf_annotate_linx_fusions/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_sv_vcf_tbi         // channel: [required]  [val(meta), path(vcf.tbi)]
      ^^^^^^^^^^^^^
  ```
