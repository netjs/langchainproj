from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(load_max_docs=5, 
                               doc_content_chars_max=2000, 
                               top_k_results=3)

docs = retriever.invoke("Indian economy")

#displaying the results.
for i, res in enumerate(docs):
    print(f"Result {i+1}: {res.page_content[:500]}...")

