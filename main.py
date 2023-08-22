from fastapi import FastAPI 
from model import Song

app=FastAPI()

from database import(
    fetch_all_songs
)

@app.get("/")
async def index():
    return "Hello World!"

@app.get("/songs")
async def all_songs():
    response=await fetch_all_songs()
    return response