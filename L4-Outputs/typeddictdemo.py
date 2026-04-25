"""
This code file demonstrates how to use TypedDict for structured outputs in LCEL.
"""
from typing import List, Optional, TypedDict
from langchain_groq import ChatGroq
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

#Define a TypedDict for a single book
class BookModel(TypedDict):
    title: str
    year_first_published: int
    main_characters: Optional[list[str]]

#Define a TypedDict for multiple books (container)
class BooksResponse(TypedDict):
    books: List[BookModel]

prompt = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "You are a helpful assistant that provides information about books."},
    HumanMessagePromptTemplate.from_template("List 3 books of author {author}.")
])

model = ChatGroq(model="qwen/qwen3-32b", temperature=0.2)

# Wrap with structured output using TypedDict
structured_model = model.with_structured_output(BooksResponse)

chain = prompt | structured_model

response = chain.invoke({"author": "Agatha Christie"})

print(response)