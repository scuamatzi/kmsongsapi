from pydantic import BaseModel

class Song(BaseModel):
    song_name: str
    country: str
    author: str
    rhythm: str
    section: str
    letter: str
    chords: str
    track: str