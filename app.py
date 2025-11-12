import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANCHCHAIN_API_KEY'] = os.getenv('LANCHCHAIN_API_KEY')
os.environ['LANCHCHAIN_PROJECT'] = os.getenv('LANCHCHAIN_PROJECT')
os.environ['LANCHCHAIN_TRACING_V2'] = 'true'


from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


### design prompt template

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question."),
    ("user", "Question: {question}")
])

## streamlit Framewok
st.title("Langchain Demo with gemma-2b")
input_text = st.text_input("What question in your mind?")

## ollama LLama2 model

llm = Ollama(model="gemma:2b")
output_praser = StrOutputParser()
chain = prompt|llm|output_praser

if input_text:
    st.write(chain.invoke({"question":input_text}))


