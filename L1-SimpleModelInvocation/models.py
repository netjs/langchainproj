from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(    
    model="gemini-3.1-flash-lite-preview",
    temperature=0.3
)

response = model.invoke("What is the role of GPU in deep learning, explain in 5 lines?")
print(response.content)