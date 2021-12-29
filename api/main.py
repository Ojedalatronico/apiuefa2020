import streamlit as st
from fastapi import FastAPI
from routers import equipos

app=FastAPI()

app.include_router(equipos.router)

st.title("UEFA EURO 2020")
st.text("We are working now :)")
