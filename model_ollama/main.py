import os
import streamlit as st
import tempfile
from concurrent.futures import ThreadPoolExecutor
from process_pdf import load_and_split_pdfs
from summarizer import get_summary_chain, summarize_document
from translator import get_translation_chain, translate_text
from question_handler import get_question_answer_chain, answer_question
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Custom CSS for styling
st.markdown("""
    <style>
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        .stSelectbox, .stTextInput, .stFileUploader {
            padding: 12px 20px;
            border-radius: 8px;
        }
        .stMarkdown h1 {
            color: #4CAF50;
            font-size: 36px;
        }
        .stMarkdown h2, .stMarkdown h3 {
            color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown("<h1>📝 Document Processing and Question Answering</h1>", unsafe_allow_html=True)

# Step 1: Organize layout with columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2>📂 Upload PDF(s)</h2>", unsafe_allow_html=True)
    pdf_files = st.file_uploader("Upload PDF(s)", accept_multiple_files=True, type=['pdf'], label_visibility="collapsed")

with col2:
    st.markdown("<h2>🔧 Choose Action</h2>", unsafe_allow_html=True)
    action = st.selectbox(
        "Choose the action you want to perform:",
        ("Summarize", "Translate", "Ask a Question", "Chat with PDF")
    )

    model_choice = st.selectbox(
        "Choose the model to use:",
        ("Llama 3.1", "Llama 2", "Mistral", "CodeLlama")
    )

    # Only show language options if "Translate" is selected
    if action == "Translate":
        target_language = st.selectbox(
            "Choose the language to translate to:",
            ("English", "French", "Arabic")
        )

# Initialize Ollama model based on user's selection
if model_choice == "Llama 3.1":
    llm = Ollama(model="llama3.1", base_url="http://localhost:11434")
elif model_choice == "Llama 2":
    llm = Ollama(model="llama2", base_url="http://localhost:11434")
elif model_choice == "Mistral":
    llm = Ollama(model="mistral", base_url="http://localhost:11434")
elif model_choice == "CodeLlama":
    llm = Ollama(model="codellama", base_url="http://localhost:11434")

# Step 2: Define the translation function with language choice
def get_translation_chain(llm, target_language):
    translation_prompts = {
        "English": "Translate the following text into English:\nText: {text}",
        "French": "Traduisez le texte suivant en français :\nTexte : {text}",
        "Arabic": "ترجم النص التالي إلى العربية:\nالنص: {text}"
    }
    translation_prompt = translation_prompts[target_language]
    translation_prompt_template = PromptTemplate(template=translation_prompt, input_variables=["text"])
    return LLMChain(llm=llm, prompt=translation_prompt_template)

def translate_text(translation_chain, text):
    return translation_chain.run({"text": text})

# Step 3: Define chat with PDF functionality
def chat_with_pdf(llm, doc_content, question):
    question_prompt_template = PromptTemplate(template="Answer the question based on the document content: {text}\nQuestion: {question}", input_variables=["text", "question"])
    chat_chain = LLMChain(llm=llm, prompt=question_prompt_template)

    response = chat_chain.run({"text": doc_content, "question": question})
    return response

# Step 4: Process PDFs

if pdf_files:
    st.markdown("<h2>🛠 Processing PDFs...</h2>", unsafe_allow_html=True)

    pdf_paths = []
    with tempfile.TemporaryDirectory() as temp_dir:
        # Give users an option to select specific PDFs
        st.markdown("<h3>Select PDFs to process:</h3>", unsafe_allow_html=True)
        selected_pdfs = [pdf_file for pdf_file in pdf_files if st.checkbox(pdf_file.name)]

        if not selected_pdfs:
            st.warning("Please select at least one PDF to process.")
        else:
            for pdf_file in selected_pdfs:
                temp_pdf_path = f"{temp_dir}/{pdf_file.name}"
                with open(temp_pdf_path, "wb") as f:
                    f.write(pdf_file.read())
                pdf_paths.append(temp_pdf_path)

            # Load and split PDFs into chunks
            docs = load_and_split_pdfs(pdf_paths)
            doc_content = " ".join([doc.page_content for doc in docs])

            # Initialize LLM Chains
            summary_chain = get_summary_chain(llm)
            question_answer_chain = get_question_answer_chain(llm)
            translation_chain = None
            if action == "Translate":
                translation_chain = get_translation_chain(llm, target_language)

            # Handle different actions
            if action == "Summarize":
                st.markdown("<h2>📄 Document Summary</h2>", unsafe_allow_html=True)
                summary = summarize_document(summary_chain, doc_content)
                st.markdown(f"**Summary**: {summary}")

            elif action == "Translate":
                if translation_chain:
                    st.markdown("<h2>🌍 Translated Text</h2>", unsafe_allow_html=True)
                    translation = translate_text(translation_chain, doc_content)
                    st.markdown(f"**Translation**: {translation}")
                else:
                    st.error("Translation chain could not be initialized.")

            elif action == "Ask a Question":
                st.markdown("<h2>❓ Ask a Question</h2>", unsafe_allow_html=True)
                question = st.text_input("Ask a question about the document:")
                if question:
                    answer = answer_question(question_answer_chain, doc_content, question)
                    st.markdown(f"**Answer**: {answer}")

            elif action == "Chat with PDF":
                # Chat interface for continuous questions
                chat_history = []

                st.markdown("<h2>💬 Chat with PDF</h2>", unsafe_allow_html=True)
                chat_container = st.container()

                def display_chat():
                    """Function to render the chat messages dynamically."""
                    with chat_container:
                        for i, chat_entry in enumerate(chat_history):
                            st.markdown(f"**You**: {chat_entry['question']}")
                            st.markdown(f"**Response**: {chat_entry['response']}")

                # Input and processing
                while True:
                    question = st.text_input("Ask a question to the document:")
                    if question:
                        response = chat_with_pdf(llm, doc_content, question)
                        chat_history.append({"question": question, "response": response})
                        display_chat()
                    st.button("Submit")
                    st.stop()  # Pausing execution to ensure continuous question flow

            else:
                st.warning("Please select a valid action to proceed.")
