from langchain_community.document_loaders import WebBaseLoader

# Example URL to load
url1 = "https://www.netjstech.com/2026/04/runablepassthrough-langchain-examples.html"   
url2 = "https://www.netjstech.com/2026/04/runnableparallel-in-langchain-example.html"

loader = WebBaseLoader([url1, url2])
documents = loader.load()
print(f"Number of Documents: {len(documents)}")

