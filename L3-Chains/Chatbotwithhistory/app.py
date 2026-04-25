"""
UI part of chatbot with history. Uses streamlit for the user interface.

"""

import streamlit as st
from chatbot import generate_response

# Streamlit app to demonstrate the simple chain
st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🤖 Chatbot With Context" )
# Initialize session state
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#Ensure user_id is set before allowing chat interactions
if st.session_state.user_id is None:
    user_id_input = st.text_input("Enter your User ID:")
    if st.button("Confirm User ID"):
        if user_id_input.strip() == "":
            st.warning("User ID is required to continue.")
        else:
            st.session_state.user_id = user_id_input.strip()
            st.success(f"User ID set: {st.session_state.user_id}")

if st.session_state.user_id:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Enter your query:")  

    if user_input:
        st.session_state.chat_history.append( {"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        response = generate_response(user_input, st.session_state.user_id)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(f"**Chatbot Response:** {response}")   
    else:
        st.warning("Please enter a query to get a response.")