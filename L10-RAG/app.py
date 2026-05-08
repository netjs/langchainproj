"""
This code file contains Streamlit app to demonstrate basic
RAG application
"""
import streamlit as st
from simplerag import generate_response

# 
st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("🤖 Medical Insurance Chatbot" )
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