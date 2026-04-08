# Nextflow lint results

- Generated: 2026-04-08T00:22:42.865785809Z
- Nextflow version: 26.03.2-edge
- Summary: 7 warnings

## :warning: Warnings

- Warning: `main.nf:56:5`: Variable was declared but not used

  ```nextflow
      ch_vep_cache_unprocessed = val_vep_cache ? channel.fromPath(val_vep_cache).map { it -> [[id:'vep_cache'], it] }.collect()
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `main.nf:73:5`: Variable was declared but not used

  ```nextflow
      ch_svdb_dbs             = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncorefiner_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:16:5`: Variable was declared but not used

  ```nextflow
      valid_config = checkConfigProvided()
      ^^^^^^^^^^^^
  ```

- Warning: `workflows/oncorefiner.nf:45:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_samplesheet        // channel: [mandatory] samplesheet read in from --input
          ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/oncorefiner.nf:51:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_sv_vcf_tbi         // channel: [optional]  [val(meta), path(vcf.tbi)]
          ^^^^^^^^^^^^^
  ```
