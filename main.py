from fastapi import FastAPI
from api.router import players,team,league

app=FastAPI()

app.include_router(team.router)
app.include_router(league.router)
app.include_router(players.router)

@app.get("/")
def root():
    return{"message": "Euro Api"}