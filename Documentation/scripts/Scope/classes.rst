Python Code Explanation
==============================

load_and_split_pdfs Function
-----------------------------
.. raw:: html


 <p>
        The <strong>load_and_split_pdfs</strong> function is responsible for loading the content of multiple PDF files and splitting them into smaller chunks. It accepts the following arguments: 
        <em>pdf_paths</em>, <em>chunk_size</em>, and <em>chunk_overlap</em>.
    </p>
    <p>
        First, the function initializes an empty list called <strong>documents</strong> to store the text extracted from the PDF files. It then iterates over each file path in the <em>pdf_paths</em> list.
    </p>
    <p>
        For each PDF file, it checks if the file exists using the <strong>os.path.exists()</strong> function. If the file does not exist, a <strong>FileNotFoundError</strong> is raised to inform the user.
    </p>
    <p>
        If the file exists, the function uses the <strong>PyPDFLoader</strong> from the <em>langchain</em> library to load the PDF's content. The loader extracts text from the file, and the resulting documents are appended to the <strong>documents</strong> list.
    </p>
    <p>
        After all PDF files are loaded, the function uses <strong>RecursiveCharacterTextSplitter</strong> to split the content into smaller chunks. The chunk size is controlled by the <em>chunk_size</em> parameter (default: 1000 characters), and overlapping text chunks are handled by the <em>chunk_overlap</em> parameter (default: 200 characters).
    </p>
    <p>
        Finally, the function returns a list of split documents for further processing, such as summarization or translation.
    </p>

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

