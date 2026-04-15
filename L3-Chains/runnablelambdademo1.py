"""
This code file demonstrates the use of RunnableLambda in LCEL. 
Creates user method to determine the route. 
"""
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama


support_template = "You are a support agent. User input: {query}. Provide 3 reasons for the issue."
sales_template = "You are a sales specialist. User input: {query}. Provide 3 reasons to buy the product and 3 for not buying."
general_template = "You are a general assistant. User input: {query}. Provide a helpful response."
# 1. Define specialized chains
support_chain = ChatPromptTemplate.from_template(support_template) | ChatOllama(model="llama3.1") | StrOutputParser()
sales_chain = ChatPromptTemplate.from_template(sales_template) | ChatOllama(model="llama3.1") | StrOutputParser()
general_chain = ChatPromptTemplate.from_template(general_template) | ChatOllama(model="llama3.1") | StrOutputParser()

# 2. Define routing logic using RunnableLambda
def route_query(input: dict):
    print(f"Routing input: {input}")
    query = input["query"].lower()
    print(f"Routing query: {query}")
    if "support" in query or "issue" in query:
        return support_chain
    elif "price" in query or "buy" in query:
        return sales_chain
    else:
        return general_chain

router_node = RunnableLambda(route_query)

print("Router node created.", type(router_node))

# 3. Create the final routing chain
# The router_node returns a chain, which is then invoked with the input
final_chain = router_node 

# Example usage
result = final_chain.invoke({"query": "Request to buy a 3D printer."})

print(result)