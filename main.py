"""
AI Opportunity Scanner using LangChain and GPT-4
"""

import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Set API key
os.environ["OPENAI_API_KEY"] = "your-key-here"

# Define prompt template
template = PromptTemplate.from_template(
    "You are an AI consultant. Analyze the following text and recommend 3 AI use cases: {input_text}"
)

# Build and run chain
chain = LLMChain(llm=OpenAI(), prompt=template)
text = open("business_report.txt").read()

response = chain.run(input_text=text)
print("AI Recommendations:
", response)
