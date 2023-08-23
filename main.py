from fastapi import FastAPI, HTTPException
from model import Song
import pprint

app=FastAPI()

from database import(
    fetch_all_songs,
    create_song,
    fetch_song,
    delete_song,
    update_todo
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
    result=await fetch_song(song.song_name)
    if result:
        raise HTTPException(400, f"This song '{song.song_name}' is already in database" )

    response=await create_song(dict(song))
    if response:
        return song
    raise HTTPException(400,"Failed to add song!")

@app.put("/songs")
async def put_song(song: Song):
    response=await fetch_song(song.song_name)
    if not response:
        raise HTTPException(400, f"Song '{song.song_name} is not in database.'")
    result=await update_todo(song)
    return result

@app.delete("/songs")
async def remove_song(song_name: str):
    song_exist=await fetch_song(song_name)
    if not song_exist:
        raise HTTPException(400, f"The song '{song_name}' doesn't exist in database")
    
    result=await delete_song(song_name)
    return f"{song_name} deleted."