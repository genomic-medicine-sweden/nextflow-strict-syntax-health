# Nextflow lint results

- Generated: 2026-10-06T00:18:20.859608776Z
- Nextflow version: 26.09.1-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_nallo_pipeline/main.nf:758:317`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  def validateWorkflowCompatibility(val_str_caller, val_skip_repeat_annotation, val_snv_caller, val_snv_calling_processes, val_skip_sv_calling, val_sv_callers_to_run, val_skip_snv_calling, val_cnv_expected_xy_cn, val_cnv_expected_xx_cn, val_cnv_excluded_regions, val_skip_phasing, val_phaser, val_sv_callers_to_merge, val_skip_portello) {
                                                                                                                                                                                                                                                                                                                              ^^^^^^^^^^^^^^^^^
  ```
