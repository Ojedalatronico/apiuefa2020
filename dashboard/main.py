import streamlit as st
from streamlit.stats import StatsManager
from sections import sidebar
from data.get import *
from data.usefully import *
import pandas as pd
import matplotlib.pyplot as plt

seleccion=sidebar.create()
pd.DataFrame()
st.title("UEFA EURO 2020")
st.text("We are working now :)")

# --- Matches path ---

if seleccion=="General stats":

    st.text("patata")
    

if seleccion=="individual matches":
    stage=st.selectbox("What stage do you want to see?", list(set([i["stage"] for i in all_matches()])))
    estadisticas = st.selectbox("What stats do you want to see?", ["goals and shots","possession"])
    column1,column2 = st.columns(2)
    with column1:
        team = st.selectbox("Select a team",list(set([i["team_name_home"] for i in all_matches_teams(stage)])))
    with column2:
        team2 = st.selectbox("Select its rival", list(set([i["team_name_away"] for i in team_rival(stage,team)])))
    home=stats_home(stage,team)[0]
    away=stats_away(stage,team)[0]
    if estadisticas =="goals and shots":
        with column1:
            st.text(f"{team} did {home['team_home_score']} goals")
            st.text(f"{team} did {home['shots_on_target_home']} shots on target")
            st.text(f"{team} did {home['total_shots_home']} shots")
            st.pyplot(goles(home["total_shots_home"],home["shots_on_target_home"],home["team_home_score"]))
        with column2:
            st.text(f"{team2} did {away['team_away_score']} goals")
            st.text(f"{team2} did {away['shots_on_target_away']} shots on target") 
            st.text(f"{team2} did {away['total_shots_away']} shots")   
            st.pyplot(goles(away["total_shots_away"],away["shots_on_target_away"],away["team_away_score"]))
    if estadisticas =="possession":
        st.pyplot(possession(home["possession_home"],away["possession_away"],team,team2))


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
"""
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
"""
# --- Teams path ---

"""if seleccion == "against team":
    theteam=st.selectbox("pick first team", ([equipos["common_name"] for equipos in get_all_team()]))
    theteam2=st.selectbox("pick second team", ([equipos["common_name"] for equipos in get_all_team()]))
    data=[find_team(name) for name in [theteam, theteam2]]
    st.text(data)
if seleccion=="Compare":
    st.text("I'm working on it")
"""