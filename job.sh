#!/bin/bash
#SBATCH --job-name=open-reasoner-7b-mmlu
#SBATCH --output=open-reasoner-%j.out
#SBATCH -p nvidia
#SBATCH --gres=gpu:a100:1
#Other SBATCH commands go here
#SBATCH -t 1-00:00:00
#SBATCH --mem=64GB

#Activating conda
source /share/apps/NYUAD/miniconda/3-4.11.0/bin/activate
conda activate lm-eval

lm_eval --model vllm \
	--model_args pretrained=Open-Reasoner-Zero/Open-Reasoner-Zero-7B,max_gen_toks=10000 \
	--tasks mmlu_pro_plus \
	--device cuda:0 \
	--batch_size auto \
	--show_config \
	--log_samples \
	--output_path results \
	--wandb_args project=mmlu-pro-plus-eval,name=base-open-reasoner-7b
