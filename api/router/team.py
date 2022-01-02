from fastapi import APIRouter
from ..data.mongo import db
from fastapi.encoders import jsonable_encoder

router = APIRouter()
@router.get("/team")
def team_rout():
    return{"message": "Equipos de la EURO cup"}

@router.get("/team/{common_name}")
def get_team(common_name):
    results = db["uefa2020_teams"].find({"common_name": common_name})
    return jsonable_encoder(results)
