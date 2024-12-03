# Importations des bibliothèques nécessaires
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from concurrent.futures import ThreadPoolExecutor
import os

# Configurez le modèle Ollama
llm = Ollama(model="llama3.1", base_url="http://localhost:11434")


