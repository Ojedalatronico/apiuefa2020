import streamlit as st
from sections import sidebar
from data.usefully import *
from data.get import *
import pandas as pd
import streamlit as st

seleccion=sidebar.create()
pd.DataFrame()
st.title("UEFA EURO 2020")
st.text("We are working now :)")

# --- Matches path ---
def general_stats(individual_home,individual_away,total,average,data):
    shots= sumalista([i[individual_home] for i in all_matches()],[i[individual_away] for i in all_matches()])
    partidovs=partido([i["team_name_home"] for i in all_matches()],[i["team_name_away"] for i in all_matches()])
    st.text(f"En toda la euro hubieron {generals[total]} {data}, eso es un average de {generals[average]} {data} por partido")
    st.text("El gráfico muestra lo muestra por cada partido")
    return bar_shots(shots,partidovs)

if seleccion=="General stats":
    generals=general()[0]
    data=st.selectbox("What data do you want to see?", ["shots","shots on target", "goals","yellow cards","red cards"] )
    if data=="shots":
        st.pyplot(general_stats("total_shots_home","total_shots_away","total_shots","average_shots",data))
    if data=="shots on target":
        st.pyplot(general_stats("shots_on_target_home","shots_on_target_away","total_shots_on_target","average_shots_on_targe",data))
    if data=="goals":
        st.pyplot(general_stats("team_home_score","team_away_score","total_goals","average_goals",data))
    if data=="yellow cards":
        st.pyplot(general_stats("yellow_cards_home","yellow_cards_away","total_yellow_cards","average_yellow_cards",data))
    if data=="red cards":
        st.pyplot(general_stats("red_cards_home","red_cards_away","total_red_cards","average_red_cards",data))
if seleccion=="individual matches":
    stage=st.selectbox("What stage do you want to see?", list(set([i["stage"] for i in all_matches()])))
    estadisticas = st.selectbox("What stats do you want to see?", ["goals and shots","possession","cards"])
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
    if estadisticas =="cards":
         with column1:
            st.text(f"{team} got {home['yellow_cards_home']} yellow cards")
            st.text(f"and {team} got {home['red_cards_home']} red cards")
         with column2:
            st.text(f"{team2} got {away['yellow_cards_away']} yelow card")
            st.text(f"and {team2} got {away['red_cards_away']} red cards") 
# --- General Statistics path ---

if seleccion== "See a year":
    data=st.selectbox("Select a year", ["2020","2016"])
    df=pd.DataFrame(league(data)).transpose()
    st.dataframe(df)
    box=st.selectbox("Do you want to see totals goals each 10 min or 15 min", ["10 min","15 min"])
    st.pyplot(bar_chart_goals(data,box))
if seleccion=="Compare years":
    st.text("Not for now :(")

