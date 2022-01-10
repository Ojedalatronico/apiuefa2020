from fastapi import APIRouter
from ..data.mongo import db
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/league")
def league(season):
    p={"_id":0,"season":1,
    "number_of_clubs":1,"total_matches":1,"average_goals_per_match":1,"btts_percentage":1,"clean_sheets_percentage":1,"average_corners_per_match":1,"total_corners_for_season":1,
    "average_cards_per_match":1,"total_cards_for_season":1}
    results = list(db["euro2020_league"].find({"season":season},p))
    return loads(json_util.dumps(results))

@router.get("/league/goals_each_10")
def goal_each_10(season):
    p={"_id":0,"goals_min_0_to_10":1,"goals_min_11_to_20":1,"goals_min_21_to_30":1,
    "goals_min_31_to_40":1,"goals_min_41_to_50":1,"goals_min_51_to_60":1,"goals_min_61_to_70":1,"goals_min_71_to_80":1,"goals_min_81_to_90":1}
    results = db["euro2020_league"].find({"season":season},p)
    return loads(json_util.dumps(results))

@router.get("/league/goals_each_15")
def goal_each_15(season):
    p={"_id":0,"goals_min_0_to_15":1,
    "goals_min_16_to_30":1,"goals_min_31_to_45":1,"goals_min_46_to_60":1,"goals_min_61_to_75":1,"goals_min_76_to_90":1}
    results = db["euro2020_league"].find({"season":season},p)
    return loads(json_util.dumps(results))
