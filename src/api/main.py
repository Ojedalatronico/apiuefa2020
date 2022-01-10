from fastapi import FastAPI
from api.router import league,matches,general

app=FastAPI()

app.include_router(league.router)
app.include_router(matches.router)
app.include_router(general.router)

@app.get("/")
def root():
    return{"message": "Euro Api"}