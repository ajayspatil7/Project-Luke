# Required Library
import os
import apiKey
import streamlit as stl
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apiKey.apiKey
stl.title("MyGpt-GPT")
user_prompt = stl.text_input('Paste Your Code Here')

model = OpenAI(temperature=0.9)

if user_prompt:
    resp = model(user_prompt)
    stl.write(resp)