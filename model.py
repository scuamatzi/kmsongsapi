from pydantic import BaseModel

class Song(BaseModel):
    song: str
    country: str
    author: str
    rhythm: str
    section: str