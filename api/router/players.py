from fastapi import APIRouter
from ..data.mongo import db
from fastapi.encoders import jsonable_encoder
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/players")
def all_players():
    results = list(db["uefa2020_players"].find({},{"_id":0,"full_name":1, "nationality":1}))
    return loads(json_util.dumps(results))

@router.get("/look/players")
def look_player(full_name):
    results = list(db["uefa2020_players"].find({"full_name":full_name},{"_id":0}))
    return loads(json_util.dumps(results))

@router.get("/lookbycountry/players")
def player_lookbycountry(nationality):
    results = list(db["uefa2020_players"].find({"nationality":nationality},{"_id":0,"full_name":1,"nationality":1}))
    return loads(json_util.dumps(results))