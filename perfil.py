import json

class Usuario():
    def __init__(self,json):
        self.id=json["id"]
        self.nombre=json['name']
        self.correo=json['email'] 
        
    def as_dict(self):
        info = {
            "id": self.id,
            "name": self.nombre,
            "email": self.correo,
        }
        return info
    
    def __str__(self):
        return "Nombre: {},\n Correo: {}".format(self.nombre, self.correo)
        
class Escucha (Usuario):

    def as_dict(self):
        info = {
            "id": self.id,
            "name": self.nombre,
            "email": self.correo,
            "type":"listener",
        }
        return info
        
class Musico (Usuario):
    def _init_(self, json):
        super().__init__(json)
        self.likes = []
        if "likes" in json: 
            self.likes = json["likes"]

    def as_dict(self):
        info = {
            "id": self.id,
            "name": self.nombre,
            "email": self.correo,
            "type":"musician",
            
        }
        return info
        
# Función auxiliar para insertar un nuevo usuario en la tabla Usuario
    def agregar_usuario(nombre, correo, contrasena):
     pass

    def buscar_perfil(self, filtro):
        # Lógica para buscar el perfil en función del filtro
        pass

    def cambiar_info_personal(self):
        # Lógica para cambiar la información personal del usuario
        pass

    def borrar_datos(self):
        # Lógica para borrar los datos del usuario
        pass

    def ver_perfil(self, otro_usuario):
        # Lógica para ver la información del perfil de otro usuario
        pass