"""
UI for the conversational RAG
"""

import streamlit as st
import uuid
from sqlutil import get_sessions_for_user, get_session_messages, save_message
from conversationalrag import generate_response
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
st.set_page_config(page_title="Conversational RAG", layout="wide")
st.title("Conversational RAG")
st.sidebar.title("Previous Conversations")

if "session_id" not in st.session_state or st.sidebar.button("Start New Conversation"):
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.chat_history = []

if "user_id" not in st.session_state:
    st.session_state.user_id = None

#Ensure user_id is set before allowing chat interactions
if st.session_state.user_id is None:
    user_id_input = st.text_input("Enter your User ID:")
    if st.button("Confirm User ID"):
        if user_id_input.strip() == "":
            st.warning("User ID is required to continue.")
        else:
            st.session_state.user_id = user_id_input.strip()

if st.session_state.user_id:
    st.sidebar.markdown("Previous Conversations")
    sessions = get_sessions_for_user(st.session_state.user_id)
    for session in sessions:
        session_id, last_active = session
        if st.sidebar.button(f"Session: {session_id[:10]} (Last Active: {last_active})"):
            st.session_state.session_id = session_id
            st.session_state.chat_history = get_session_messages(session_id)    
    st.markdown(f"Hi, {st.session_state.user_id} what would you like to ask?")
    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            role = "user"
            with st.chat_message(role):
                st.markdown(message.content) 
        elif isinstance(message, AIMessage):
            role = "assistant"
            with st.chat_message(role):
                st.markdown(message.content) 
    user_input = st.chat_input("Enter your query:")  

    if user_input:
   
        save_message(st.session_state.user_id, st.session_state.session_id, "user", user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        with st.chat_message("user"):
            st.markdown(user_input)
        response = generate_response(user_input, st.session_state.chat_history)
        st.session_state.chat_history.append(AIMessage(content=response))
        save_message(st.session_state.user_id, st.session_state.session_id, "assistant", response)
        with st.chat_message("assistant"):
            st.markdown(f"**Chatbot Response:** {response}") 