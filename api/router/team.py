from fastapi import APIRouter
from ..data.mongo import db
from fastapi.encoders import jsonable_encoder
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/find/team")
def find_team(common_name):
    results = list(db["uefa2020_teams"].find({"common_name":common_name}))
    return loads(json_util.dumps(results))


@router.get("/team")
def team_rout():
    return{"message": "Equipos de la EURO cup"}

@router.get("/team/{common_name}")
def get_team(common_name):
    results = db["uefa2020_teams"].find({"common_name": common_name})
    return loads(json_util.dumps(results))

    
@router.get("/all_teams")
def all_team():
    results = db["uefa2020_teams"].find({},{"_id":0,"common_name":1})
    return loads(json_util.dumps(results))
