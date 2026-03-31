#!/bin/bash

# Ensure we're in the right directory
cd "$(dirname "$0")"

echo "Installing backend dependencies..."
pip install -r backend/requirements.txt

echo "Running ingestion pipeline..."
python backend/rag/ingest.py

echo "Starting Ask Chipathon Chatbot..."
python backend/cli_chat.py
