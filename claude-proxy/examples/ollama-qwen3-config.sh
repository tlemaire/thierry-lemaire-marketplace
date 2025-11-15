#!/bin/bash

# Ollama configuration for qwen3-coder:30b
# Usage: ./ollama-qwen3-config.sh

echo "Starting Ollama with qwen3-coder:30b..."

# Start Ollama service
ollama serve

echo "Ollama started"
echo "Model available: qwen3-coder:30b"
echo "API endpoint: http://localhost:11434"