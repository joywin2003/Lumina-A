import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY=os.environ.get("LANGCHAIN_API_KEY")


#chatbot
llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY)
prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "Question:{question}"),
])
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


#Streamlit
import streamlit as st
st.title("Google Gemini 1.5 pro model chatbot")
question = st.text_input("Ask me a Question")

if question:
    st.write(chain.invoke(f"Question: {question}")) 