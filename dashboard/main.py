import streamlit as st
from data.get import get_all_team, find_team
from sections import sidebar

sidebar.create()



st.title("UEFA EURO 2020")
st.text("We are working now :)")

theteam=st.selectbox("pick first team", ([equipos["common_name"] for equipos in get_all_team()]))
theteam2=st.selectbox("pick second team", ([equipos["common_name"] for equipos in get_all_team()]))

data=[find_team(name) for name in [theteam, theteam2]]

st.text(data)