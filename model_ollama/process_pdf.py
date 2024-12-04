# import os
# import streamlit as st
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# # Function to load and split PDFs into chunks
# def load_and_split_pdfs(pdf_paths, chunk_size=1000, chunk_overlap=200):
#     documents = []
    
#     for pdf_path in pdf_paths:
#         if not os.path.exists(pdf_path):
#             raise FileNotFoundError(f"The file {pdf_path} does not exist.")
        
#         loader = PyPDFLoader(pdf_path)
#         docs = loader.load()
#         documents.extend(docs)
    
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
#     return text_splitter.split_documents(documents)

# # Function to save the processing results
# def save_processing_results(results, output_file="results.txt"):
#     with open(output_file, 'w') as f:
#         for i, result in enumerate(results):
#             f.write(f"Document {i + 1}:\n")
#             f.write(f"Summary: {result.get('Summary', 'N/A')}\n")
#             f.write(f"Translation: {result.get('Translation', 'N/A')}\n")
#             f.write(f"Emails: {result.get('Emails', 'N/A')}\n")
#             f.write("-" * 50 + "\n")




import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Function to load and split a single PDF into chunks
def load_and_split_pdfs(pdf_paths, chunk_size=1000, chunk_overlap=200):
    documents = []

    for pdf_path in pdf_paths:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file {pdf_path} does not exist.")

        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        documents.extend(docs)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)

# Function to save the processing results
def save_processing_results(results, output_file="results.txt"):
    with open(output_file, 'w') as f:
        for i, result in enumerate(results):
            f.write(f"Document {i + 1}:\n")
            f.write(f"Summary: {result.get('Summary', 'N/A')}\n")
            f.write(f"Translation: {result.get('Translation', 'N/A')}\n")
            f.write(f"Emails: {result.get('Emails', 'N/A')}\n")
            f.write("-" * 50 + "\n")
