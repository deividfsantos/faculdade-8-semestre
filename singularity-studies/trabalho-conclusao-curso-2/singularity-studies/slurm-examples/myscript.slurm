#!/bin/bash
#SBATCH --job-name=meujob
#SBATCH --output=output.txt
#SBATCH --error=error.txt
#SBATCH --ntasks=1
#SBATCH --time=00:01:00
#SBATCH --partition=normal

module load python

srun python3 myscript.py
