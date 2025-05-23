import streamlit as st
import pyodbc
import pandas as pd
st.header("Hello World 5")

texto = st.text_input("Enter your name")

def test():
    st.write("Hello", texto)

st.button("Submit", on_click=test)

st.markdown("## This is a markdown")

SECRETO = 123

