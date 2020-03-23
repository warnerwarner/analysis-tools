#!/bin/bash
#
#SBATCH --job-name=kilosort2
#SBATCH --array=1		## N_TASKS_TOTAL: SET THIS TO THE NUMBER OF INDEPENDENT JOBS,TYPICLLAY 100,SEE BELOW N_TASKS_TOTAL
#SBATCH --output=/home/camp/warnert/analysis-tools/Python3/combining_out.txt	##
#SBATCH --error=/home/camp/warnert/analysis-tools/Python3/combining_error.txt
#SBATCH --ntasks=1
#SBATCH --time=24:00:00
#SBATCH --mem=200G
#SBATCH --partition=cpu


python combined_recordings.py