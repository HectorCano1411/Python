from clases.Animal_No_Vertebrado import AN
from conex.logger_base import log


class Aracnido(AN):     
    _veneno = ' '
    #ENCAPSULAMOS LOS ATRIBUTOS DE LA CLASE   
    def __init__(self, id_aracnido = None, veneno = None ,columna_vertebral = None, morder = None, telaraña = None ):
        super().__init__(columna_vertebral)
        self._id_aracnido = id_aracnido
        self._veneno = veneno
        self._morder = morder
        self._telaraña = telaraña
        
    #USAMOS DECORADOR @PROPERTY PARA SEÑALAR QUE ES UNA ATRIBUTO ENMCAPSULADO DONDE PODEMOS USAR EL METODO GET PARA LLAMAR EL ATRIBUTO     
    @property
    def id_aracnido(self):
        return self._id_aracnido
    #USAMOS DECORADOR @SETTER PARA SEÑALAR QUE ES UN ATRIBUTO ENCAPSULADO Y PODEMOS USAR EL METODO SET PARA MODIFICAR EL ATRIBUTO
    
    @id_aracnido.setter
    def id_aracnido(self, id_aracnido):
        self._id_aracnido = id_aracnido

    @property
    def veneno(self):
        return self._veneno
    @veneno.setter
    def veneno(self, veneno):
        self._veneno = veneno
        
    @property
    def morder(self):
        return self._morder
    
    @morder.setter
    def morder(self, morder):
        self._morder = morder
        
    @property
    def telaraña (self):
        return self._telaraña
    
    @telaraña.setter
    def telaraña (self, telaraña):
        self._telaraña = telaraña

        
    def __str__(self):
        return f'''Id aracnido {self._id_aracnido} ,El aracnido tiene : {self._veneno } {super().__str__() } puede morder : {self._morder} telaraña: {self._telaraña}'''  
        
    #METODOS DEL ARACNIDO
'''             
    def morder(self):
        m = input(" ¿'El aracnido puede morder? Ingrese (si / no) avise por favaor>>  ")
        if m == 'si':
            log.debug("El  aracnido puede morder!!!!!")
        else:
            m == 'no'
            log.debug("El  aracnido no puede morder!!!!!")
            
            
    def tejer_telaraña (self):
        t = input("ingresed cuanta telaraña puede tejer el aracnido >>")
        log.debug(f'el aracnido puede tejer {t} telaraña')

#AQUI  COMPROBAMOS LOS METODOS         
        
Aracnido('', '' , '')
a = Aracnido( 1, "veneno" ," columna vertebral  ", 'muy fuerte', 'muy sedosa'  )
a.morder()
a.tejer_telaraña()
log.debug(a)

    

#ESTAMOS COMPROBANDO QUE LA HERENCIA FUINCIONE BIEN
         
if __name__ == "__main__":
    
    aracnido1 = Aracnido(1, 'columna', ' veneno de tarantula')
    log.debug(aracnido1)
'''   
     
















