"""
This code file demonstrates how to use ChatPrompt Templates to generate code. The code defines a 
prompt template for generating code for the given programming problem and given programming language,
and then uses this template to create code for the given problem.
"""

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_ollama import ChatOllama
from prompt import code_system_prompt_template, code_human_prompt_template
import streamlit as st
from langchain_core.messages import HumanMessage

# Define system and human message templates
system_message = SystemMessagePromptTemplate.from_template(code_system_prompt_template)
human_message = HumanMessagePromptTemplate.from_template(code_human_prompt_template)    

def generate_code(problem: str, language: str) -> str:
    """
    This function generates code for a given programming problem and programming language using a 
    ChatPromptTemplate.
    
    Args:
        problem (str): The programming problem to solve.
        language (str): The programming language to use for the code generation.
    
    Returns:
        str: The generated code as a string.
    """
    # Create a ChatPromptTemplate object
    prompt = ChatPromptTemplate.from_messages([system_message, human_message]) 
    # Initialize the model
    model = ChatOllama(model="llama3.1",    
                        temperature=0.7)            
    # Format the prompt with the problem and language
    formatted_prompt = prompt.format(problem=problem, language=language)
    print(f"Formatted prompt: {formatted_prompt}")
    # Generate the code using the model
    response = model.invoke(formatted_prompt)
    # Return the generated code
    return response.content


# Streamlit app to demonstrate code generation
st.set_page_config(page_title="AI Code Generator", layout="centered")
st.title("🤖 Code Generator ")
st.markdown("Select **programming language** and state your coding problem to generate code!")
# Create a dropdown with a default value
option = st.selectbox(
    'Choose your favorite programming language:',
    ('Python', 'JavaScript', 'Java', 'C++'),
    index=0  # sets the default value to the first option
)

#print(f"Selected programming language: {option}")
problem = st.text_area("Enter the programming problem you want to solve:")

# Generate code when the button is clicked
if st.button("Generate Code"):
    if problem.strip() == "":
        st.warning("Please enter a programming problem to generate code.")
    else:
        with st.spinner("Generating code..."):
            generated_code = generate_code(problem, option)
            st.code(generated_code, language=option.lower())