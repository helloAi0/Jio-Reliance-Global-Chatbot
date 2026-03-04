# Jio-Reliance-Global-Chatbot 🤖

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://langchain.com/)

An enterprise-grade, unified RAG (Retrieval-Augmented Generation) chatbot designed to provide seamless customer support across the Reliance ecosystem, including **Jio Mobile, Jio Fiber, and Jio Mart.**

## 🌟 Key Features
* **Multi-Domain Intelligence:** Unified vector search across different business unit datasets.
* **Hybrid RAG Architecture:** Combines FAISS vector indexing with Gemini 3 Flash for high-accuracy responses.
* **Context-Aware UI:** Built with Streamlit's modern chat interface and session state management.
* **Metadata Tagging:** Automatically identifies which department (Mobile/Fiber/Mart) the information originated from.

## 🛠️ Tech Stack
* **LLM:** Google Gemini 3 Flash Preview
* **Embeddings:** Google `gemini-embedding-001`
* **Orchestration:** LangChain / LangChain-Classic
* **Vector Store:** FAISS (Facebook AI Similarity Search)
* **Frontend:** Streamlit

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* A Google AI Studio API Key

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/helloAi0/Jio-Reliance-Global-Chatbot.git](https://github.com/helloAi0/Jio-Reliance-Global-Chatbot.git)
   cd Jio-Reliance-Global-Chatbot