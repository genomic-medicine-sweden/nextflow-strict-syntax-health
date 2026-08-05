# Nextflow lint results

- Generated: 2026-08-05T00:29:12.174763866Z
- Nextflow version: 26.07.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:277:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ].findAll { key, value -> value != null }
                  ^^^
  ```

- Warning: `subworkflows/local/vcf_annotate_linx_fusions/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_sv_vcf_tbi         // channel: [required]  [val(meta), path(vcf.tbi)]
      ^^^^^^^^^^^^^
  ```
