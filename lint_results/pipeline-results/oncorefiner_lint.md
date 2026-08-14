# Nextflow lint results

- Generated: 2026-08-14T00:18:37.853983573Z
- Nextflow version: 26.07.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `main.nf:132:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_cadd_header = Channel.value(
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:284:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ].findAll { key, value -> value != null }
                  ^^^
  ```

- Warning: `subworkflows/local/vcf_annotate_linx_fusions/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_sv_vcf_tbi         // channel: [required]  [val(meta), path(vcf.tbi)]
      ^^^^^^^^^^^^^
  ```
