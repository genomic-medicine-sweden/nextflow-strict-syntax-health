# Nextflow lint results

- Generated: 2026-03-24T10:44:51.643175222Z
- Nextflow version: 26.03.0-edge
- Summary: 52 warnings

## :warning: Warnings

- Warning: `modules/local/btk/input/main.nf:27:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ].findAll { it.value } // filter out falsy values (null, false, "", [], etc)
                  ^^
  ```

- Warning: `modules/local/cpretext/input/main.nf:22:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ].findAll { it.value } // filter out falsy values (null, false, "", [], etc)
                  ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:58:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list   = files_in.collect { it.toString() }
                                           ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def mat_ktab = matktab ? "${matktab.find{ it.toString().endsWith(".ktab") }}" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:42:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mat_ktab = matktab ? "${matktab.find{ it.toString().endsWith(".ktab") }}" : ''
                                                ^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def pat_ktab = patktab ? "${patktab.find{ it.toString().endsWith(".ktab") }}" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:43:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def pat_ktab = patktab ? "${patktab.find{ it.toString().endsWith(".ktab") }}" : ''
                                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ear_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ear_pipeline/main.nf:39:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:17:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hap1 = Channel.fromPath(inputs.reference_hap1, checkIfExists: true)
                ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:21:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(inputs.reference_hap2, checkIfExists: true).map { fasta -> tuple([id: inputs.assembly_id, file: 'hap2'], fasta) }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:22:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:25:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(inputs.reference_haplotigs, checkIfExists: true).map { fasta -> tuple([id: inputs.assembly_id, file: 'haplotigs'], fasta) }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:26:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:51:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      sample_id               = Channel.of([id: inputs.assembly_id])
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:52:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      longread_type           = inputs.longread.type ? Channel.of(inputs.longread.type): Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:52:88`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      longread_type           = inputs.longread.type ? Channel.of(inputs.longread.type): Channel.empty()
                                                                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:53:53`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      longread_dir            = inputs.longread.dir ? Channel.fromPath(inputs.longread.dir, checkIfExists: true, type: 'dir') : Channel.empty()
                                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:53:127`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      longread_dir            = inputs.longread.dir ? Channel.fromPath(inputs.longread.dir, checkIfExists: true, type: 'dir') : Channel.empty()
                                                                                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:58:64`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cpretext_aligner        = inputs.curationpretext.aligner ? Channel.of(inputs.curationpretext.aligner) : Channel.empty()
                                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:58:109`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cpretext_aligner        = inputs.curationpretext.aligner ? Channel.of(inputs.curationpretext.aligner) : Channel.empty()
                                                                                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:59:71`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cpretext_telomere_motif = inputs.curationpretext.telomere_motif ? Channel.of([id: inputs.assembly_id], inputs.curationpretext.telomere_motif) : Channel.empty()
                                                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:59:149`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cpretext_telomere_motif = inputs.curationpretext.telomere_motif ? Channel.of([id: inputs.assembly_id], inputs.curationpretext.telomere_motif) : Channel.empty()
                                                                                                                                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:60:64`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cpretext_hic_dir        = inputs.curationpretext.hic_dir ? Channel.fromPath(inputs.curationpretext.hic_dir, checkIfExists: true, type: 'dir') : Channel.empty()
                                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:60:149`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cpretext_hic_dir        = inputs.curationpretext.hic_dir ? Channel.fromPath(inputs.curationpretext.hic_dir, checkIfExists: true, type: 'dir') : Channel.empty()
                                                                                                                                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:62:61`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastk_hist              = inputs.merquryfk.fastk_hist ? Channel.fromPath(inputs.merquryfk.fastk_hist, checkIfExists: true) : Channel.empty()
                                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:62:130`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastk_hist              = inputs.merquryfk.fastk_hist ? Channel.fromPath(inputs.merquryfk.fastk_hist, checkIfExists: true) : Channel.empty()
                                                                                                                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:63:61`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastk_ktab              = inputs.merquryfk.fastk_ktab ? Channel.fromPath(inputs.merquryfk.fastk_ktab, hidden: true).collect()  : Channel.empty() // Collect as a list
                                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:63:134`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastk_ktab              = inputs.merquryfk.fastk_ktab ? Channel.fromPath(inputs.merquryfk.fastk_ktab, hidden: true).collect()  : Channel.empty() // Collect as a list
                                                                                                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:65:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_nt_database         = inputs.btk.nt_database ? Channel.fromPath(inputs.btk.nt_database, checkIfExists: true) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:65:120`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_nt_database         = inputs.btk.nt_database ? Channel.fromPath(inputs.btk.nt_database, checkIfExists: true) : Channel.empty()
                                                                                                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:66:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_nt_database_prefix  = inputs.btk.nt_database_prefix ? Channel.of(inputs.btk.nt_database_prefix) : Channel.empty()
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:66:107`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_nt_database_prefix  = inputs.btk.nt_database_prefix ? Channel.of(inputs.btk.nt_database_prefix) : Channel.empty()
                                                                                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:67:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_nr_diamond_database = inputs.btk.diamond_nr_database_path ? Channel.fromPath(inputs.btk.diamond_nr_database_path, checkIfExists: true) : Channel.empty()
                                                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:67:146`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_nr_diamond_database = inputs.btk.diamond_nr_database_path ? Channel.fromPath(inputs.btk.diamond_nr_database_path, checkIfExists: true) : Channel.empty()
                                                                                                                                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:68:74`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_un_diamond_database = inputs.btk.diamond_uniprot_database_path ? Channel.fromPath(inputs.btk.diamond_uniprot_database_path, checkIfExists: true) : Channel.empty()
                                                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:68:156`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_un_diamond_database = inputs.btk.diamond_uniprot_database_path ? Channel.fromPath(inputs.btk.diamond_uniprot_database_path, checkIfExists: true) : Channel.empty()
                                                                                                                                                             ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:69:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_ncbi_taxonomy_path  = inputs.btk.ncbi_taxonomy_path ? Channel.fromPath(inputs.btk.ncbi_taxonomy_path, checkIfExists: true) : Channel.empty()
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:69:134`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_ncbi_taxonomy_path  = inputs.btk.ncbi_taxonomy_path ? Channel.fromPath(inputs.btk.ncbi_taxonomy_path, checkIfExists: true) : Channel.empty()
                                                                                                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:70:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_taxid               = inputs.btk.taxid ? Channel.of(inputs.btk.taxid) : Channel.empty()
                                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:70:81`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_taxid               = inputs.btk.taxid ? Channel.of(inputs.btk.taxid) : Channel.empty()
                                                                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:71:58`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_gca_accession       = inputs.btk.gca_accession ? Channel.of(inputs.btk.gca_accession) : Channel.empty()
                                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:71:97`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      btk_gca_accession       = inputs.btk.gca_accession ? Channel.of(inputs.btk.gca_accession) : Channel.empty()
                                                                                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:72:53`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      busco_lineages          = inputs.btk.lineages ? Channel.of(inputs.btk.lineages) : Channel.empty()
                                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:72:87`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      busco_lineages          = inputs.btk.lineages ? Channel.of(inputs.btk.lineages) : Channel.empty()
                                                                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:73:51`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      busco_config            = inputs.btk.config ? Channel.fromPath(inputs.btk.config, checkIfExists: true) : Channel.empty()
                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yaml_input/main.nf:73:110`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      busco_config            = inputs.btk.config ? Channel.fromPath(inputs.btk.config, checkIfExists: true) : Channel.empty()
                                                                                                               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/ear.nf:51:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```
