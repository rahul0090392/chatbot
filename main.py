import os

import streamlit as st
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from PyPDF2 import PdfReader

# Get OpenAI API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.header("📄 Chat with Your PDF")

with st.sidebar:
    st.title("Upload Your Document")
    file = st.file_uploader("Upload a PDF file to start asking questions", type="pdf")

# Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = "\n".join(page.extract_text() or "" for page in pdf_reader.pages)

    # Improved Text Chunking
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", "?"],  # Prioritizing logical sentence breaks
        chunk_size=800,  # Reduced chunk size for better retrieval
        chunk_overlap=300,  # Increased overlap to retain context across chunks
        length_function=len,
    )
    chunks = text_splitter.split_text(text)

    # Generate embeddings
    embeddings = OpenAIEmbeddings()

    # Create vector store - FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get user question
    user_question = st.text_input("🔎 Ask a question based on the document")

    # Perform similarity search and get the answer
    if user_question:
        retriever = vector_store.as_retriever(
            search_kwargs={"k": 5}
        )  # Retrieve top 5 most relevant chunks
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(
                model="gpt-4", temperature=0
            ),  # Upgraded to GPT-4 for better responses
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,  # Returns the retrieved chunks along with the response
        )

        response = qa_chain(user_question)

        # Display AI-generated answer
        st.subheader("💡 Answer:")
        st.write(response["result"])

        # Show source text for transparency
        with st.expander("📚 See Retrieved Context"):
            for doc in response["source_documents"]:
                st.write(doc.page_content)
