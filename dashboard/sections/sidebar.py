import streamlit as st

def create():
    st.sidebar.header("What do you want to see?")
    seleccionado=st.sidebar.selectbox("Select only one:", options=["Teams","Players","Results"])

    if seleccionado=="Teams":
        Finish=st.sidebar.selectbox("Select only one:", options=["See team alone","2020 vs 2016","against team"])
    return Finish
