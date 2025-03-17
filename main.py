import os

import streamlit as st
from langchain.chains import RetrievalQA  # Use RetrievalQA instead of load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import (  # Use langchain_openai instead of langchain_community
    ChatOpenAI,
    OpenAIEmbeddings,
)
from PyPDF2 import PdfReader

# Get OpenAI API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Upload PDF files
st.header("My first Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = "".join(page.extract_text() or "" for page in pdf_reader.pages)

    # Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_text(text)

    # Generate embeddings
    embeddings = OpenAIEmbeddings()

    # Create vector store - FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get user question
    user_question = st.text_input("Type your question here")

    # Perform similarity search and get the answer
    if user_question:
        retriever = vector_store.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
            chain_type="stuff",
            retriever=retriever,
        )
        response = qa_chain.run(user_question)
        st.write(response)
