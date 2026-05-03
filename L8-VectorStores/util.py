from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

def load_documents(dir_path):
    
    """
    loading the documents in a specified directory
    """
    pdf_loader = DirectoryLoader(dir_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = pdf_loader.load()
    return documents

def create_splits(extracted_data):
    """
    splitting the document using text splitter
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

def getEmbeddingModel():
    """
    Configure the embedding model used
    """
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings