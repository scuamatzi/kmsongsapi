from fastapi import FastAPI, HTTPException
from model import Song
import pprint

app=FastAPI()

from database import(
    fetch_all_songs,
    create_song,
    fetch_song
)

# @app.get("/{song_name}")
# async def one_song(song_name:str):
#     response=await fetch_song(song_name)
#     if response:
#         return response
#     raise HTTPException(400, "Song not found.")
#     #return dict(response)

@app.get("/")
async def index():
    return "Hello World!"

@app.get("/songs", response_model=list[Song])
async def all_songs():
    response=await fetch_all_songs()
    return response

@app.post("/songs")
async def addsong(song: Song):
    result=await fetch_song(song.song)
    if result:
        raise HTTPException(400, f"This song '{song.song}' is already in database" )

    response=await create_song(dict(song))
    if response:
        return song
    raise HTTPException(400,"Failed to add song!")