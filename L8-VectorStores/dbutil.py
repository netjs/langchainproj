from langchain_chroma import Chroma
from util import load_documents, create_splits, getEmbeddingModel
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from dotenv import load_dotenv
load_dotenv()
import os

# Initialize Pinecone client
pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key)
index_name = "test"
index = pc.Index(index_name)

# if chroma store is used
def get_chroma_store():
    embeddings = getEmbeddingModel()
    vector_store = Chroma(
        collection_name="data_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",  # Where to save data locally
    )
    return vector_store

# if Pinecone store is used
def get_pinecone_store():
    embeddings = getEmbeddingModel()
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    return vector_store

def load_data():
    # Access the underlying Chroma client
    #client = get_chroma_store()._client

    # Delete the collection
    #client.delete_collection("data_collection")

    documents = load_documents("./langchaindemos/resources")
    text_chunks = create_splits(documents)
    #COMMENT/UNCOMMENT BASED ON THE VECTOR STORE YOU ARE USING
    #vector_store = get_chroma_store()
    vector_store = get_pinecone_store()
    #add documents
    vector_store.add_documents(text_chunks)

load_data()