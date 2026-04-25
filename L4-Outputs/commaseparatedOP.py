"""
This code file demonstrates how to use the CommaSeparatedListOutputParser in LCEL.
"""
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.1")

output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()

system_message = SystemMessagePromptTemplate.from_template("You are an expert {field} analyst")

human_message = HumanMessagePromptTemplate.from_template("List 5 important trends in {field}. \n{format_instructions}")

prompt = ChatPromptTemplate.from_messages([system_message, human_message]).partial(format_instructions=format_instructions)

chain = prompt | model | output_parser

result = chain.invoke({"field": "AI"})
print(result)
