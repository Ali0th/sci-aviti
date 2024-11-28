##Make AVITI sci-seq data compatible with the sci-rocket pipeline

date: 2024-11-28


Element Biosciences' NGS platform (AVITI) offers a lower price per read compared to illumina. Due to its unique chemistry, there are differences in the sequencing output files of AVITI which make it incompatible with the `bcl2fastq` part of `sci-rocket`. For this reason, until the `sci-rocket` pipeline is updated to become AVITI-compatible, some extra steps need to be taken in order to process the sequencing files. 

## Step 1: `bcl2fastq` conversion 

AVITI output folder structure and file types are different than those of Illumina. Element Biosciences provide their own `Bases2Fastq` software. Instructions for download and installation can be found here: [https://docs.elembio.io/docs/bases2fastq/](https://docs.elembio.io/docs/bases2fastq/). 

Before converting to FASTQ:

- Update the `RunManifest.json` file to include `index1` and `index2` in the FASTQ files. The `RunManifest.json` file is located in the AVITI sequencing output folder. An example of `RunManifest.json` that includes `index1` and `index2` can be found at   
`/g/hvu/MVlachonikolou/all_you_need_for_AVITI`. 

- Update `RunManifest.csv` with fake indices to direct all the reads along with the indices in the header to the Unassigned FASTQ files. An example of a fake `RunManifest.csv` can be found at  
`/g/hvu/MVlachonikolou/all_you_need_for_AVITI`. 

To convert the BCL files to FASTQ, simply run:

```{bash, eval = FALSE}
path/to/bases2fastq path/to/Sequencing_Data/ path/to/bases2fastq_output
```

Go to `path/to/bases2fastq_output/Samples/Unassigned` and rename the fastq files to Undetermined_S0_R1_001.fastq.gz and Undetermined_S0_R2_001.fastq.gz. 


For more details, see [https://docs.elembio.io/docs/bases2fastq/](https://docs.elembio.io/docs/bases2fastq/).



## Step 2: `sci-rocket` demultiplexing 

The `.fastq.gz` files are almost identical to Illumina's, apart from an important difference. Illumina sequences the reverse complement of the `p5` index. `sci-rocket` takes this into account when reading the sequences and reverses the `p5` to match the `example_barcodes`. AVITI, on the other hand, reads `p5` exactly as it is on the `example_barcodes` list. To avoid errors, create a modified `example_barcodes.tsv` file with reverse complement `p5` oligos and point the `sci-rocket` config file to it. An example of an updated `example_barcodes.tsv` can be found at  
`/g/hvu/MVlachonikolou/all_you_need_for_AVITI`. 

Finally, point the `path_fastq` of the `sci-rocket sample_sheet.tsv` to:   
`path/to/bases2fastq_output/Samples/Unassigned`

This will have the unidentified `R1` and `R2` `.fastq.gz` files.

Now you are ready to run `sci-rocket` on your AVITI sequencing data!

Good Luck,  
MV

