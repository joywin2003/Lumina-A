from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

app = FastAPI(
    title="LangChain LLM API",
    description="API for multiple llms such as Ollama and Gemini using LangServe",
    version="0.1.0",
)


#Ollama model
llama = Ollama(model="llama3")

#gemini model
gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",google_api_key=GOOGLE_API_KEY)