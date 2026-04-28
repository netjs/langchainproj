from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import os
print(os.getcwd())
# Load all .pdf files from the specified directory
loader = DirectoryLoader("./langchaindemos/resources", glob="**/*.pdf", loader_cls=PyPDFLoader)

documents = loader.load()

# Check the number of documents loaded
print(f"Loaded {len(documents)} documents.")

