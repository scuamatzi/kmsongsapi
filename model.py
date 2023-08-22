from pydantic import BaseModel

class Song(BaseModel):
    song: str
    country: str
    autor: str
    rythm: str
    section: str