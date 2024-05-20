import vlc
import time
from threading import Thread

mediaPlayer = vlc.MediaPlayer("")

def play_song(path:str):
    global mediaPlayer
    media = vlc.Media(path) 
    mediaPlayer.set_media(media)
    mediaPlayer.audio_set_volume(30)
    # start playing video
    mediaPlayer.play()

    mediaPlayer.get_media().parse()
    song = mediaPlayer.get_media().get_meta(0)
    author = mediaPlayer.get_media().get_meta(1)
    album = mediaPlayer.get_media().get_meta(4)
    current_song = f"{author} - {song} ({album})"
    f = open("E:\stream\cursong.txt","+w")
    f.write(current_song)
    f.close()
    while mediaPlayer.is_playing():
        time.sleep(1)

class Player:
    mediaPlayer=None

    def __init__(self) -> None:
        self.songs=[]
        self.current=0
        self.thread=None

    def addSong(self, path:str) -> None:
        self.songs.append(path)
    
    def deleteSong(self, index:int) -> None:
        if(index>=len(self.songs)):
            raise ValueError("index Out of bounds")
        self.songs.remove(self.songs[index])
    
    def get_songs(self) -> list[str]:
        return self.songs

    def play(self, index:int) -> str:
        if(index >= len(self.songs)):
           raise ValueError("index Out of bounds")
        song = self.songs[index]
        print(song)
        self.thread= Thread(target=play_song, args=[song])
        self.thread.start()
        return song
    
    def stop(self)-> None:
        if self.thread is not None:
            mediaPlayer.stop()
    
    def next(self) -> None:
        mediaPlayer.stop()
        self.current=self.current+1
        self.play(self.current % len(self.songs))
    def prev(self) -> None:
        mediaPlayer.stop()
        self.current=self.current-1
        self.play(self.current % len(self.songs))


if __name__ == '__main__':
    p = Player()
    p.addSong("E:\\stream\\canciones\\mitch murder - outride a crisis.mp3")
    p.addSong("E:\stream\\canciones\\Out Run Remix - Splash Wave Remix Synthwave _ Retrowave _ OutRun_mE6DAja2xNs.mp3")
    p.play(0)
    time.sleep(10)
    p.next()
    time.sleep(10)
    p.prev()
    time.sleep(5)
    p.stop()