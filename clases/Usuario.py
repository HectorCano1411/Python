class Usuario:
    
    def __init__(self, id_usuario = None, nombre = None , password = None):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._password = password
        
    def __str__(self):
        return f' Usuario: {self._id_usuario} {self._nombre} {self._password}'    
        
    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password
        
    