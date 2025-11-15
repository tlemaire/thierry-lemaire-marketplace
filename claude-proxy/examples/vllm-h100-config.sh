#!/bin/bash

# vLLM configuration for 4x H100 with Qwen3-Next
# Usage: ./vllm-h100-config.sh

echo "Starting vLLM with Qwen3-Next on 4x H100..."

export CUDA_VISIBLE_DEVICES=0,1,2,3
export NCCL_DEBUG=WARN

python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen3-Next \
  --host 0.0.0.0 \
  --port 8000 \
  --trust-remote-code \
  --tensor-parallel-size 4 \
  --gpu-memory-utilization 0.95 \
  --max-model-len 32768 \
  --max-num-seqs 256 \
  --enable-prefix-caching

echo "vLLM started on http://localhost:8000"