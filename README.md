# 🚀 Chipathon AI Knowledge Hub: Ask Chipathon Chatbot

A high-performance, modular AI powerhouse for OpenROAD-based physical design documentation. This project features a built-in RAG (Retrieval-Augmented Generation) chatbot and a Docusaurus-based document hub.

---

## 🛠️ Project Components

-   **Documentation Hub (Frontend):** A Docusaurus site serving as the structured "Source of Truth" for OpenROAD wikis.
-   **Ask Chipathon (Backend):** A Python-powered RAG assistant that retrieves context from documentation and generates cited answers using OpenAI/LLMs.
-   **Ingestion Pipeline:** A CLI utility to chunk, embed, and store technical markdown files in a localized ChromaDB vector store.

---

## 🏗️ Folder Structure

```text
chipathon-ai-hub/
├── .env.example          # Environment variable template
├── README.md             # This document
├── run.sh                # (optional) Automation script
│
├── backend/              # 🔥 Python RAG Backend
│   ├── cli_chat.py      # Main Chatbot interface
│   ├── config.py         # Config management (dotenv)
│   ├── requirements.txt  # Project dependencies
│   ├── db/               # Local Vector Database (Chroma)
│   └── rag/              # Core Logic
│       ├── ingest.py     # Document loader & injector
│       ├── retriever.py  # Similarity Search logic
│       ├── llm.py        # LLM Wrapper (Prompts & Citations)
│       └── utils.py      # Logging & helper functions
│
└── frontend/             # 🌐 Docusaurus Documentation
    ├── docs/             # Markdown source files (OpenROAD, RTL-to-GDSII, etc.)
    ├── docusaurus.config.js # Frontend configuration
    └── ...
```

---

## ⚙️ Local Setup Guide

### 1. Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **Active OpenAI API Key**

### 2. Implementation Steps

#### Step A: Environment Configuration
Copy the example environment file and add your OpenAI API Key:
```powershell
cp .env.example .env
# Open .env and add: OPENAI_API_KEY=your-key-here
```

#### Step B: Backend Initialization
```powershell
# Navigate to backend
cd backend

# Install dependencies (use python -m pip to avoid path issues)
python -m pip install -r requirements.txt

# Return to root and set PYTHONPATH
cd ..
$env:PYTHONPATH="."

# Build the Vector Database (Ingest documents)
python backend/rag/ingest.py

# Start the Chatbot CLI
python backend/cli_chat.py
```

#### Step C: Frontend Documentation Site
```powershell
# Navigate to frontend
cd frontend

# Install Node modules
npm install

# Start the dev server (Live at http://localhost:3000)
npm start
```

---

## 🤖 Example Queries
Once the chatbot is live, you can ask specialized hardware design questions:
- *"Explain the RTL to GDSII flow in the context of OpenROAD."*
- *"What are the key components of the OpenROAD project?"*
- *"How do congestion and timing metrics impact the physical layout?"*
- *"What are the common challenges for Chipathon participants?"*

---

## 🧩 Architectural Features
- **Semantic Retrieval:** Uses high-dimensional vector embeddings for advanced context matching.
- **Strict Prompting:** The chatbot only answers using provided context to prevent hallucinations.
- **Modern UI:** Uses the `rich` library for beautiful terminal output.
- **Persistence:** Local ChromaDB store ensures the system works offline once data is ingested.

---

## 📜 License
This project is open-source and intended to support the global Chipathon and OpenROAD ecosystem.
