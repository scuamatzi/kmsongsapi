from model import Song
from pymongo import MongoClient
import json
import pprint
import re

file=open("pass.json", mode="r")
data=json.load(file)
user=data["user"]
password=data["password"]
uri=data["uri"]
file.close

try:
    client=MongoClient("mongodb://km:kmpassword@192.168.50.30")
    print("Database Connection Successful!")
except:
    raise("Database connection failed!")

db=client.kmsongs
collection=db.songs

async def fetch_all_songs():
    songs=[]
    db_result=collection.find()
    for item in db_result:
        songs.append(Song(**item))
    return songs

async def create_song(song):
    result = collection.insert_one(song)
    return song

async def fetch_song(song_name):
    ## This way it finds the exact song_name text
    result=collection.find_one({"song_name": re.compile('^'+ re.escape(song_name) + '$', re.IGNORECASE)})

    ## This way it finds name songs that include song_name text
    #result=collection.find_one({"song": re.compile( re.escape(item) , re.IGNORECASE)})

    if result:
        return Song(**result)
    else:
        return None

async def delete_song(song_name):
    collection.delete_one({"song_name": re.compile('^'+re.escape(song_name)+'$', re.IGNORECASE) })
    return True