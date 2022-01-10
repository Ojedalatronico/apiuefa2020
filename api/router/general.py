from fastapi import APIRouter
from ..data.mongo import db
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/general")
def general():
    results = list(db["GENERAL"].find({},{"_id":0}))
    return loads(json_util.dumps(results))