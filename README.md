# TE_pipeline

## Setup
clone this repo xxxxx
insurveyor - if using clustering computing then singularity option is rec https://github.com/kensung-lab/INSurVeyor/releases/download/1.1.2/insurveyor.sif
ensure htslib is installed sudo apt-get install autoconf zlib1g-dev
Input file - insurveyor requires BAM files coordinated sorted and index with MC and MQ tags, each line in input file should just be unique identifier that corresponds BAM/BAI in data directory.
Ensure reference fasta is indexed and in data directory. For convenience named the reference the same as the species study
Ensure GCF file (if interested) is in data directory
Config - data directory, output directory, reference location, input file, gcf file

## Running
Run insurveyor to get insertions
Look at output summary file to see if any bad samples should be removed 
Compile histogram from input file list with changes
Analyze histogram peak summary and histogram slides for target analysis ranges
  The pipeline will not filter based on size just similarity so its up to the user to pick suitable ranges 
getPopulationLoci with target histogram peak ranges



