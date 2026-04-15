"""
This code file demonstrates the use of RunnableBranch in LCEL. 
Creates user method to determine the route and based on the conditon one of the chains is selected. 
Support chain, sales chain, and general chain are created for demonstration.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableBranch

support_template = "You are a support agent. User input: {query}. Provide 3 reasons for the issue."
sales_template = "You are a sales specialist. User input: {query}. Provide 3 reasons to buy the product and 3 for not buying."
general_template = "You are a general assistant. User input: {query}. Provide a helpful response."

model = ChatOllama(model="llama3.1", temperature=0.5)
# 1. Define specialized chains
support_chain = ChatPromptTemplate.from_template(support_template) | model | StrOutputParser()
sales_chain = ChatPromptTemplate.from_template(sales_template) | model | StrOutputParser()
general_chain = ChatPromptTemplate.from_template(general_template) | model | StrOutputParser()

# 2. Define routing logic using RunnableLambda
def route_query(input: str) -> str:
    query = input.lower()
    print(f"Routing query: {query}")
    if "support" in query or "issue" in query:
        return "support"
    elif "price" in query or "buy" in query:
        return "sales"
    else:
        return "general"
    
branch = RunnableBranch(
    (lambda x: route_query(x["query"]) == "support", support_chain),
    (lambda x: route_query(x["query"]) == "sales", sales_chain),
    general_chain
)

# Example usage
response1 = branch.invoke({"query": "I have a login issue with my account."})
print(response1)

response2 = branch.invoke({"query": "Request to buy a 3D printer."})
print(response2)

response3 = branch.invoke({"query": "Does company provide transportation services?"})
print(response3)