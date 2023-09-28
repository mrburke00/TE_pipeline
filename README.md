# TE_pipeline

## Setup
clone this repo 
```
git clone git@github.com:mrburke00/TE_pipeline.git
```
insurveyor - if using clustering computing then singularity option is rec 

```
cd TE_pipeline
wget https://github.com/kensung-lab/INSurVeyor/releases/download/1.1.2/insurveyor.sif
```

ensure htslib is installed
```
sudo apt-get install autoconf zlib1g-dev
```
Config - data directory, output directory, reference location, input file, gcf file

Input file - insurveyor requires BAM files coordinated sorted and index with MC and MQ tags, each line in input file should just be unique identifier that corresponds BAM/BAI in data directory. Input file and data structure should appear like the following

```
config.yaml
  data_dir : "../TE_pipeline/data/"
  output_dir : "../TE_pipeline/output/"
  species : "horse"
```

```
data/
  /horse/
    horse_sraNumbers.txt
    horse.ref
    horse.ref.fai
    horse.gcf
    srr123.bam
    srr123.bam.bai
    srr456.bam
    srr456.bam.bai
```

```
horse_sraNumbers.txt
  srr123
  srr456
```

Ensure reference fasta is indexed and in data directory. For convenience named the reference the same as the species study

Ensure GCF file (if interested) is in data directory



## Running
Serial Run
Run insurveyor to get insertions

```
bash call_insurveyor.sh -s species -output output_dir -data data_dir
```

Parallel Run

note: requires gargs (https://github.com/brentp/gargs)

Calculate how many separate jobs you want to start as -p flag (will divide number of lines in sranumbers by p), also easily extendible to sbatch script 

```
bash spawn_insurveyor.sh -s species -p no_jobs -output output_dir -data data_dir
```

Look at output summary file to see if any bad samples should be removed 

Compile histogram from input file list with changes

Analyze histogram peak summary and histogram slides for target analysis ranges

  The pipeline will not filter based on size just similarity so its up to the user to pick suitable ranges 
  
getPopulationLoci with target histogram peak ranges

```
bash getPopulationLoci -s species -l lower_peak_bp -u upper_peak_bp
```




