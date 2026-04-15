"""
This code file demonstrates the use of simple chain using LCEL. 
A simple chatbot with a basic response mechanism. Uses streamlit for the user interface.
"""

from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_ollama import ChatOllama

import streamlit as st
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser


# Define system and human message templates
system_message = SystemMessage(content="You are a helpful assistant that responds to user queries.")    
# Define the output parser
parser = StrOutputParser()

def generate_response(user_input: str) -> str:
    """
    This function generates a response for a given user input using a simple chain.
    
    Args:
        user_input (str): The user's input query.
    Returns:
        str: The generated response as a string.    

    """
    # Create a ChatPromptTemplate object
    prompt = ChatPromptTemplate.from_messages([system_message, 
                                               HumanMessagePromptTemplate.from_template("{user_input}")]) 
    # Initialize the model
    model = ChatOllama(model="llama3.1", temperature=0.5)            

    #chain the prompt, model, and parser together
    chatbot_chain = prompt | model | parser

    # Generate the response using the model
    response = chatbot_chain.invoke({"user_input": user_input})
    #print(response)
    # Return the generated response
    return response

# Streamlit app to demonstrate the simple chain
st.set_page_config(page_title="Simple Chatbot", layout="centered")
st.title("🤖 Simple Chatbot" )
# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Enter your query:")  

if user_input:
    st.session_state.chat_history.append( {"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    response = generate_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(f"**Chatbot Response:** {response}")   
else:
    st.warning("Please enter a query to get a response.")     