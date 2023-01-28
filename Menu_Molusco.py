from CRUD.DaoM import DAOM
from conex.logger_base import log
from clases.Molusco import Molusco


opcion = None
while  opcion != 5:
    print('OPCIONES DEL MENU'.center(50,'-'))
    print('1. Listar     Moluscos  >>' )
    print('2. Agregar    Moluscos  >>' )
    print('3. Modificar  Moluscos  >>' )
    print('4. Eliminar   Moluscos  >>' )
    print('5. Salir                >>' )
    
    opcion = int(input('Escribe una opcion (1-5): >> '))
    
    if opcion == 1:
        molusco = DAOM.seleccionar()
        for molusco in molusco:
            log.debug(molusco)  
    elif opcion == 2:
        c = int(input(' Escribe la cantidad de conchas a ingresar >> '))
        h = input ( ' Escribe el habitat del molusco a ingresar >> ')
        cv = input (' Escribe si tiene o no columna vertebral >> ')
        mr =input (' Esdcriba el modo de respirar del molusco >> ')
        molusco = Molusco(concha=c, habitat= h, columna_vertebral= cv, modo_respirar= mr)
        molusco_insertado = DAOM.insertar(molusco)
        log.debug(f' Molusco insertado : {molusco_insertado}')
    elif opcion ==3:
        id_m = int(input(' Escribe el id_molusco a modificar >> '))
        co = int(input(' Escribe el numero de conchas a modificar >> '))
        ha = input(' Escribe el habitat del molusco a modificar >> ')
        cv = input (' Escribe la columna vertebral a modificar >> ')
        molusco =  Molusco(id_m,co,ha,cv)
        molusco_actualizado = DAOM.actualizar(molusco)
        log.debug(f' El Molusco fue actualizado {molusco_actualizado}')
    elif opcion ==4:
        id_m = int(input(' Escribe el id del molusco a eliminar >> '))
        molusco = Molusco(id_molusco = id_m)
        molusco_eliminado = DAOM.eliminar(molusco)
        log.debug(f' el molusco fue eliminado: {molusco_eliminado}')
else:
    log.debug('Salimos de la aplicacion')       