# Nextflow lint results

- Generated: 2026-03-31T07:43:25.465909199Z
- Nextflow version: 26.03.1-edge
- Summary: 1 error, 5 warnings

## :x: Errors

- Error: `main.nf:54:42`: Unexpected input: '*'

    ```nextflow
        ch_gnomad_nuclear_snv   = channel.of(*1..22, 'X', 'Y')
                                             ^
    ```


## :warning: Warnings

- Warning: `modules/nf-core/bcftools/concat/main.nf:32:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

    ```nextflow
        def input = vcfs.sort{it.toString()}.join(" ")
                              ^^
    ```

- Warning: `subworkflows/local/utils_nfcore_rarediseaserefs_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
        monochrome_logs   // boolean: Do not use coloured log outputs
        ^^^^^^^^^^^^^^^
    ```

- Warning: `subworkflows/local/utils_nfcore_rarediseaserefs_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

    ```nextflow
        input             //  string: Path to input samplesheet
        ^^^^^
    ```

- Warning: `workflows/rarediseaserefs.nf:58:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

    ```nextflow
        def topic_versions = Channel.topic("versions")
                             ^^^^^^^
    ```

- Warning: `workflows/rarediseaserefs.nf:82:17`: Variable was declared but not used

    ```nextflow
            ).set { ch_collated_versions }
                    ^^^^^^^^^^^^^^^^^^^^
    ```
