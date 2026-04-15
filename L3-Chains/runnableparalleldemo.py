"""
This code file demonstrates the use RunnableParallel in LCEL. 
Creates two parallel chains, one for generating a content with professional tone for LinkedIn 
and another for generating a content with casual tone for Twitter. 
"""
from langchain.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define system and human message templates
linkedin_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant that generates content for social media platforms."),
    HumanMessagePromptTemplate.from_template("Write a {linkedin_tone} post for {linkedin_platform} about {topic}.")            
])

twitter_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant that generates content for social media platforms."),
    HumanMessagePromptTemplate.from_template("Write a {twitter_tone} post for {twitter_platform} about {topic}.")            
])

# Define the output parser
parser = StrOutputParser()

def generate_content(topic: str) -> dict:
    """
    This function generates content for LinkedIn and Twitter in parallel using RunnableParallel.
    
    Args:
        topic (str): The topic to generate content about.
    
    Returns:
        dict: A dictionary containing the generated content for LinkedIn and Twitter.
    """
    # Initialize the model
    #model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", temperature=0.7)   
    model = ChatOllama(model="llama3.1", temperature=0.7)              

    # Create two parallel chains for LinkedIn and Twitter
    linkedin_chain = linkedin_prompt | model | parser
    twitter_chain = twitter_prompt | model | parser

    # Create a RunnableParallel object to run both chains in parallel
    parallel_chain = RunnableParallel({
        "linkedin": linkedin_chain,
        "twitter": twitter_chain
    })

    # Generate content for both platforms in parallel
    response = parallel_chain.invoke({
        "topic": topic,
        "linkedin_tone": "professional",
        "linkedin_platform": "LinkedIn",
        "twitter_tone": "casual",
        "twitter_platform": "Twitter"
    })

    # Return the generated content as a dictionary
    return response

# Example usage
if __name__ == "__main__":
    topic = "XYZ tech announces new AI product for its gen AI platform"
    generated_content = generate_content(topic)
    print("Generated LinkedIn Post:")
    print(generated_content["linkedin"])
    print("\nGenerated Twitter Post:")
    print(generated_content["twitter"])