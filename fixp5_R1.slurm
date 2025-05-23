#!/bin/bash
#SBATCH --job-name=fix_p5_headers
#SBATCH --output=fix_p5_headers_%j.out
#SBATCH --error=fix_p5_headers_%j.err
#SBATCH --time=68:00:00            # Adjust as needed
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G                   # Enough for streaming reads
#SBATCH --nice=100              # Be extra nice on priority
#SBATCH --partition=htc-el8     # Or use your cluster's default/low priority queue
#SBATCH --mail-type=END,FAIL

# Activate environment if needed (optional)
# source activate your-env

echo "Starting header fix on R1..."
python ~/fix_aviti_fastq_headers.py Undetermined_S0_R1_001.fastq.gz Undetermined_S0_R1_001.fixed.fastq.gz

echo "Done."
