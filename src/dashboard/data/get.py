from config.api import url
import requests

# --- General Statistics path ---

def league(season):
    q ={
        "season":season
    }
    return requests.get(url+"/league", params=q).json()
def goal_each_10(season):
    q ={
        "season":season
    }
    return requests.get(url+"/league/goals_each_10", params=q).json()
def goal_each_15(season):
    q ={
        "season":season
    }
    return requests.get(url+"/league/goals_each_15", params=q).json()


# --- Matches path ---

def all_matches():
    q={}
    return requests.get(url+"/matches", params=q).json()

def all_matches_teams(stage):
    q = {
        "stage":stage
    }
    return requests.get(url+"/matche/teams", params=q).json()

def team_rival(stage,team_name_home):
    q = {
        "stage":stage,
        "team_name_home":team_name_home
    }
    return requests.get(url+"/matche/rival", params=q).json()

def stats_home(stage,team_name_home):
    q = {
        "stage":stage,
        "team_name_home":team_name_home,
    }
    return requests.get(url+"/home/stats", params=q).json()

def stats_away(stage,team_name_home):
    q = {
        "stage":stage,
        "team_name_home":team_name_home
    }
    return requests.get(url+"/away/stats", params=q).json()

# --- General path ---
def general():
    q={}
    return requests.get(url+"/general", params=q).json()