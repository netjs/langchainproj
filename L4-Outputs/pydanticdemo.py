"""
This code file demonstrates how to use Pydantic models for structured outputs in LCEL.
"""
from pydantic import BaseModel
from typing import Optional, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

#Define a TypedDict for a single book
class BookModel(BaseModel):
    title: str
    year_first_published: int
    main_characters: Optional[list[str]]

#Define a TypedDict for multiple books (container)
class BooksResponse(BaseModel):
    books: List[BookModel]

prompt = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "You are a helpful assistant that provides information about books."},
    HumanMessagePromptTemplate.from_template("List 3 books of author {author}.")
])

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", temperature=0.2)

# Wrap with structured output using TypedDict
structured_model = model.with_structured_output(BooksResponse)

chain = prompt | structured_model

response = chain.invoke({"author": "Agatha Christie"})

print(response)

# to get plain dictionary output instead of pydantic model
response_dict = response.model_dump()
print(response_dict)