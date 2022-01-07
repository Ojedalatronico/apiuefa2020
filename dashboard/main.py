import streamlit as st
from sections import sidebar
from data.get import *
from data.usefully import *
import pandas as pd

seleccion=sidebar.create()
pd.DataFrame()
st.title("UEFA EURO 2020")
st.text("We are working now :)")

# --- General Statistics path ---

if seleccion== "See a year":
    data=st.selectbox("Select a year", ["2020","2016"])
    df=pd.DataFrame(league(data)).transpose()
    st.dataframe(df)
    box=st.selectbox("Do you want to see totals goals each 10 min or 15 min", ["10 min","15 min"])
    st.pyplot(bar_chart_goals(data,box))
if seleccion=="Compare years":
    st.text("I'm working on it")

# --- Players path ---

if seleccion=="See individual stats":
    data=st.selectbox("How do you want to look it up", ["Full name","Nationality","Position","Age"])
    if data == "Full name":
        name=st.text_input("Intenta introducir un nombre")
        jugador=find_players(name)
        st.text(jugador)
    if data == "Nationality":
        nationality=st.selectbox("pick team", list(set([i["Current Club"] for i in all_players()])))
        players=st.selectbox("pich a player", [e["full_name"] for e in find_players_by_country(nationality)])
        st.text(find_players(players))
    if data == "Position":
        position=st.selectbox("pick team", list(set([i["position"] for i in all_players()])))
        players=st.selectbox("pich a player", [e["full_name"] for e in find_players_by_position(position)])
        st.text(find_players(players))
    if data == "Age":
        age=st.selectbox("pick team", list(set([i["age"] for i in all_players()])))
        players=st.selectbox("pich a player", [e["full_name"] for e in find_players_by_age(age)])
        st.text(find_players(players))
if seleccion=="Compare with another player":
    st.text("I'm working on it")

# --- Teams path ---

if seleccion == "against team":
    theteam=st.selectbox("pick first team", ([equipos["common_name"] for equipos in get_all_team()]))
    theteam2=st.selectbox("pick second team", ([equipos["common_name"] for equipos in get_all_team()]))
    data=[find_team(name) for name in [theteam, theteam2]]
    st.text(data)

if seleccion=="Compare":
    st.text("I'm working on it")

# --- Matches path ---

if seleccion=="Matches":
    st.text("I'm working on it")