from clases.Animal_No_Vertebrado import AN
from conex.logger_base import log

class Molusco(AN):
    
    #ENCAPSULAMOS LOS ATRIBUTOS DE LA CLASE    
    _concha =  int
    _habitat = ''
    
    def __init__(self, id_molusco = None, concha = None, habitat = None, columna_vertebral = None , modo_respirar = None) :
        super().__init__(columna_vertebral)
        self._id_molusco = id_molusco
        self._concha = concha
        self._habitat = habitat
        self._modo_respirar = modo_respirar
    
    #USAMOS DECORADOR @PROPERTY PARA SEÑALAR QUE ES UNA ATRIBUTO ENMCAPSULADO DONDE PODEMOS USAR EL METODO GET PARA LLAMAR EL ATRIBUTO         
    @property
    def id_molusco(self):
        return self._id_molusco
    #USAMOS DECORADOR @SETTER PARA SEÑALAR QUE ES UN ATRIBUTO ENCAPSULADO Y PODEMOS USAR EL METODO SET PARA MODIFICAR EL ATRIBUTO
    @id_molusco.setter
    def id_molusco(self, id_molusco):
        self._id_molusco = id_molusco    
        
    @property
    def concha(self):
        return self._concha
        
    @concha.setter
    def concha(self,concha):
        self._concha = concha
    @property
    def habitat(self):
        return self._habitat
    
    @habitat.setter
    def habitat(self,habitat):
        self._habitat = habitat    
    
    @property
    def modo_respirar (self):
        return self._modo_respirar 
    @modo_respirar.setter
    def modo_respirar(self, modo_respirar):
        self._modo_respirar = modo_respirar
    
    
        #USAMOS EL METODO '__STR__' PARA REWTORNAR LOS VALORES DE LOS ATRIBUTOS    
    def __str__(self):
        return f''' Id Molusco: {self._id_molusco} Concha:{self._concha} Habitat: {self._habitat} {super().__str__()} Modo_Respirar {self._modo_respirar}
    '''
'''    
    #METODOS DEL MOLUSCO
    
    def modo_respirar(self):
        r = input("el molusco puede respirar sobre el agua  o  bajo el agua? >>  ")
        if r == "sobre":
            log.debug(" El molusco puede respirar sobre el agua")
        else: 
            r == "bajo"
            log.debug(" El molusco puede respirar bajo  el agua ")

    #AQUI  COMPROBAMOS LOS METODOS

m = Molusco( 2, 'no tiene columna pero' )
m.modo_respirar()
log.debug(m)

        
#ESTAMOS COMPROBANDO QUE LA HERENCIA FUINCIONE BIEN
         
if __name__ == "__main__":
    
    molusco = Molusco(1,1,'en el mar','columna vertebral')    
    log.debug(molusco)
    molusco = Molusco(20,1, 'bajo la arena','no tiene','bajo el agua')
    print(molusco)
    
'''    
    
    

