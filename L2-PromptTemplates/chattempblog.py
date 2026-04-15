"""
This code file is part of the LangChain Demos, specifically for demonstrating how to use ChatPrompt 
Templates to generate blog posts. The code defines a prompt template for generating a blog post 
based on a given topic and then uses this template to create a blog post about 
the given topic. 
"""

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_ollama import ChatOllama 
from prompt import system_prompt_template, human_prompt_template


system_message = SystemMessagePromptTemplate.from_template(system_prompt_template)

human_message = HumanMessagePromptTemplate.from_template(human_prompt_template)

# Create a ChatPromptTemplate object
prompt = ChatPromptTemplate.from_messages([system_message, human_message])

# Initialize the Ollama model
model = ChatOllama(model="llama3.1", 
                    temperature=0.7)

# Define the topic and number of paragraphs for the blog post   
topic = "What is an ideal duration to keep any stock in your portfolio?"
no_of_paras = 3
expertise = "financial"

# Format the prompt with the topic and number of paragraphs
formatted_prompt = prompt.format(topic=topic, no_of_paras=no_of_paras, expertise=expertise)
# Print the formatted prompt to verify its correctness
print("Formatted Prompt:\n", formatted_prompt)  

# Generate the blog post using the model
response = model.invoke(formatted_prompt)
# Print the generated blog post 
print("\nGenerated Blog Post:\n", response.content)