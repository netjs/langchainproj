"""
This code file is part of the LangChain Demos, specifically for demonstrating how to use Prompt 
Templates to generate blog posts. The code defines a prompt template for generating a blog post 
based on a given topic and then uses this template to create a blog post about 
the given topic. 
"""

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama 
# Define a prompt template for generating a blog post
template = """
    You are an expert technical content writer. Write a detailed blog post as per the given instructions.
    The blog post should be engaging, informative, and well-structured. Include an introduction,
    main body, and conclusion. Use subheadings where appropriate and provide examples to illustrate key points.
    ***Instructions***: Write a {no_of_paras} paragraphs blog post about the following topic: {topic}.
"""

# Create a PromptTemplate object
prompt = PromptTemplate.from_template(template)
# Initialize the Ollama model
model = ChatOllama(model="llama3.1", 
                    temperature=0.7)
# Define the topic and number of paragraphs for the blog post   
topic = "Dictionary in Python"
no_of_paras = 6
# Format the prompt with the topic and number of paragraphs
formatted_prompt = prompt.format(topic=topic, no_of_paras=no_of_paras)   
# Print the formatted prompt to verify its correctness
print("Formatted Prompt:\n", formatted_prompt)  
# Generate the blog post using the model
response = model.invoke(formatted_prompt)
# Print the generated blog post 
print("\nGenerated Blog Post:\n", response.content)