from pydantic import BaseModel

class Song(BaseModel):
    song: str
    country: str
    autor: str
    rhythm: str
    section: str