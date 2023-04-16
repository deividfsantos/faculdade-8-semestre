#!/bin/bash
#SBATCH --job-name=hello_world
#SBATCH --output=output.txt
#SBATCH --error=error.txt

echo "Hello, World!"
