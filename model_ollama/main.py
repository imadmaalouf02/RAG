import streamlit as st
import tempfile
from concurrent.futures import ThreadPoolExecutor
from process_pdf import load_and_split_pdfs
from summarizer import get_summary_chain, summarize_document
from translator import get_translation_chain, translate_text
from question_handler import get_question_answer_chain, answer_question
from langchain_community.llms import Ollama

# Custom CSS for styling
st.markdown("""
    <style>
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        .stSelectbox {
            padding: 12px 20px;
            border-radius: 8px;
        }
        .stTextInput {
            padding: 12px 20px;
            border-radius: 8px;
        }
        .stFileUploader {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 12px;
        }
        .stMarkdown h1 {
            color: #4CAF50;
            font-size: 36px;
        }
        .stMarkdown h2 {
            color: #4CAF50;
            font-size: 28px;
        }
        .stMarkdown h3 {
            color: #4CAF50;
            font-size: 24px;
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
        ("Summarize", "Translate", "Ask a Question")
    )

    model_choice = st.selectbox(
        "Choose the model to use:",
        ("Llama 3.1", "Llama 2", "Mistral", "CodeLlama")
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

# Step 3: Process if PDFs are uploaded
if pdf_files:
    st.markdown("<h2>🛠 Processing PDFs...</h2>", unsafe_allow_html=True)

    pdf_paths = []
    with tempfile.TemporaryDirectory() as temp_dir:
        for pdf_file in pdf_files:
            temp_pdf_path = f"{temp_dir}/{pdf_file.name}"
            with open(temp_pdf_path, "wb") as f:
                f.write(pdf_file.read())
            pdf_paths.append(temp_pdf_path)

        # Load and split PDFs into chunks
        docs = load_and_split_pdfs(pdf_paths)

        # Initialize LLM Chains
        summary_chain = get_summary_chain(llm)
        translation_chain = get_translation_chain(llm)
        question_chain = get_question_answer_chain(llm)

        # Get user question for "Ask a Question" option
        question = None
        if action == "Ask a Question":
            question = st.text_input("Enter your question here:")

        # Process document in a background thread
        def process_document(doc):
            try:
                if action == "Summarize":
                    summary = summarize_document(summary_chain, doc.page_content)
                    return {"Result": summary}
                elif action == "Translate":
                    summary = summarize_document(summary_chain, doc.page_content)
                    translation = translate_text(translation_chain, summary)
                    return {"Result": translation}
                elif action == "Ask a Question" and question:
                    answer = answer_question(question_chain, question, doc.page_content)
                    return {"Result": answer}
                else:
                    return {"Result": "No valid input provided."}
            except Exception as e:
                return {"Result": f"Error: {str(e)}"}

        if st.button("Process Documents"):
            st.markdown("<h2>🔄 Processing in Background...</h2>", unsafe_allow_html=True)
            with st.spinner('Please wait while we process the documents...'):
                with ThreadPoolExecutor() as executor:
                    results = list(executor.map(process_document, docs))

            # Step 4: Display results in an expander
            for i, result in enumerate(results):
                with st.expander(f"Document {i + 1} - Result"):
                    st.write(result["Result"])
