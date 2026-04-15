from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama
from pydantic import BaseModel

# Define a schema for the JSON output
class Trend(BaseModel):
    name: str
    description: str


model = ChatOllama(model="llama3.1")
output_parser = JsonOutputParser(pydantic_object=Trend)

# Get format instructions from the parser
format_instructions = output_parser.get_format_instructions()


system_message = SystemMessagePromptTemplate.from_template("You are an expert {field} analyst")
human_message = HumanMessagePromptTemplate.from_template(
    "List one important trend in {field} for 2026.\n{format_instructions}"
)

# Create ChatPromptTemplate with partial variable for format_instructions
prompt = ChatPromptTemplate.from_messages([system_message, human_message]).partial(
    format_instructions=format_instructions
)

chain = prompt | model | output_parser

result = chain.invoke({"field": "AI"})
print(result)