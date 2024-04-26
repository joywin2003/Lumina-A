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

prompt=ChatPromptTemplate.from_template("{topic}")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|gemini,
    path="/gemini",
)

add_routes(
    app,
    prompt2|llama,
    path="/llama",
)

add_routes(
    app,
    prompt1|gemini,
    path="/essay"
)

add_routes(
    app,
    prompt2|llama,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)