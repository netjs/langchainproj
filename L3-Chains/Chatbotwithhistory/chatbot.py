"""
This code file demonstrates the use of a chatbot with history using LCEL.
A chatbot is created that maintains a history of the conversation using MessagePlaceholder 
and RunnableWithMessageHistory.
Uses streamlit for the user interface.
"""

from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_ollama import ChatOllama

from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Define system and human message templates
system_message = SystemMessage(content="You are a helpful assistant that responds to user queries.")
# Define the output parser
parser = StrOutputParser()

# In-Memory Store to hold chat histories for different sessions 
# (not suitable for production, just for demo purposes)
store = {}

# Function to retrieve chat history for a given session_id, or create a new one if it doesn't exist
def get_session_history(session_id: str):
    print(f"Retrieving chat history for session_id: {session_id}")
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def generate_response(user_input: str, session_id: str) -> str:
    session_id = session_id or "default_session"
    # Create a ChatPromptTemplate object with MessagePlaceholder for conversation history
    prompt = ChatPromptTemplate.from_messages([
        system_message, 
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{user_input}")
    ]) 


    # Initialize the model
    model = ChatOllama(model="llama3.1", temperature=0.1)            

    # Chain the prompt, model, and parser together using RunnableWithMessageHistory
    chatbot_chain = prompt | model | parser

    with_message_history = RunnableWithMessageHistory(
        chatbot_chain,
        get_session_history,
        input_messages_key="user_input",
        history_messages_key="chat_history",
    )
    response = with_message_history.invoke(
        {"user_input": user_input},
        config={"configurable": {"session_id": session_id}}
    )
    
    return response



