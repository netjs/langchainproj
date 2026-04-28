"""
Shows CSV loading with the CSVLoader, which uses the CSVLoader to extract data from CSV files. 
Then sending that data to a LLM to answer a question based on the data in the CSV file.
"""
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
import os
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


def load_text_from_url(url: str):

    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents

def generate_response(user_input: str) -> str:
    document = load_text_from_url("https://www.netjstech.com/2026/04/runablepassthrough-langchain-examples.html")
    system_message = SystemMessage(content="You are a helpful assistant that responds to user queries based on the provided context and nothing else.")
    human_message = HumanMessagePromptTemplate.from_template("Based on the given context: {context}, answer the question: {user_input}")
    prompt = ChatPromptTemplate.from_messages([system_message, human_message])
    model = ChatOllama(model="llama3.1")
    chain = prompt | model | StrOutputParser()
    response = chain.invoke({"user_input": user_input, "context": document[0].page_content})
    return response

if __name__ == "__main__":
    response = generate_response("What is the main topic of the article and what are the key points discussed?")
    print(response)


