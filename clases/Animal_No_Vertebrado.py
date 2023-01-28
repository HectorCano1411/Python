from conex.logger_base import log

class  AN:
     #ENCAPSULAMOS LOS ATRIBUTOS DE LA CLASE
    _columna_vertebral = False
    
    def __init__(self, columna_vertebral = None ):
        self._columna_vertebral = columna_vertebral
        
    
    def __str__(self):
        return  f'y no tiene {self._columna_vertebral}'
    
    #USAMOS DECORADOR @PROPERTY PARA SEÑALAR QUE ES UNA ATRIBUTO ENMCAPSULADO DONDE PODEMOS USAR EL METODO GET PARA LLAMAR EL ATRIBUTO         
    @property
    def columna_vertebral(self):
        return self._columna_vertebral
    
    #USAMOS DECORADOR @SETTER PARA SEÑALAR QUE ES UN ATRIBUTO ENCAPSULADO Y PODEMOS USAR EL METODO SET PARA MODIFICAR EL ATRIBUTO
    @columna_vertebral.setter
    def columna_vertebral(self, columna_vertebral):
        self._columna_vertebral = columna_vertebral
    
a = AN(' columna vertebral')
log.debug(a)
