
# 🤖 AgentPDFX

**AgentPDFX** is an intelligent document understanding agent powered by LLMs and Retrieval-Augmented Generation (RAG).  
It lets you upload a PDF(WIP) and ask questions about its content using natural language. Powered by [Agno](https://docs.agno.com), [Ollama](https://ollama.com), and optional OpenAI.

---

## 🚀 Features

- 💡 Agentic RAG pipeline built with [Agno](https://docs.agno.com)
- 📄 PDF ingestion and chunking with built-in tools
- 🔍 Vector-based semantic search using [ChromaDB](https://www.trychroma.com/)
- 🧠 Embedding via **Ollama (local)** or **OpenAI (cloud)**
- 🖥️ Interactive CLI for querying your documents
- 🧪 Clean project structure with `src/` layout and Poetry environment

---

## 📁 Example PDF

For testing, you can use this example document:

📄 [ThaiRecipes.pdf](https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf)  
(You can download and save it under `src/agentpdfx/data/sample.pdf`)

---

## 🧑‍💻 Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/agentpdfx.git
cd agentpdfx
````

### 2. Install dependencies with Poetry

```bash
poetry install
```

### 3. Setup environment variables

Create a `.env` file in the root (next to `pyproject.toml`):

```env
USE_OLLAMA=true
OLLAMA_URL=http://localhost:11434
OPENAI_API_KEY=your-openai-api-key
MODEL_ID=mxbai-embed-large
```

> Use `USE_OLLAMA=false` to switch to OpenAI embedding/model instead.

### 4. Download a sample PDF

```bash
curl -o src/agentpdfx/data/sample.pdf https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf
```

### 5. Run the agent

```bash
PYTHONPATH=src poetry run python agentpdfx/main.py
```

---

## 🧠 Example Interaction

```
✅ AgentPDFX is ready. Ask your question!
🧠 You: What ingredients are used in the Pad Thai recipe?
🤖 AgentPDFX:
- Rice noodles
- Tamarind paste
- Fish sauce
- Eggs
...
```

---

## 🛠 Tech Stack

* 🧱 **Python 3.10+**
* 🧠 [Agno](https://docs.agno.com) – agent framework
* 💾 [ChromaDB](https://www.trychroma.com) – vector storage
* 🔡 [Ollama](https://ollama.com) – local LLMs and embedding models
* ⚙️ [Poetry](https://python-poetry.org/) – dependency management
* ✍️ [Pydantic](https://docs.pydantic.dev/) – configuration and data modeling
* 🐍 \[FastAPI (optional)] – if you plan to expose the agent via API later

---

## 🧪 Project Structure

```
AgentPDFX/
├── pyproject.toml
├── .env
├── src/
│   └── agentpdfx/
│       ├── main.py
│       ├── agent.py
│       ├── config.py
│       ├── knowledge_base.py
│       └── data/
│           └── sample.pdf
```

---

## 📦 Future Improvements

* [ ] Add FastAPI interface
* [ ] Streamlit front-end for document Q\&A
* [ ] Multi-document support
* [ ] pgVector support for production vector DB

---

## 📄 License

MIT License – Use freely and credit if you build on top of it 🙏

---

## 🙌 Acknowledgments

* [Agno AI Framework](https://docs.agno.com)
* [Ollama](https://ollama.com)
* [Thai Recipes PDF](https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf) courtesy of Agno

