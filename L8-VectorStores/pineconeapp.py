from dbutil import get_pinecone_store

vector_store = get_pinecone_store()

def do_search(query:str):
   #search documents
	result = vector_store.similarity_search(
  		query=query,
  		k=3 # number of outcome 
	)
    #displaying the results.
	for i, res in enumerate(result):
    	  print(f"Result {i+1}: {res.page_content[:500]}...")



do_search('What is the waiting period for the pre-existing diseases')

print("Another Query")

do_search('What is the condition for getting cumulative bonus')


print("Another Query")

do_search('What are the co-pay rules')
