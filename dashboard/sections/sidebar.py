from google.protobuf.symbol_database import Default
from sections import sidebar
import streamlit as st


def create():

    st.sidebar.header("What do you want to see?")
    seleccionado=st.sidebar.selectbox("What do you want yo see:", options=["General Statistics","Teams","Players","Matches",])

    if seleccionado=="General Statistics":
        Finish=st.sidebar.selectbox("Do you want to see a year or compare", options=["See a year", "Compare years"])
        return Finish

    if seleccionado=="Players":
        Finish=st.sidebar.selectbox("What do you want to do", options=["See individual stats","Compare with another player"])
        return Finish
    
    if seleccionado=="Teams":
        Finish=st.sidebar.selectbox("Select only one:", options=["See team alone","2020 vs 2016","against team"])
        return Finish

    if seleccionado=="Matches":
        Finish=st.sidebar.selectbox("and:", options=["General stats","individual matches"])
        return Finish

    return None