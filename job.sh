#!/bin/bash
#SBATCH --job-name=backmath
#SBATCH --output=backmath-%j.out
#SBATCH -p nvidia
#SBATCH --gres=gpu:a100:1
#Other SBATCH commands go here
#SBATCH -t 1-00:00:00
#SBATCH --mem=64GB

#Activating conda
source /share/apps/NYUAD/miniconda/3-4.11.0/bin/activate
conda activate lm-eval

lm_eval --model vllm \
	--model_args pretrained=Qwen/Qwen2.5-7B,max_gen_toks=4096 \
	--tasks backmath \
	--device cuda:0 \
	--batch_size auto \
	--log_samples \
	--output_path results \
	--wandb_args project=backmath,name=base-qwen \
	# --wandb_args project=mmlu-pro-plus-eval,name=base-open-reasoner-7b
