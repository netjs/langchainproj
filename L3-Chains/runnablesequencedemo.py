from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 1. Define LLM
llm = ChatOllama(model="llama3.1", temperature=0)

#llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", temperature=0)

# Define the prompts
prompt_1 = PromptTemplate.from_template(
    "Analyze the following contract clause for any hidden financial risks: {clause}"
)
prompt_2 = PromptTemplate.from_template(
    "Summarize the following risk analysis in a professional, concise, bulleted memo for the financial head: {analysis}"
)


#Parsing to String ensures clean text outputs
parser = StrOutputParser()

# Step A: Clause -> Risk Analysis
risk_analysis_chain = RunnableSequence(prompt_1, llm, parser)

# Step B: Risk Analysis -> Financial Memo
financial_memo_chain = RunnableSequence(prompt_2, llm, parser)

# 4. Create Sequence: Clause -> Risk Analysis -> Financial Team 
# (gets analysis as input and produces memo for financial head as output)
# Sequence is: Prompt1 -> LLM -> Parser -> Prompt2 -> LLM -> Parser
# chain = (
#     {"analysis": prompt_1 | llm | parser} 
#     | prompt_2 
#     | llm 
#     | parser
# )

# Step C: Full pipeline
chain = RunnableSequence(
        {"analysis": risk_analysis_chain},  # feed clause into risk analysis
        financial_memo_chain                # feed analysis into financial memo    
)

# Execute with Corporate Input
contract_clauses = """
Scope of Work (SOW):Vendor shall deliver required work with in one month of initiation and provide support services as detailed in Exhibit A.
Payment Terms: Client shall pay Invoice within 30 days of receipt. Late payments will incur a 1.5% monthly interest fee.
Termination Clause: Either party may terminate this agreement with 10 calendar days' written notice if the other party breaches material terms.
Limitation of Liability: The vendor will not be liable for any damages unless they exceed 300% of the total contract value, and notice is provided within 1 day.
"""
result = chain.invoke({"clause": contract_clauses})

print(result)