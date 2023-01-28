from CRUD.DaoA import DAO
from conex.logger_base import log
from clases.Aracnido import Aracnido


    
opcion = None
while  opcion != 5:
    print('OPCIONES DEL MENU'.center(50,'-'))
    print('1. Listar    Aracnido   >>' )
    print('2. Agregar   Aracnido   >>' )
    print('3. Modificar Aracnido   >>' )
    print('4. Eliminar  Aracnido   >>' )
    print('5. Salir                >>' )
    
    opcion = int(input('Escribe una opcion (1-5): >> '))
    
    if opcion == 1:
        aracnido = DAO.seleccionar()
        for aracnido in aracnido:
            log.debug(aracnido)    
    elif opcion == 2:
        ve = input(' Igrese si tiene o no veneno >> ')
        cv = input(' Ingrese si tiene o no columna vertebral >>')
        mo = input(' Escriba si puede morder o no >> ')
        aracnido = Aracnido (veneno = ve, columna_vertebral = cv, morder= mo )
        aracnido_insertado  = DAO.insertar(aracnido)
        log.debug(f' Aracnido insertado: {aracnido_insertado}')
    elif opcion ==3:
        id_aracnido = int(input(' Escribe el id_aracnido a modificar >> '))
        ven = input(' Escribe el veneno a modificar >> ')
        colu = input(' Escribe la columna a modificar >> ')
        aracnido = Aracnido(id_aracnido,ven,colu)
        aracnido_actualizado = DAO.actualizar(aracnido)
        log.debug(f' Actualizado: {aracnido_actualizado}')
    elif opcion ==4:
        id_aracnidoE = int(input(' Escribe el id_aracnido a eliminar'))
        aracnido = Aracnido(id_aracnido =id_aracnidoE)
        aracnido_eliminado = DAO.eliminar(aracnido)
        log.debug(f' Aracnido Eliminado {aracnido_eliminado}')                                  
else:
    log.debug('Salimos de la aplicacion')
    

