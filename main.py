from fastapi import FastAPI, HTTPException
from model import Song

app=FastAPI()

from database import(
    fetch_all_songs,
    create_song
)

@app.get("/")
async def index():
    return "Hello World!"

@app.get("/songs")
async def all_songs():
    response=await fetch_all_songs()
    return response

@app.post("/songs")
async def addsong(song: Song):
    #response=await create_song(song.dict())
    response=await create_song(dict(song))
    if response:
        return song
    raise HTTPException(400,"Failed to add song!")