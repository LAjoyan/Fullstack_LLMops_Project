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

## 🔄 Planned System Workflow (RAG Pipeline)

1. **Data Ingestion**
   - Lecture transcripts are stored in the `data/` folder
   - The ingestion script prepares and initializes the vector database

2. **Vector Storage**
   - Text is embedded using a multilingual embedding model
   - Embeddings are stored in LanceDB for similarity search

3. **User Query**
   - The user submits a question through the frontend interface

4. **Retrieval**
   - Relevant text chunks are retrieved from the vector database

5. **Generation**
   - The LLM (via OpenRouter) generates an answer using the retrieved context

6. **Output**
   - The system returns the answer along with its source

## 🚀 Installation & Setup (In Progress)

Detailed setup instructions will be added as the project is completed.

## 🔐 Environment Variables

Create a `.env` file and add your API key:

```
OPENROUTER_API_KEY=your_key_here
COHERE_API_KEY=your_key_here
```

## 🌿 Branching Strategy

We use a simple branching workflow to collaborate on the project.

- `main` → stable version of the project
- separate branches → used by each team member for development

Each team member works on their own branch. Changes are reviewed and tested before being merged into the `main` branch.

All changes are merged through pull requests.

## 🤝 Collaboration
This project is developed collaboratively by a team of four students. Each member works on separate branches to ensure structured collaboration and clear version control.

### Team Members

- [Lilit Ajoyan](https://www.linkedin.com/in/lilit-ajoyan-1565b4183/)
- [Josefin Lesley](https://www.linkedin.com/in/josefin-l-490ab038b/)
- [Erfan Tahmasebi](https://www.linkedin.com/in/erfan-tahmasebi-b41276290/)
- [Leo Lindqvist](https://www.linkedin.com/in/leo-lindqvist-kr%C3%B6hnert-bb0a2b1b5/)

