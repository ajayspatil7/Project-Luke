import streamlit as stl


def IB_HeadingsViewer():
    stl.title(":blue[Alan Turing Checker]")
    stl.divider()


def IB_Languages_Radio():
    languages = ['python', 'c', 'cpp', 'cshtml', 'css', 'javascript', 'csharp']
    language_choice = stl.radio("**:green[Choose your language]**", (languages), horizontal=True)
    return language_choice

