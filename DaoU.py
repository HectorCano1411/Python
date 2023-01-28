from clases.Usuario import Usuario
from conex.logger_base import log
from conex.conexion import   Conexion

class DAOU:
    '''
    DAO - Data Access Object
    CRUD - Create -Read - Update - Delete
    '''
    
    _SELECCIONAR    = 'SELECT * FROM  usuario ORDER BY id_usuario'
    _INSERTAR       = 'INSERT INTO usuario(nombre,password) VALUES (%s, %s)'
    _ACTUALIZAR     = 'UPDATE USUARIO SET  nombre=%s , password=%s WHERE id_usuario=%s'
    _ELIMINAR       = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                usuarios= []
                for registro in registros:
                    usuario = Usuario(registro[0], registro[1], registro[2])
                    usuarios.append(usuario)
                return usuarios
            
        
    @classmethod
    def insertar(cls, usuario):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = ( usuario.nombre, usuario.password)
                cursor.execute(cls._INSERTAR, (valores))
                conexion.commit()
                log.debug(f' Usuario insertado: {usuario}')
                return cursor.rowcount
    @classmethod
    def actualizar(cls, usuario):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.nombre, usuario.password, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug(f'Usuario actualizado : {usuario}')
                return cursor.rowcount
            
    @classmethod
    def eliminar(cls, usuario):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR, valores)
                conexion.commit()
                log.debug(f' Usuario Eliminado: {usuario}')
                return cursor.rowcount