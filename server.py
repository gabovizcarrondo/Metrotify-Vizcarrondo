import json
from musica import Cancion, Album, Playlist
from perfil import Musico, Escucha
import urllib.request

def poblar():
    try:
        with open("user.json", "r", encoding="utf-8") as user_json, open("album.json", "r") as albums_json, open("playlist.json", "r") as playlist_json:
            pass
    except FileNotFoundError:
        a=json.loads(urllib.request.urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json").read())
        b=json.loads(urllib.request.urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json").read())
        c=json.loads(urllib.request.urlopen("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json").read())
        with open("user.json", "w", encoding="utf-8") as user_json, open("album.json", "w") as albums_json, open("playlist.json", "w") as playlist_json:
            json.dump(c, user_json)
            json.dump(a, albums_json)
            json.dump(b, playlist_json)
            
    with open("user.json", "r", encoding="utf-8") as user_json, open("album.json", "r") as albums_json, open("playlist.json", "r") as playlist_json:
        x = json.load(user_json)
        users = []
        for i in x:
            if i["type"] == "musician":
                users.append(Musico(i))
            else:
                users.append(Escucha(i))
                
        x = json.load(playlist_json)
        playlist = []
        for i in x:
                playlist.append(Playlist(i))
                
        x = json.load(albums_json)
        albums = []
        for i in x:
                albums.append(Album(i))
                
        return (users,albums,playlist)