Python Code Explanation
==============================



process_pdf.py
---------------


load_and_split_pdfs Function
______________________________
.. raw:: html


    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>load_and_split_pdfs</strong> function is responsible for loading the content of multiple PDF files and splitting them into smaller chunks. It accepts the following arguments: 
        <em>pdf_paths</em>, <em>chunk_size</em>, and <em>chunk_overlap</em>.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        First, the function initializes an empty list called <strong>documents</strong> to store the text extracted from the PDF files. It then iterates over each file path in the <em>pdf_paths</em> list.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        For each PDF file, it checks if the file exists using the <strong>os.path.exists()</strong> function. If the file does not exist, a <strong>FileNotFoundError</strong> is raised to inform the user.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        If the file exists, the function uses the <strong>PyPDFLoader</strong> from the <em>langchain</em> library to load the PDF's content. The loader extracts text from the file, and the resulting documents are appended to the <strong>documents</strong> list.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        After all PDF files are loaded, the function uses <strong>RecursiveCharacterTextSplitter</strong> to split the content into smaller chunks. The chunk size is controlled by the <em>chunk_size</em> parameter (default: 1000 characters), and overlapping text chunks are handled by the <em>chunk_overlap</em> parameter (default: 200 characters).
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        Finally, the function returns a list of split documents for further processing, such as summarization or translation.
    </i></span></p>

.. code-block:: python

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


Save_processing_results Function
____________________________________


.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>save_processing_results</strong> function saves the results from processing the PDF documents into a text file. It accepts a list of results and an optional file name for output.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The function opens the output file in write mode. It iterates over the <em>results</em> list, where each item represents the processed data for a document (e.g., summary, translation, or extracted emails).
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        For each document, the function writes the document number, its summary, translation, and any extracted emails. After each document's results, a separator line is added to ensure the results are clearly formatted.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        This function helps save the results from the PDF processing for later reference or review.
    </i></span></p>




.. code-block:: python

    def save_processing_results(results, output_file="results.txt"):
        with open(output_file, 'w') as f:
            for i, result in enumerate(results):
                f.write(f"Document {i + 1}:\n")
                f.write(f"Summary: {result['Summary']}\n")
                f.write(f"Translation: {result['Translation']}\n")
                f.write(f"Emails: {result['Emails']}\n")
                f.write("-" * 50 + "\n")

.. raw:: html

    <h2>Summary</h2>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        In summary, the <strong>load_and_split_pdfs</strong> function loads and processes PDF files by splitting their content into smaller text chunks. These chunks are easier to handle by language models for tasks such as summarization, translation, or question answering. The <strong>save_processing_results</strong> function stores the results in a text file, ensuring that the output of the processing is well-organized and accessible for later use.
    </i></span></p>


question_handler.py
-------------------

get_question_answer_chain Function
_____________________________________
.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>get_question_answer_chain</strong> function is responsible for setting up a chain to answer questions based on a given text. It takes one argument, <em>llm</em>, which represents the language model used to generate the answers.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        Inside the function, the <strong>question_answer_prompt</strong> is defined, containing a template where a question and a text are dynamically inserted. This template serves as a prompt for the language model.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>PromptTemplate</strong> class from <em>langchain</em> is used to create a template that takes two input variables: <em>question</em> and <em>text</em>. These variables are injected into the prompt when running the chain.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        Finally, the function returns an instance of <strong>LLMChain</strong>, which combines the language model and the question-answer prompt. This chain is ready to process inputs for answering questions.
    </i></span></p>

.. code-block:: python

    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain

    def get_question_answer_chain(llm):
        question_answer_prompt = """
        Answer the following question based on the provided text:
        Question: {question}
        Text: {text}
        """
        question_prompt_template = PromptTemplate(template=question_answer_prompt, input_variables=["question", "text"])
        return LLMChain(llm=llm, prompt=question_prompt_template)


answer_question Function
_________________________

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>answer_question</strong> function takes three arguments: <em>question_chain</em>, <em>question</em>, and <em>text</em>. This function runs the language model chain to generate an answer based on the provided question and text.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The function calls <strong>question_chain.run()</strong> with a dictionary containing the <em>question</em> and <em>text</em> as key-value pairs. The chain processes the input and returns an answer generated by the language model.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        This function is a simple interface that allows users to pass a question and corresponding text to the chain, obtaining a language model-generated answer.
    </i></span></p>

.. code-block:: python

    def answer_question(question_chain, question, text):
        return question_chain.run({"question": question, "text": text})


.. raw:: html

    <h2>Summary</h2>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        In summary, the <strong>get_question_answer_chain</strong> function creates a question-answering system by using a language model and a structured prompt. The <strong>answer_question</strong> function runs this chain by passing in a question and text, returning an answer generated by the model.
    </i></span></p>






summarizer.py
------------------

get_summary_chain Function
___________________________

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>get_summary_chain</strong> function creates a chain for summarizing a given text using a language model. It accepts one argument, <em>llm</em>, which stands for the language model responsible for generating summaries.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        Inside the function, a <strong>summary_prompt</strong> is defined as a template for summarization. The prompt asks the language model to summarize the provided text within a 100-word limit.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>PromptTemplate</strong> class from the <em>langchain</em> library is used to define the template, with <em>text</em> being the only input variable. This allows dynamic injection of different texts into the prompt.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The function returns an instance of <strong>LLMChain</strong>, which connects the language model with the summarization prompt. This chain can be used to generate concise summaries of input texts.
    </i></span></p>

.. code-block:: python

    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain

    def get_summary_chain(llm):
        summary_prompt = """
        Summarize the following text (maximum 100 words):
        Text: {text}
        """
        summary_prompt_template = PromptTemplate(template=summary_prompt, input_variables=["text"])
        return LLMChain(llm=llm, prompt=summary_prompt_template)


summarize_document Function
___________________________

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>summarize_document</strong> function runs the summarization chain to generate a summary for a given document. It accepts two arguments: <em>summary_chain</em>, which is the chain created using the <strong>get_summary_chain</strong> function, and <em>doc_content</em>, which is the content of the document to be summarized.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        This function calls the <strong>run()</strong> method of the <em>summary_chain</em>, passing the document's content as a dictionary with the <em>text</em> key. The chain processes the input and returns a summarized version of the document.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        By using this function, users can easily generate concise summaries of large documents, making the content easier to review or share.
    </i></span></p>

.. code-block:: python

    def summarize_document(summary_chain, doc_content):
        return summary_chain.run({"text": doc_content})


.. raw:: html

    <h2>Summary</h2>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        In summary, the <strong>get_summary_chain</strong> function sets up a summarization process using a language model, while the <strong>summarize_document</strong> function runs this process to generate summaries for any provided text. This approach helps users create concise and meaningful overviews of larger documents.
    </i></span></p>



translator.py
--------------

get_translation_chain Function
______________________________

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>get_translation_chain</strong> function creates a chain for translating text into English using a language model. It accepts one argument, <em>llm</em>, which stands for the language model responsible for the translation task.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        Inside the function, a <strong>translation_prompt</strong> is defined as a template. This prompt asks the language model to translate the provided text into English.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>PromptTemplate</strong> class from the <em>langchain</em> library is used to define the translation prompt template, with <em>text</em> being the only input variable. This allows different texts to be passed into the translation prompt dynamically.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The function returns an <strong>LLMChain</strong> that links the language model with the translation prompt. This chain will handle the translation task for any given text.
    </i></span></p>

.. code-block:: python

    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain

    def get_translation_chain(llm):
        translation_prompt = """
        Translate the following text into English:
        Text: {text}
        """
        translation_prompt_template = PromptTemplate(template=translation_prompt, input_variables=["text"])
        return LLMChain(llm=llm, prompt=translation_prompt_template)


translate_text Function
_______________________

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The <strong>translate_text</strong> function is responsible for translating a given piece of text using the translation chain created by the <strong>get_translation_chain</strong> function. It takes two arguments: <em>translation_chain</em>, which represents the translation model, and <em>text</em>, the content to be translated.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        The function calls the <strong>run()</strong> method of the <em>translation_chain</em>, passing the input text in a dictionary format with the <em>text</em> key. The model processes the input and returns the translated text.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        This function allows easy translation of any non-English text into English using a language model, making multilingual documents accessible.
    </i></span></p>

.. code-block:: python

    def translate_text(translation_chain, text):
        return translation_chain.run({"text": text})


.. raw:: html

    <h2>Summary</h2>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        In summary, the <strong>get_translation_chain</strong> function sets up the translation process using a language model, while the <strong>translate_text</strong> function leverages this chain to translate any text into English. This system is useful for translating multilingual documents into a common language for easier understanding and processing.
    </i></span></p>


