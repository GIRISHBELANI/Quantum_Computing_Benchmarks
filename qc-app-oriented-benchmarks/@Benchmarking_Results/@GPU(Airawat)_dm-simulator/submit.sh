#!/bin/bash
#SBATCH --job-name=dm_gpu_benchmarks
#SBATCH --partition=testp
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=128           # Reserve 128 CPUs for multiprocessing
#SBATCH --gres=gpu:A100-SXM4:2                 # Request 2 GPU
##SBATCH --mem=300GB                  # 300 GB of memory
#SBATCH --time=2:00:00              # Time limit, will take default time limit if not mentioned
#SBATCH --output=dm_gpu_benchmarks_%j.log
#SBATCH --error=dm_gpu_benchmarks_%j.log

source /nlsasfs/home/qntmacl/vivekn/wrkzubair/miniconda3/bin/activate
conda activate terra_upg_gpu
python script_dm_noisefree_gpu_bkp.py

