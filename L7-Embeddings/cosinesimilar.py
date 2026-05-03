from langchain_ollama import OllamaEmbeddings
import numpy as np

embeddings = OllamaEmbeddings(model="nomic-embed-text")

v1 = np.array(embeddings.embed_query("I am running to the market"))
v2 = np.array(embeddings.embed_query("I am walking to the market"))

# cosine similarity using numpy
cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("Similarity is", cos_sim)