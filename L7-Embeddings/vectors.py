from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
query = "I am running to the market"
vector = embeddings.embed_query(query)

# vector dimensions
print(len(vector)) 
# first 10 values
print(vector[:10])   

