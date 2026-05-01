from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def get_file_path(file_name):
    # Current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Project root is one level above
    project_root = os.path.dirname(script_dir)

    #print(f"Project root directory: {project_root}")
    file_path = os.path.join(project_root, "resources", file_name)
    return file_path

def load_documents(file_name):
    file_path = get_file_path(file_name)
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"Number of Documents: {len(documents)}")
    return documents

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = text_splitter.split_documents(documents)
    print(f"length of chunks {len(chunks)}")
    for i, chunk in enumerate(chunks[:3]):  # first 3 chunks
        # Chunk Lengths
        print(f"Chunk {i+1} length: {len(chunk.page_content)}")
        # Chunk Content
        #print(f"Chunk {i+1}:\n{chunk.page_content}...\n") 
        # Chunk Metadata
        #print(f"Chunk {i+1} metadata: {chunk.metadata}")

if __name__ == "__main__":
    documents = load_documents("Health Insurance Policy Clause.pdf")
    split_documents(documents)
    






