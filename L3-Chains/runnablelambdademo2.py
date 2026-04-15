from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from typing_extensions import TypedDict
from operator import itemgetter
from typing import Literal
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

history_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a history expert."),
        ("human", "{query}"),
    ]
)
geography_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert."),
        ("human", "{query}"),
    ]
)

model = ChatGroq(model="qwen/qwen3-32b", temperature=0.5)

chain_history = history_prompt | model | StrOutputParser()
chain_geography = geography_prompt | model | StrOutputParser()

route_system = "Classify the user's query to either the history "
"or geography related. Answer with one word only: 'history' or 'geography'."
route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", route_system),
        ("human", "{query}"),
    ]
)

#Class to enforce structured output from LLMs
class RouteQuery(TypedDict):
    """Schema for LLM output for routing queries."""
    destination: Literal["history", "geography"]

route_chain = (
    route_prompt
    | model.with_structured_output(RouteQuery)
    | itemgetter("destination")
)

final_chain = {
    "destination": route_chain,  
    "query": lambda x: x["query"],  # pass through input query
} | RunnableLambda(
    # if history, chain_history. otherwise, chain_geography.
    lambda x: (
        # display the routing decision for clarity
        print(f"Routing to destination: {x['destination']}") or
        (chain_history if x["destination"] == "history" else chain_geography)
    )
)

result = final_chain.invoke({"query": "List 5 temples built by the Cholas. Only list the temples, no other information. "})

print(result)