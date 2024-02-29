<script lang="ts">
  import { createEventDispatcher, tick, getContext } from "svelte";

  // import { upload_files as default_upload_files } from "@gradio/client";

  // import { blobToBase64, normalise_file } from "@gradio/upload";
  import {
    upload,
    prepare_files,
    normalise_file,
    type FileData,
  } from "@gradio/client";

  import LoadingSpinner from "./loading_spinner.svelte";
  let uploaded_files;

  const dispatch = createEventDispatcher();

  export let root: string;

  const upload_fn = getContext<typeof upload_files>("upload_files");

  async function handle_upload(file_data: FileData[]): Promise<void> {
    await tick();
    uploaded_files = await upload(file_data, root, upload_fn);
    uploaded_files[0].orig_name = file_data.name;
    uploaded_files[0].size = file_data.size;
    dispatch("load", uploaded_files);
  }

  // async function handle_upload(file_data: FileData[]): Promise<void> {
  //   await tick();
  //   let files = (Array.isArray(file_data) ? file_data : [file_data]).map(
  //     (file_data) => file_data.blob!
  //   );

  //   await upload_files(root, files).then(async (response) => {
  //     if (response.error) {
  //       (Array.isArray(file_data) ? file_data : [file_data]).forEach(
  //         async (file_data, i) => {
  //           file_data.data = await blobToBase64(file_data.blob!);
  //           file_data.blob = undefined;
  //         }
  //       );
  //     } else {
  //       (Array.isArray(file_data) ? file_data : [file_data]).forEach((f, i) => {
  //         if (response.files) {
  //           f.orig_name = f.name;
  //           f.name = response.files[i];
  //           f.is_file = true;
  //           f.blob = undefined;
  //           normalise_file(f, root, null);
  //         }
  //       });
  //     }
  //   });
  //   console.log(file_data);
  //   dispatch("load", file_data);
  // }

  let loading = false;

  async function fetchFromDB(identifier, database): Promise<void> {
    let dbs = {
      pdb_assym: {
        url: "https://files.rcsb.org/view/",
        ext: ".pdb",
      },
      pdb_bioass: {
        url: "https://files.rcsb.org/view/",
        ext: ".pdb1",
      },
      af: {
        url: "https://alphafold.ebi.ac.uk/files/AF-",
        ext: "-F1-model_v4.pdb",
      },
      esm: {
        url: "https://api.esmatlas.com/fetchPredictedStructure/",
        ext: ".pdb",
      },
      // pubchem: "pubchem",
      // text: "text",
    };
    let url = dbs[database]["url"];
    let ext = dbs[database]["ext"];
    // load the file and save blob

    // emulate file upload by fetching from the db and triggering upload
    // check if response status is 200, then return blob

    loading = true;
    let file = null;
    try {
      file = await fetch(url + identifier + ext).then((r) => {
        loading = false;
        if (r.status == 200) {
          let b = r.blob();
          b.name = identifier + ext;
          return b;
        } else {
          dispatch("notfound");
        }
      });
    } catch (error) {
      loading = false;
      dispatch("notfound");
    }

    let file_data = {
      name: identifier + ".pdb",
      size: file.size,
      data: "",
      blob: file,
    };

    await handle_upload(file_data);
  }

  let selectedValue = "pdb_assym";
  let placeholder = "";
  let textInput = "";
  function handleSelect(event) {
    selectedValue = event.target.value;
  }
  let placeholders = {
    pdb_assym: "Enter PDB identifier",
    pdb_bioass: "Enter PDB identifier",
    af: "Enter UniProt identifier",
    esm: "Enter MGnify protein identifier",
    // pubchem: "Enter PubChem identifier",
    // text: "Enter molecule in PDB or mol2 format",
  };
  $: placeholder = placeholders[selectedValue];

  function isEnterPressed(event) {
    if (event.key === "Enter") {
      fetchFromDB(textInput, selectedValue);
    }
  }
</script>

<div class="flex mt-2">
  <div class="flex input wfull">
    <input
      type="text"
      {placeholder}
      class="wfull inp"
      bind:value={textInput}
      on:keydown={isEnterPressed}
    />
    <select name="" id="" class="select" on:change={handleSelect}>
      <option value="pdb_assym">PDB Assym. Unit</option>
      <option value="pdb_bioass">PDB BioAssembly</option>
      <option value="af">AlphaFold DB</option>
      <option value="esm">ESMFold DB</option>
      <!-- <option value="pubchem">Pubchem</option>
      <option value="text">Text input</option> -->
    </select>
  </div>
  <button
    class="btn text-center"
    on:click={() => fetchFromDB(textInput, selectedValue)}
  >
    {#if loading}
      <LoadingSpinner />
    {:else}
      <span>Fetch</span>
    {/if}
  </button>
</div>
<span class="or py">- or -</span>

<style>
  .py {
    padding: 10px 0;
  }
  .btn {
    margin: 0 5px;
    padding: 3px 15px;
    border: var(--button-border-width) solid
      var(--button-secondary-border-color);
    background: var(--button-secondary-background-fill);
    color: var(--button-secondary-text-color);
    border-radius: var(--button-large-radius);
    padding: var(--button-large-padding);
    font-weight: var(--button-large-text-weight);
    font-size: var(--button-large-text-size);
    cursor: pointer;
  }
  .btn:hover {
    border-color: var(--button-secondary-border-color-hover);
    background: var(--button-secondary-background-fill-hover);
    color: var(--button-secondary-text-color-hover);
    box-shadow: var(--button-shadow-hover);
  }
  .or {
    color: var(--body-text-color-subdued);
    text-align: center;
    display: block;
  }
  .wfull {
    width: 100%;
  }
  .mt-2 {
    margin-top: 2rem;
  }

  .input {
    box-shadow: var(--input-shadow);
    background: var(--input-background-fill);
    border: var(--input-border-width) solid var(--input-border-color);
    border-radius: var(--input-radius);
    margin: 0 5px;
  }
  .select {
    outline: none;
    border: none;
  }
  .flex {
    display: flex;
    justify-content: space-between;
  }
  .inp {
    width: 100%;
    border: 0 #fff !important;
    outline: none !important;
  }
  .inp:focus,
  .inp:hover {
    border: 0 !important;
    outline: none !important;
  }
  .text-center {
    text-align: center;
  }
</style>
