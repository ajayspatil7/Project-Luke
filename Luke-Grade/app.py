# Required Library
import os
import time
from interface import interfaceBuilder as iC
import apiKey
import streamlit as stl
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apiKey.apiKey

# (Heading) UI Component 1
iC.IB_HeadingsViewer()

# (Language Choice) UI Component 2
user_lang_choice = iC.IB_Languages_Radio()

# (User Input) UI Component 3
# user_prompt = stl.text_input('Paste Your Code Here')
# Text area,
user_prompt = stl.text_area("**Paste your code here**", height=400)

model = OpenAI(temperature=0.9)


if user_prompt:
    with stl.spinner('Analysing your prompt...'):
        time.sleep(1.0)
        resp = model(user_prompt)
        stl.success("Here's your prompt")
        stl.code(resp, language=user_lang_choice)
