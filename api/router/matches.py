from fastapi import APIRouter
from ..data.mongo import db
from fastapi.encoders import jsonable_encoder
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/matches")
def all_matches():
    results = list(db["uefa2020_results"].find({}))
    return loads(json_util.dumps(results))
