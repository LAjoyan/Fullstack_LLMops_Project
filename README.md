# 📚 Study Buddy RAG – Fullstack LLMOps Project

## 📌 Overview
This project is a fullstack Retrieval-Augmented Generation (RAG) system designed to help students interact with lecture material more effectively.

The system uses lecture transcriptions as its knowledge base. It retrieves relevant information and generates answers using a large language model based on that context. The goal is to provide accurate responses while also showing the source of the information.

The project is developed collaboratively and follows a structured workflow using Git branches.

## 🧠 Key Features
- Retrieval-Augmented Generation (RAG) pipeline
- Lecture-based question answering
- Source-aware responses
- Modular and scalable architecture

## ⚙️ Technologies Used
- Python 3.13
- uv (package manager)
- LanceDB (vector database)
- OpenRouter (LLM access)
- Pydantic-AI

## 🏗️ Project Structure

```
fullstack-llmops-project/
├── backend/              # RAG logic, LLM interaction
│   ├── constants.py
│   └── pyproject.toml
│
├── frontend/             # UI (Streamlit will be added soon)
│   └── pyproject.toml
│
├── data/                 # Lecture transcripts (RAG source)
│
├── setup/                # Ingestion & vector DB setup
│   └── ingestion.py
│
├── monitoring/           # MLflow (planned)
│
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml        # Root config (no dependencies)
├── uv.lock
├── README.md
└── way_of_working.md
```

## 📦 Project Configuration

This project uses **separate `pyproject.toml` files** for the backend and frontend.

This approach allows:
- Independent dependency management for each part of the system
- Clear separation of concerns
- Better scalability as the project grows
- A structure similar to real-world fullstack and ML systems

The root `pyproject.toml` only contains general project metadata and does not manage dependencies.

