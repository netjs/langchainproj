"""
This code file demonstrates how to use PydanticOutputParser in LCEL.
"""
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_ollama import ChatOllama


class Trend(BaseModel):
    name: str
    description: str

output_parser = PydanticOutputParser(pydantic_object=Trend)

# Get format instructions from the parser
format_instructions = output_parser.get_format_instructions()

model = ChatOllama(model="llama3.1")

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