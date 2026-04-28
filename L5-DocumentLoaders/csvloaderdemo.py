"""
Shows CSV loading with the CSVLoader, which uses the CSVLoader to extract data from CSV files. 
This loader is suitable for structured data in CSV format.
"""

from langchain_community.document_loaders import CSVLoader
import os

# Current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Project root is one level above
project_root = os.path.dirname(script_dir)

print(f"Project root directory: {project_root}")

file_path = os.path.join(project_root, "resources", "50_Startups.csv")
loader = CSVLoader(file_path)

documents = loader.load()

print(f"Number of Documents: {len(documents)}")
print(f"Type of Documents: {type(documents)}")
# One documnent per row in the CSV file
print(f"Content of first Document: {documents[0].page_content}") 
print(f"Metadata of first Document: {documents[0].metadata}")
