from langchain_chroma import Chroma
from util import load_documents, create_splits, getEmbeddingModel

def get_chroma_store():
    embeddings = getEmbeddingModel()
    vector_store = Chroma(
        collection_name="data_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",  # Where to save data locally
    )
    return vector_store


def load_data():
    # Access the underlying Chroma client
    #client = get_chroma_store()._client

    # Delete the collection
    #client.delete_collection("data_collection")

    documents = load_documents("./langchaindemos/resources")
    text_chunks = create_splits(documents)
    vector_store = get_chroma_store()
    #add documents
    vector_store.add_documents(text_chunks)

load_data()