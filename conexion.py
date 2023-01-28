from conex.logger_base import log
import mysql.connector as conn
import sys



#import mysql.connector

class Conexion:

    _DATABASE   ='eva3'
    _USER       ='root'
    _PASSWORD   =''
    _DB_PORT    = '3307'
    _HOST       ='localhost'
    _conexion   = None
    _cursor     = None

    @classmethod
    def obtenerConexion(cls):
        #if cls._conexion is None:
            try:
                cls._conexion = conn.connect(host      = cls._HOST,
                                            user       = cls._USER, 
                                            passwd     = cls._PASSWORD, 
                                            port       = cls._DB_PORT,
                                            database   = cls._DATABASE )
                log.debug(f'Conexion exitosa : {cls._conexion}')
                return cls._conexion    
                
            except Exception as e :
                log.error(f'ocurrio una excepción al obtener la conexión: {e}')
                sys.exit()
                
        #else:
            return cls._conexion
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f' se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
                
            except Exception as e :
                log.error(f'ocurrio una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor
        
        

                
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()