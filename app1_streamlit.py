import streamlit as st
import pyodbc
import pandas as pd
st.header("Hello World")

st.text_input("Enter your name")

def test():
    print("test")

st.button("Submit", on_click=test)

SECRETO = 123

