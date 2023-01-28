from clases.Molusco import Molusco
from conex.logger_base import log
from conex.conexion import   Conexion



class DAOM:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR    = 'SELECT * FROM molusco ORDER BY id_molusco'
    _INSERTAR       = 'INSERT INTO molusco ( concha,habitat, columna_vertebral, modo_respirar ) VALUES(%s, %s, %s,%s)'
    _ACTUALIZAR     = 'UPDATE molusco SET  concha=%s , habitat=%s, columna_vertebral=%s, modo_respirar=%s WHERE id_molusco=%s'
    _ELIMINAR       = 'DELETE FROM molusco WHERE id_molusco=%s'
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                moluscos = []
                for registro in registros:
                    molusco = Molusco(registro[0], registro[1], registro[2], registro[3] ,registro[4])
                    moluscos.append(molusco)
                return moluscos
            


    @classmethod
    def insertar(cls, molusco):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = ( molusco.concha, molusco.habitat, molusco.columna_vertebral, molusco.modo_respirar)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                log.debug(f'Molusco insertado: {molusco}')
                return cursor.rowcount
            
            
    @classmethod
    def actualizar(cls, molusco):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (molusco.concha, molusco.habitat, molusco.columna_vertebral,molusco.modo_respirar, molusco.id_molusco)
                cursor.execute(cls._ACTUALIZAR, valores,multi=True)
                conexion.commit()
                log.debug(f'Molusco actualizado : {molusco}')
                return cursor.rowcount
                
                
    @classmethod
    def eliminar(cls, molusco):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (molusco.id_molusco,)
                cursor.execute(cls._ELIMINAR, valores,multi=True)
                conexion.commit()
                log.debug(f' Molusco Eliminado: {molusco}')
                return cursor.rowcount
            
            
if __name__ == "__main__":      
    molusco = Molusco(concha = 2, habitat = 'rio', columna_vertebral = 'no tiene', modo_respirar=' bajo el agua')
    molusco_insertado = DAOM.insertar(molusco)
    log.debug(f'Molusco insertado: {molusco_insertado}')
   

    
    
    
    