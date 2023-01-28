from clases.Aracnido import Aracnido
from conex.logger_base import log
from conex.conexion import   Conexion



class DAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR    = 'SELECT * FROM aracnido3 ORDER BY id_aracnido'
    _INSERTAR       = 'INSERT INTO aracnido3 ( veneno, columna_vertebral, morder, telaraña ) VALUES( %s, %s,%s,%s)'
    _ACTUALIZAR     = 'UPDATE aracnido3 SET  veneno=%s , columna_vertebral=%s, morder=%s, telaraña=%s WHERE id_aracnido=%s'
    _ELIMINAR       = 'DELETE FROM aracnido3 WHERE id_aracnido=%s'
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                aracnidos = []
                for registro in registros:
                    aracnido = Aracnido(registro[0], registro[1], registro[2],registro[3],registro[4])
                    aracnidos.append(aracnido)
                return aracnidos

    @classmethod
    def insertar(cls, aracnido):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (aracnido.veneno, aracnido.columna_vertebral, aracnido.morder,aracnido.telaraña)
                cursor.execute(cls._INSERTAR, valores )
                conexion.commit()
                log.debug(f'Aracnido insertado: {aracnido}')
                return cursor.rowcount
            
            
    @classmethod
    def actualizar(cls, aracnido):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = ( aracnido.veneno, aracnido.columna_vertebral, aracnido.morder, aracnido.telaraña, aracnido.id_aracnido)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug(f'Aracnido actualizado : {aracnido}')
                return cursor.rowcount
                
                
    @classmethod
    def eliminar(cls, aracnido):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (aracnido.id_aracnido,)
                cursor.execute(cls._ELIMINAR, valores)
                conexion.commit()
                log.debug(f' Objeto Eliminado: {aracnido}')
                return cursor.rowcount
            
            
    



if __name__ == "__main__":    
   
    #INSERTAR
    aracnido = Aracnido(  veneno =' de araña tigre ', columna_vertebral = ' no tiene ', morder = ' muy fuerte ', telaraña =' bastante ')
    aracnido_insertado = DAO.insertar(aracnido)
    log.debug(f'aracnidos insertados: {aracnido_insertado}')
    
    
    #Actualizar un regiistro
    aracnido1 = Aracnido(6,  ' de araña  pollito', 'no tiene', 'muy fuerte', 'bastante' )
    aracnidos_actualizados = DAO.actualizar(aracnido1)
    log.debug(f'Aracnido actualizado: {aracnidos_actualizados}')




'''

    

#Eliminar  un registro
aracnido = Aracnido(id_aracnido = 5)
aracnido_eliminado = DAO.eliminar(aracnido)
log.debug(f' Aracnido eliminado: {aracnido_eliminado}')
'''     
    
