#!/bin/bash
#SBATCH -p long # Partition or queue. In this case, short!
#SBATCH --job-name=devin_slurm_test # Job name
#SBATCH --mail-type=ALL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=debu7497@colorado.edu
#SBATCH --nodes=1 # Only use a single node
#SBATCH --ntasks=16 # Run on a single CPU
#SBATCH --mem=64gb # Memory limit
#SBATCH --time=48:00:00 # Time limit hrs:min:sec
#SBATCH --output=/scratch/Shares/layer/workspace/devin_sra/TE_pipeline/log_seq/slurm_run_%j.out
#SBATCH --error=/scratch/Shares/layer/workspace/devin_sra/TE_pipeline/log_seq/slurm_run_%j.err # %j inserts job number
pwd; hostname; date

python clusterSequences.py -l 240 -u 260 -s horse

sleep 20
date

