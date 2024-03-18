from perfil import Usuario
import json

def crear_album(self, nombre, descripcion, portada, fecha, genero, tracklist):
        # Lógica para crear un álbum
        pass

def crear_playlist(self, titulo, descripcion, canciones):
        # Lógica para crear una playlist
        pass

class Cancion():
    def __init__(self, json):
        self.id = json["id"]
        self.nombre = json["name"]
        self.duration = json["duration"]
        self.likes = []
        self.link = json["link"]
        if "likes" in json: 
            self.likes = json["likes"]
        self.streams = 0
        if "streams" in json: 
            self.streams = json["streams"]
        
    def as_dict(self):
        info = {
            "id": self.id,
            "name": self.nombre,
            "duration": self.duration,
            "link": self.link,
            "likes": self.likes,
            "streams": self.streams
        }
        return info
        
class Album():
    def __init__(self, json):
        self.id = json["id"]
        self.nombre = json["name"]
        self.portada = json["cover"]
        self.descripcion = json["description"]
        self.genre = json["genre"]
        self.fecha = json ["published"]
        self.artista = json["artist"]
        self.tracklist = [Cancion(i) for i in json["tracklist"]]
        self.likes = []
        if "likes" in json: 
            self.likes = json["likes"]
    
    def as_dict(self):
        info = {
            "id": self.id,
            "name": self.nombre,
            "cover": self.portada,
            "description": self.descripcion,
            "genre": self.genre,
            "published": self.fecha,
            "artist": self.artista,
            "tracklist": [i.as_dict() for i in self.tracklist],
        }
        return info
    
    def __str__(self):
        return "Nombre: {},\n Genero: {},\n Publicado: {},\n Tracklist: {}".format(self.nombre, self.genre, self.fecha, '\n'.join([i.nombre for i in self.tracklist]))

class Playlist():
    def __init__(self, json):
        self.canciones = json["tracks"]
        self.id = json["id"]
        self.nombre = json["name"]
        self.descripcion=json["description"]
        self.creator=json["creator"]
        
    def as_dict(self):
        info = {
            "tracks": self.canciones,
            "id": self.id,
            "name": self.nombre,
            "description": self.descripcion,
            "creator":self.creator
        }
        return info
    
    def __str__(self):
        return "Nombre: {},\n Creador: {}".format(self.nombre, self.creator)