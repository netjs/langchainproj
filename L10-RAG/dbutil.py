from langchain_chroma import Chroma
from util import load_documents, create_splits, getEmbeddingModel

# Global variable to hold the Chroma instance
_vector_store = None

def get_chroma_store():
    global _vector_store
    # Check if the Chroma instance already exists, if not create it
    if _vector_store is None:
        embeddings = getEmbeddingModel()
        _vector_store = Chroma(
            collection_name="data_collection",
            embedding_function=embeddings,
            persist_directory="./chroma_langchain_db",  # Where to save data locally
        )
    return _vector_store


def load_data():
    # Access the underlying Chroma client
    #client = get_chroma_store()._client

    # Delete the collection
    #client.delete_collection("data_collection")

    #get the PDFs from the resources folder
    documents = load_documents("./langchaindemos/resources")
    text_chunks = create_splits(documents)
    vector_store = get_chroma_store()
    #add documents
    vector_store.add_documents(text_chunks)

def search_data(query):
    vector_store = get_chroma_store()
    #search documents
    result = vector_store.similarity_search(
        query=query,
        k=3 # number of outcome 
    )
    return result

load_data()