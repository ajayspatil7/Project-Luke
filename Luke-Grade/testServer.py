import streamlit as st


def submittedTest():
    st.write("I've been called by a function")


isEmpty = True


st.button("Submit", on_click=submittedTest)

