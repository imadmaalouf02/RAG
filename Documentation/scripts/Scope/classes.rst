Python Code Explanation
==============================

load_and_split_pdfs Function
-----------------------------
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

    <div class="code-block">
        <strong>Code Snippet:</strong>
        <pre>
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
        </pre>
        </div>

Save_processing_results Function
--------------------------------


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

    <div class="code-block">
        <strong>Code Snippet:</strong>
        <pre>
    def save_processing_results(results, output_file="results.txt"):
        with open(output_file, 'w') as f:
            for i, result in enumerate(results):
                f.write(f"Document {i + 1}:\n")
                f.write(f"Summary: {result['Summary']}\n")
                f.write(f"Translation: {result['Translation']}\n")
                f.write(f"Emails: {result['Emails']}\n")
                f.write("-" * 50 + "\n")
            </pre>
    </div>

    <h2>Summary</h2>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
        In summary, the <strong>load_and_split_pdfs</strong> function loads and processes PDF files by splitting their content into smaller text chunks. These chunks are easier to handle by language models for tasks such as summarization, translation, or question answering. The <strong>save_processing_results</strong> function stores the results in a text file, ensuring that the output of the processing is well-organized and accessible for later use.
    </i></span></p>