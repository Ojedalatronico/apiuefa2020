import streamlit as st
from data.get import get_all_team

st.title("UEFA EURO 2020")
st.text("We are working now :)")

theteams=st.selectbox("pick one", ([equipos["common_name"] for equipos in get_all_team()]))

st.text(theteams)