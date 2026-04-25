"""
This code file demonstrates how to use JSON Schema for structured outputs in LCEL.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Define JSON Schema for a single book
book_schema = {
    "title": "BookModel",
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "year_first_published": {"type": "integer"},
        "main_characters": {
            "type": "array",
            "items": {"type": "string"},
            "maxItems": 3   # restrict to 3 characters
        }
    },
    "required": ["title", "year_first_published"]
}


# Define JSON Schema for multiple books (container)
books_response_schema = {
    "title": "BooksResponse",
    "type": "object",
    "properties": {
        "books": {
            "type": "array",
            "items": book_schema,
            "minItems": 3,
            "maxItems": 3
        }
    },
    "required": ["books"]
}

prompt = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "You are a helpful assistant that provides information about books."},
    HumanMessagePromptTemplate.from_template("List 3 books of author {author}.")
])

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", temperature=0.2)

# Wrap with structured output using TypedDict
structured_model = model.with_structured_output(books_response_schema)

chain = prompt | structured_model

response = chain.invoke({"author": "Agatha Christie"})

print(response)
