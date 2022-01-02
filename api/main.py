from fastapi import FastAPI
from .router import team


app=FastAPI()

app.include_router(team.router)

@app.get("/")
def root():
    return{"message": "Euro Api"}