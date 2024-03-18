class Interaccion:
    def __init__(self, usuario, item):
        self.usuario = usuario
        self.item = item

class Like(Interaccion):
    def __init__(self, usuario, item):
        super().__init__(usuario, item)

class Reproduccion(Interaccion):
    def __init__(self, usuario, cancion):
        super().__init__(usuario, cancion)