import vlc
import time
from threading import Thread
from os import environ, listdir
from os import remove

mediaPlayer = vlc.MediaPlayer("")



def play_song(path:str):
    global mediaPlayer
    media = vlc.Media(path) 
    mediaPlayer.set_media(media)
    mediaPlayer.audio_set_volume(60)
    # start playing video
    mediaPlayer.play()

    mediaPlayer.get_media().parse()
    song = mediaPlayer.get_media().get_meta(0)
    author = mediaPlayer.get_media().get_meta(1)
    album = mediaPlayer.get_media().get_meta(4)
    current_song = f"{author} - {song} ({album})"
    cursongfilepath=environ['STREAM_PATH']
    f = open(f"{cursongfilepath}cursong.txt","+w")
    f.write(current_song)
    f.close()
    while mediaPlayer.is_playing():
        time.sleep(1)

class Song:
    def __init__(self, title, position):
      self.title=title
      self.position=position

class Player:
    mediaPlayer=None

    def __init__(self) -> None:
        self.current=0
        self.thread=None

    def _get_current_songs(self):
        song_dir= environ['SONG_DIR']
        songList=[]

        songs=listdir(song_dir);
        for s in songs:
          songList.append(Song(s,songs.index(s)))
        return songList
    
    def _delete_song(self,index):
        songs= self._get_current_songs()
        remove(songs[index])

    def addSong(self, path:str) -> None:
       pass
    
    def deleteSong(self, index:int) -> None:
        if(index>=len(self._get_current_songs)):
            raise ValueError("index Out of bounds")
        self.songs.remove(self.songs[index])
    
    def get_songs(self) -> list[str]:
        return self._get_current_songs()

    def play(self, index:int) -> str:
        if(index >= len(self._get_current_songs())):
           raise ValueError("index Out of bounds")
        song = environ['SONG_DIR']+self._get_current_songs()[index].title
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
        self.play(self.current % len(self._get_current_songs()))
    def prev(self) -> None:
        mediaPlayer.stop()
        self.current=self.current-1
        self.play(self.current % len(self._get_current_songs()))


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