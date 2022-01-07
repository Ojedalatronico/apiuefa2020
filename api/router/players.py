from fastapi import APIRouter
from ..data.mongo import db
from fastapi.encoders import jsonable_encoder
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/players")
def all_players():
    results = list(db["uefa2020_players"].find({}))
    return loads(json_util.dumps(results))

    
