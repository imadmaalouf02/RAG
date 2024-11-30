
What is Retrieval-Augmented Generation (RAG)?
---------------------------------------------
.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>  
    RAG is a method that combines information retrieval with text generation. The model retrieves relevant information from documents and uses a language model to answer questions, summarize, or translate the information, helping provide responses grounded in facts.

    </i></span></p>

Step-by-Step Breakdown:
--------------------------

Libraries and Tools Required:
______________________________

.. raw:: html
    
    <p style="text-align: justify;">
    <Str>Streamlit:</Str> 
    <span style="color:#000080;"><i>  This is a Python framework to create interactive web applications. It is used here to create the user interface (UI) where users can upload documents, choose actions, and interact with the app.
    </i></span></p>

.. raw:: html
     
    <p style="text-align: justify;">
    <St>LangChain:</St>
    <span style="color:#000080;"><i>  LangChain is a library designed to facilitate the creation of applications that integrate language models (like Llama, Mistral, etc.) with external data such as documents.
    </i></span></p>

.. raw:: html
    
    <p style="text-align: justify;">
    <s>Ollama:<s> 
    <span style="color:#000080;"><i> A specific library used to run different language models (Llama 3.1, Llama 2, Mistral, and CodeLlama) for generating text, answering questions, translating, and summarizing.
    </i></span></p>
    




Streamlit Application Structure
------------------------------------------------
.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    The app uses Streamlit to create a user-friendly interface. It consists of several steps:
    </i></span></p>


UI Components
-------------
.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    - Users upload PDFs using a file uploader.
    </i></span></p>

    
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    - They choose the action (Summarize, Translate, or Ask a Question).
    </i></span></p>

    
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    - They select a language model to use (Llama 3.1, Llama 2, Mistral, or CodeLlama).
    </i></span></p>


Back-End Processing
-------------------

.. raw:: html
    
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    After the user uploads PDFs and selects an action, the app processes the documents using background threads.
    The document content is summarized, translated, or used to answer questions, depending on the user's choice.
    </i></span></p>


Explanation of Code
----------------=========

- **CSS Styling**: Adds visual styles to the app's buttons, text inputs, and other elements to enhance the user experience.
- **File Uploader**: ``pdf_files = st.file_uploader()`` allows the user to upload multiple PDFs.
- **Action Selection**: The user selects what they want to do (Summarize, Translate, Ask a Question) using ``st.selectbox()``.

Document Processing
----------------=========
.. raw:: html

    
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    After uploading, the app reads the PDF documents and processes them. This is done using the `process_pdf.py` file:
    </i></span></p>

- **load_and_split_pdfs**: This function loads and splits PDFs into manageable text chunks. For example, a large document is divided into smaller pieces (chunks) to process more efficiently.
- **RecursiveCharacterTextSplitter**: Used to split the text into smaller pieces so that language models can handle them better. This is important because models can have token limits.
.. raw:: html

    
    <p style="text-align: justify;"><span style="color:red;"><i>     
    Functions in Process_PDF:
    </i></span></p>

- **load_and_split_pdfs**: Loads the PDF and divides it into text chunks based on ``chunk_size`` (default 1000 characters) and overlap.
- **save_processing_results**: Saves the results (summary, translation, or extracted answers) in a text file.

The RAG Models
----------------
.. raw:: html

    
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    The app uses four language models via **Ollama**:
    </i></span></p>

- Llama 3.1
- Llama 2
- Mistral
- CodeLlama
.. raw:: html

    
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    These models perform text generation tasks such as summarization, translation, and answering questions based on the PDF content. The app switches between them based on the user's selection.
    </i></span></p>


Chain Functions (How the Actions Work)
------------------------------------------------

- **Summarization**:
  - **get_summary_chain**: Sets up a summarization chain using a prompt asking the model to summarize text.
  - **summarize_document**: This function runs the summarization on a given chunk of text.
  
- **Translation**:
  - **get_translation_chain**: Creates a translation chain that translates the given text into English.
  - **translate_text**: Runs the translation on a chunk of text.

- **Question Answering**:
  - **get_question_answer_chain**: Prepares a prompt for answering questions based on the content of the text.
  - **answer_question**: Runs the language model to answer the user’s question based on the provided document text.

Background Processing
--------------------------------=

The app uses the **ThreadPoolExecutor** to process each document chunk in parallel, speeding up the overall operation when dealing with large or multiple PDFs. This is important because it prevents the app from freezing while processing multiple files.

Displaying Results
----------------========

After the background processing is complete, the results (summaries, translations, or answers) are displayed using **st.expander**, where users can view each document's processed result.

Summary of Each Part
--------------------------------

- **Streamlit UI**: Provides an interactive interface for users to upload documents and choose actions.
- **Ollama Models**: Executes tasks like summarization, translation, and question answering using different language models (Llama, Mistral, etc.).
- **LangChain Chains**: Handles specific tasks like summarization, translation, and question answering by setting up appropriate chains with language models.
- **PDF Processing**: Loads the PDF documents, splits them into manageable chunks, and processes them in parallel for faster performance.

Differences Between Models
--------------------------------======

- **Llama 3.1 vs. Llama 2**: Llama 3.1 is an updated version with improved accuracy and capabilities compared to Llama 2.
- **Mistral**: Another advanced model, typically more lightweight and faster, though sometimes at the cost of depth in understanding.
- **CodeLlama**: Specialized in generating and working with code, useful for technical document translation and summarization.

Conclusion
----------------

In summary, this app provides a user-friendly interface to process documents with various tasks, combining the power of RAG with different advanced language models through an interactive Streamlit app.
