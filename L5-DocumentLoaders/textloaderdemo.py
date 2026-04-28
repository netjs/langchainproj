from langchain_community.document_loaders import TextLoader
import os

# Current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Project root is one level above
project_root = os.path.dirname(script_dir)

print(f"Project root directory: {project_root}")

loader = TextLoader(os.path.join(project_root, "resources", "genai.txt"), encoding="utf-8")

documents = loader.load()

print(f"Number of Documents: {len(documents)}")
print(f"Type of Documents: {type(documents)}")
# Print first 500 characters of the first document
print(f"Content of first Document: {documents[0].page_content[:500]}...") 
print(f"Metadata of first Document: {documents[0].metadata}")
