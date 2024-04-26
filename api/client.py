import requests
import streamlit as st
import os

HOST_URL = os.environ.get("HOST_URL", "http://127.0.0.1:8000")

def get_gemini_response(question):
    response=requests.post(f"{HOST_URL}/gemini/invoke",
    json={'input':{'topic':question}})
    response.raise_for_status()
    return response.json()['output']['content']


def get_ollama_response(question):
    response=requests.post(f"{HOST_URL}/gemini/invoke",
    json={'input':{'topic':question}})
    response.raise_for_status()
    return response.json()['output']['content']


#streamlit framework
st.title("LangChain LLM API")
input1 = st.text_input("Ask me a Question for Gemini")
input2 = st.text_input("Ask me a Question for ollama")

if input1:
    st.write(get_gemini_response(input1))

if input2:
    st.write(get_ollama_response(input2))

