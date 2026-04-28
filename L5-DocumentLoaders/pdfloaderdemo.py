"""
Shows PDF loading with the PyPDFLoader, which uses the PyPDF library to extract text from PDF files. This loader is suitable for simple PDFs without complex formatting or images. It can handle basic text extraction but may struggle with more complex layouts or scanned documents.
"""

from langchain_community.document_loaders import PyPDFLoader
import os

# Current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Project root is one level above
project_root = os.path.dirname(script_dir)

print(f"Project root directory: {project_root}")

loader = PyPDFLoader(os.path.join(project_root, "resources", "Health Insurance Policy Clause.pdf"))

documents = loader.load()


print(f"Number of Documents: {len(documents)}")
print(f"Type of Documents: {type(documents)}")

# Print first 500 characters of the first document
print(f"Content of first Document: {documents[0].page_content[:500]}...")
print(f"Metadata of first Document: {documents[0].metadata}")
