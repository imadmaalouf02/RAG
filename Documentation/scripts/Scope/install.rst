

Installation Instructions
-------------------------

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 

    Follow these steps to install and run the <strong>RAG - Retrieval-Augmented Generation</strong> application locally:</i></span></p>

    <ol>
    <li><strong>Clone the repository:</strong></li>
    <pre><code>git clone https://github.com/imadmaalouf02/RAG.git</code></pre>

    <li><strong>Install the dependencies:</strong></li>
    <p style="text-align: justify;"><span style="color:#000080;"><i> Make sure you have Python installed. You can install the required dependencies using the following command:</i></span></p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <li><strong>Alternative Conda installation:</strong></li>
    <p style="text-align: justify;"><span style="color:#000080;"><i> If you are using <a href="https://docs.conda.io/">Conda</a> as your environment manager, you can install Streamlit with:</i></span></p>
    <pre><code>conda install -c conda-forge streamlit</code></pre>

    <li><strong>Run the application:</strong></li>
    <p style="text-align: justify;"><span style="color:#000080;"><i> Once all dependencies are installed, run the Streamlit app using:</i></span></p>
    <pre><code>streamlit run app.py</code></pre>

    <li><strong>Access the app in your browser:</strong></li>
    <p style="text-align: justify;"><span style="color:#000080;"><i> After running the command, Streamlit will open the application in your default browser. If not, you can access it by navigating to:</i></span></p>
    <pre><code>http://localhost:8501</code></pre>
    </ol>


Step-by-Step Guide for Using the Application
--------------------------------------------
.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i> 

    <ol>
    <li><strong>Upload your document:</strong></li>
     <p style="text-align: justify;"><span style="color:#000080;"><i> On the main page of the application, you will see an option to upload a PDF file. Use the file upload widget to select your document.</i></span></p>

    <li><strong>Select the language model:</strong></li>
     <p style="text-align: justify;"><span style="color:#000080;"><i> Choose one of the available language models from the dropdown menu. The models include:</i></span></p>
    <ul>
        <li><strong>Llama 2:</strong> Ideal for general text generation and comprehension.</li>
        <li><strong>Mistral:</strong> Fast and efficient for text generation.</li>
        <li><strong>CodeLlama:</strong> Specialized for generating and understanding code.</li>
        <li><strong>Llama 3.1:</strong> Advanced model for more complex language tasks.</li>
    </ul>

    <li><strong>Choose the task:</strong></li>
     <p style="text-align: justify;"><span style="color:#000080;"><i> Select the task you want to perform from the available options:</i></span></p>
    <ul>
        <li><strong>Summarization:</strong> Get a concise summary of the document.</li>
        <li><strong>Translation:</strong> Translate the document content to another language.</li>
        <li><strong>Question-Answering:</strong> Ask questions about the document and receive detailed responses.</li>
    </ul>

    <li><strong>View the results:</strong></li>
     <p style="text-align: justify;"><span style="color:#000080;"><i> Once the task is complete, the output will be displayed on the same page. Depending on the task, you'll either see a summary, translation, or answers to your questions.</i></span></p>
    </ol>


