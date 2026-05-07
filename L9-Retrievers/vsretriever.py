from langchain_chroma import Chroma
from dbutil import get_chroma_store

vector_store = get_chroma_store()

#search documents
# retriever  = vector_store.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 2}
# )

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.3},
)

result = retriever.invoke("What is the waiting period for covering pre-existing diseases")

#displaying the results.
for i, res in enumerate(result):
    print(f"Result {i+1}: {res.page_content[:500]}...")
