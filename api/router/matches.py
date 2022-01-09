from fastapi import APIRouter
from ..data.mongo import db
from bson import json_util
from json import loads
import ast
import pandas as pd

router = APIRouter()

def str_to_dict(variable:str):
    lista=[]
    result=df[variable]
    for i in range(len(result)):
        a=ast.literal_eval(result[i])
        lista.append(a)
    return lista

df=pd.DataFrame((db["UEFA"].find({})))

@router.get("/matches")
def all_matches():
    results = list(db["UEFA"].find({},{"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/matche/teams")
def all_matches_teams(stage):
    q={"stage":stage}
    p={"_id":0,"team_name_home":1,"team_name_away":1,"stage":1}
    results = list(db["UEFA"].find(q,p))
    return loads(json_util.dumps(results))

@router.get("/matche/team/stats")
def all_matches_teams(stage,team_name_home,team_name_away):
    q={"stage":stage,
        "team_name_home": team_name_home,
        "team_name_away": team_name_away}
    p={"_id":0,"team_name_home":1,"team_name_away":1,"stage":1,"pens":1,"pens_home_score":1,
        "pen_away_score":1,"possession_home":1,"possession_away":1,"total_shots_home":1,
        "total_shots_away":1,"shots_on_target_home":1,"shots_on_target_away":1,"duels_won_home":1,"duels_won_away":1
        }
    results = list(db["UEFA"].find(q,p))
    return loads(json_util.dumps(results))

@router.get("/stages")
def all_stages():
    results = list(db["UEFA"].find({},{"_id":0,"stage":1}))
    return loads(json_util.dumps(results))

@router.get("/pens")
def all_pens():
    results = list(db["UEFA"].find({},{"_id":0,"pens":1}))
    return loads(json_util.dumps(results))

@router.get("/events")
def all_Substitution():
    results = list(db["UEFA"].find({},{"_id":0,"events_list":1}))
    return loads(json_util.dumps(results))

@router.get("/event/substitution")
def all_substitution():
    return df["events_list"].to_json(orient = 'index')
    
@router.get("/lineup_home")
def all_lineup_home():
    results = list(db["UEFA"].find({},{"_id":0,"lineup_home":1}))
    return loads(json_util.dumps(results))

@router.get("/lineup_away")
def all_lineup_away():
    results = list(db["UEFA"].find({},{"_id":0,"lineup_away":1}))
    return loads(json_util.dumps(results))