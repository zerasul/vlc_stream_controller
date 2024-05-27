from fastapi import FastAPI,Response,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from player import Player

origins = [
    'http://localhost:3000'
]

player = Player()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Song(BaseModel):
    name:str

@app.get("/api/songs")
async def getSongs(request=Request):
    return player.get_songs()

@app.post("/api/songs")
async def addSong(song:Song):
    player.addSong(song.path)
    return {"song": song.path}

@app.get("/api/play/{index}")
async def play(index:int):
    return player.play(index)

@app.get("/api/stop")
async def stop():
    return player.stop()

@app.get("/api/next")
async def next():
    return player.next()

@app.get("/api/prev")
async def prev():
    return player.prev()




