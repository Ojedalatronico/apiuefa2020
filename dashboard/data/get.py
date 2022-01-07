from config.api import url
import requests

print(url)
def get_all_team():
    return requests.get(url+"/all_teams").json()

def find_team(team):
    q = {
        "common_name":team
    }
    return requests.get(url+"/find/team", params=q).json()

# --- players routers ---

def all_players():
    q = {
    }
    return requests.get(url+"/find/team", params=q).json()

# --- League routers ---

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