from model import Song
from pymongo import MongoClient
import json
import pprint

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
    item=song
    #result = await collection.insert_one(item)
    result = collection.insert_one(item)
    return item