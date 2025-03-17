# 🤖 Chatbot with PDF Q&A

This repository contains a **Streamlit-based chatbot** that allows users to upload PDF documents and ask questions based on their content. It utilizes **LangChain, FAISS, and OpenAI's GPT models** to extract relevant information and generate responses.

---

## 🏗️ Architecture

![Architecture](https://github.com/user-attachments/assets/64636143-8fe5-43f7-aa66-bc3f9d42345e)

The system follows a **Retrieval-Augmented Generation (RAG)** approach:
1. **PDF Processing**: Extracts text from the uploaded PDF.
2. **Chunking & Embedding**: Splits text into chunks and converts them into embeddings using OpenAI.
3. **Vector Storage**: Stores embeddings in FAISS for efficient retrieval.
4. **User Query Processing**: Matches user queries with stored chunks and generates responses using GPT.

---

## 🚀 Features
✅ Upload and process PDFs  
✅ Chunk text intelligently for better context  
✅ Use FAISS for fast similarity search  
✅ Answer questions using GPT-3.5/4  
✅ Interactive UI with Streamlit  

---

## 📦 Installation

1️⃣ Clone the repository:
```sh
git clone https://github.com/rahul0090392/chatbot.git
cd chatbot
```

2️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

3️⃣ Set your **OpenAI API Key**:
```sh
export OPENAI_API_KEY="your_openai_api_key"
```

4️⃣ Run the chatbot:
```sh
streamlit run main.py
```

---

## ⚡ Usage
1. Upload a **PDF** via the sidebar.
2. Type your question in the text box.
3. Get an AI-powered answer instantly!

---

## 🛠️ Tech Stack
- **Python** 🐍
- **Streamlit** 🎨 (UI Framework)
- **PyPDF2** 📄 (PDF Processing)
- **LangChain** 🔗 (AI Orchestration)
- **FAISS** 📚 (Vector Search)
- **OpenAI GPT** 🤖 (LLM Model)

---

## 📝 To-Do
- [ ] Add support for multiple PDFs
- [ ] Improve UI/UX
- [ ] Optimize chunking strategy

---

## 🤝 Contributing
Feel free to **fork the repo** and submit PRs. Suggestions and improvements are always welcome!

---

## 📬 Contact
📧 Email: [rahul0090392@gmail.com](mailto:rahul0090392@gmail.com)  
🔗 GitHub: [rahul0090392](https://github.com/rahul0090392)

---

