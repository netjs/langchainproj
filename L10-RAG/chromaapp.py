
from langchain_chroma import Chroma
from dbutil import get_chroma_store

vector_store = get_chroma_store()


#search documents
result = vector_store.similarity_search(
  query='What is the waiting period for the pre-existing diseases',
  k=3 # number of outcome 
)

#displaying the results.
for i, res in enumerate(result):
    print(f"Result {i+1}: {res.page_content[:500]}...")
print("Another Query")
query = "What is the condition for getting cumulative bonus"
result = vector_store.similarity_search(query, k=3)

for i, res in enumerate(result):
    print(f"Result {i+1}: {res.page_content[:500]}...")

print("Another Query")
query = "What are the co-pay rules"
result = vector_store.similarity_search(query, k=3)

for i, res in enumerate(result):
    print(f"Result {i+1}: {res.page_content[:500]}...")