from fastapi import FastAPI,Response,Request
from pydantic import BaseModel
from player import Player

player = Player()
app = FastAPI()

class Song(BaseModel):
    path:str

@app.get("/api/songs")
def get_random_gif(request=Request):
    return player.songs

@app.post("/api/songs")
def get_gif(song:Song):
    player.addSong(song.path)
    return {"song": song.path}

@app.get("/api/play/{index}")
def play(index:int):
    return player.play(index)

@app.get("/api/stop")
def stop():
    return player.stop()

@app.get("/api/next")
def next():
    return player.next()

@app.get("/api/prev")
def prev():
    return player.prev()




