from fastapi import FastAPI
from bson import json_util
from json import loads
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
user=os.getenv("MONGO_USER")
password=os.getenv("MONGO_PASS")

URL=f"mongodb+srv://{user}:{password}@uefa.kgpdy.mongodb.net"

db=MongoClient(URL).get_database("Project")
app=FastAPI()

@app.get("/")
def root():
    return{"message": "Euro Api"}

@app.get("/league")
def league(season):
    p={"_id":0,"season":1,
    "number_of_clubs":1,"total_matches":1,"average_goals_per_match":1,"btts_percentage":1,"clean_sheets_percentage":1,"average_corners_per_match":1,"total_corners_for_season":1,
    "average_cards_per_match":1,"total_cards_for_season":1}
    results = list(db["euro2020_league"].find({"season":season},p))
    return loads(json_util.dumps(results))

@app.get("/league/goals_each_10")
def goal_each_10(season):
    p={"_id":0,"goals_min_0_to_10":1,"goals_min_11_to_20":1,"goals_min_21_to_30":1,
    "goals_min_31_to_40":1,"goals_min_41_to_50":1,"goals_min_51_to_60":1,"goals_min_61_to_70":1,"goals_min_71_to_80":1,"goals_min_81_to_90":1}
    results = db["euro2020_league"].find({"season":season},p)
    return loads(json_util.dumps(results))

@app.get("/league/goals_each_15")
def goal_each_15(season):
    p={"_id":0,"goals_min_0_to_15":1,
    "goals_min_16_to_30":1,"goals_min_31_to_45":1,"goals_min_46_to_60":1,"goals_min_61_to_75":1,"goals_min_76_to_90":1}
    results = db["euro2020_league"].find({"season":season},p)
    return loads(json_util.dumps(results))

@app.get("/players")
def all_players():
    results = list(db["uefa2020_players"].find({},{"_id":0,"full_name":1, "Current Club":1,"position":1,"age":1}))
    return loads(json_util.dumps(results))

@app.get("/look/players")
def look_player(full_name):
    results = list(db["uefa2020_players"].find({"full_name":full_name},{"_id":0}))
    return loads(json_util.dumps(results))

@app.get("/lookbycountry/players")
def player_lookbycountry(nationality):
    results = list(db["uefa2020_players"].find({"Current Club":nationality},{"_id":0,"full_name":1,"Current Club":1}))
    return loads(json_util.dumps(results))

@app.get("/lookbyposition/players")
def player_lookbycountry(position):
    results = list(db["uefa2020_players"].find({"position":position},{"_id":0,"full_name":1,"position":1}))
    return loads(json_util.dumps(results))

@app.get("/lookbyage/players")
def player_lookbyage(age):
    results = list(db["uefa2020_players"].find({"age":age},{"_id":0,"full_name":1,"age":1}))
    return loads(json_util.dumps(results))


@app.get("/find/team")
def find_team(common_name):
    results = list(db["uefa2020_teams"].find({"common_name":common_name}))
    return loads(json_util.dumps(results))

@app.get("/team/{common_name}")
def get_team(common_name):
    results = db["uefa2020_teams"].find({"common_name": common_name})
    return loads(json_util.dumps(results))

    
@app.get("/all_teams")
def all_team():
    results = db["uefa2020_teams"].find({},{"_id":0,"common_name":1})
    return loads(json_util.dumps(results))
