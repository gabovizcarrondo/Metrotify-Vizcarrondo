from server import poblar
import json
from perfil import Musico, Escucha
from musica import Cancion, Album
import webbrowser

def crear_usuario(usuarios):
    nombre=input("Nombre del usuario: ")
    email=input("Correo electronico: ")
    artista=input("Es artista?: ")
        
    info = {
        "id": "0000",
        "name": nombre,
        "email": email,    
    }
    if artista == "si":
        usuarios.append(Musico(info))
    else:
        usuarios.append(Escucha(info))

def crear_cancion():
    name=input("Nombre: ")
    duration=input("Duracion en minutos: ")
    link=input("Link de la cancion: ")
    info = {
        "id": "0000",
        "name": name,
        "duration": duration,  
        "link": link,  
        "streams": 0
    }
    return info
      
def crear_album(albums, logged_id):
    name=input("Nombre del album: ")
    cover=input("Link de portada: ")
    description=input("Descripcion: ")
    published=input("Fecha de publicacion:")
    genre=input("Genero del album: ")
    tracklist=[]
    while True:
        tracklist.append(crear_cancion())
        input("Quieres añadir otra cancion?(S/N) ")
        if  input().lower() != 'no':
            break
        
    info = {
        "id": "0000",
        "name": name,
        "cover": cover,  
        "description": description, 
        "published": published,
        "genre": genre,
        "tracklist": tracklist,
        "artist":logged_id
    }
    albums.append(Album(info))

def buscar_album(albums):
    name=input("Nombre del album: ")
    try:
        album_buscado=albums[[i.nombre for i in albums].index(name)]
        print (str(album_buscado))
        return
    except:
        print("No existe el album")
        return
    
def buscar_cancion(albums, logged_id):
    canciones = sum([i.tracklist for i in albums], [])
    name=input("Nombre de la cancion: ")
    try:
        album_index = [name in [j.nombre for j in i.tracklist] for i in albums].index(True)
        canciones_index = [i.nombre for i in albums[album_index].tracklist].index(name)
        cancion_buscada=albums[album_index].tracklist.pop(canciones_index)
        while True:
            x = input("1. Escuchar cancion\n2. Dar like\n3. Salir\n")
            if x=='1': 
                cancion_buscada.streams+=1
                webbrowser.open(cancion_buscada.link)
                return "Escuchaste la cancion"
            elif x=='2':
                cancion_buscada.likes.append(logged_id)
                cancion_buscada.likes = list(set(cancion_buscada.likes))
                print("Le diste like a la cancion")
            elif x=='3':
                albums[album_index].tracklist.append(cancion_buscada)
                return
            else: print ("Opcion no valida")
    except:
        print("No existe la cancion")
        return

def buscar_usuario(usuarios):
    name=input("Nombre del usuario: ")
    try:
        usuario_buscado=usuarios[[i.nombre for i in usuarios].index(name)]
        print (str(usuario_buscado))
        return
    except:
        print("No existe el usuario")
        return
    
def buscar_playlist(playlists):
    name=input("Nombre de la playlist: ")
    try:
        playlist_buscada=playlists[[i.nombre for i in playlists].index(name)]
        print (str(playlist_buscada))
        while True:
            datos = input("1. Escuchar cancion\n2. Dar like")
        return
    except:
        print("No existe la playlist")
        return

def borrar_datos(usuarios,logged_id):
    usuarios.pop([i.id for i in usuarios].index(logged_id))
    print("Usuario borrado con exito")
    with open("user.json", "w", encoding="utf-8") as user_json, open("album.json", "w") as albums_json, open("playlist.json", "w") as playlist_json:
        json.dump([i.as_dict() for i in usuarios], user_json)
        json.dump([i.as_dict() for i in albums], albums_json)
        json.dump([i.as_dict() for i in playlists], playlist_json)
    quit()

usuarios, albums, playlists=poblar()

while True:
    name=input("Nombre del usuario: ")
    try:
        usuario_buscado=usuarios[[i.nombre for i in usuarios].index(name)]
        logged_id=usuario_buscado.id
        break
    except:
        print("No existe el usuario")
        continue

while  True:
    datos_input = input("Bienvenido/a\n1. Crear\n2. Buscar\n3. Ver estadisticas\n4. Cambiar datos de cuenta\n5. Borrar cuenta\n6. Salir\n\nQue desea hacer? ")
    if datos_input=="1":
        x=input("1. Crear usuario\n2. Crear album\n")
        if  x == "1":
            crear_usuario(usuarios)
        if x =="2":
            crear_album(albums)
        pass
    elif  datos_input=="2":
        x=input("1. Buscar album\n2. Buscar Cancion\n3. Buscar Usuario\n4.Buscar Playlist\n")
        if  x == "1":
            buscar_album(albums)
        if x =="2":
            buscar_cancion(albums, logged_id)
        if x == "3":
            buscar_usuario(usuarios)
        if x=="4":
            buscar_playlist(playlists)
        pass
    elif  datos_input=="3":
        pass
    elif  datos_input=="4":
        pass
    elif  datos_input=="5":
        borrar_datos(usuarios,logged_id)
        pass
    elif datos_input=="6":
        with open("user.json", "w", encoding="utf-8") as user_json, open("album.json", "w") as albums_json, open("playlist.json", "w") as playlist_json:
            json.dump([i.as_dict() for i in usuarios], user_json)
            json.dump([i.as_dict() for i in albums], albums_json)
            json.dump([i.as_dict() for i in playlists], playlist_json)
        quit()
    else:
        print("Opcion no valida. Por favor ingresa una opcion del menu.")
        continue