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

# --- players routers ---

"""def find_players(full_name):
    q = {"full_name":full_name

    }
    return requests.get(url+"/look/players", params=q).json()
def find_players_by_country(nationality):
    q = {
        "nationality":nationality
    }
    return requests.get(url+"/lookbycountry/players", params=q).json()
def all_players():
    q = {
    }
    return requests.get(url+"/players", params=q).json()
def find_players_by_position(position):
    q = {
        "position":position
    }
    return requests.get(url+"/lookbyposition/players", params=q).json()
def find_players_by_age(age):
    q = {
        "age":age
    }
    return requests.get(url+"/lookbyage/players", params=q).json()"""

# --- Teams path ---
"""def get_all_team():
    return requests.get(url+"/all_teams").json()
def find_team(team):
    q = {
        "common_name":team
    }
    return requests.get(url+"/find/team", params=q).json()"""

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