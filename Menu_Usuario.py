from Login.Login import inicioSesion
from Login.Login import buscarUsuariopassword
from Login.Login import validarLogin
from Login.Login import Encriptar
from CRUD.DaoU import DAOU
from conex.logger_base import log
from clases.Usuario import Usuario
import pwinput

opcion = 0
while opcion != 5:
    print('OPCIONES DEL MENU'.center(50, '-'))
    print('1. Listar    Usuario   >>' )
    print('1. Agregar   Usuario   >>' )
    print('3. Modificar Usuario   >>' )
    print('4. Eliminar  Usuario   >>' )
    print('5. Salir               >>' )

    opcion = int(input('Escribe una opcion (1-3): >> '))

    if opcion == 1:
        usuario = DAOU.seleccionar()
        for usuario in usuario:
            log.debug(usuario)
                
    elif opcion == 2:
        nombre = input('Ingrese el nombre del usuario >> ')
        password = pwinput.pwinput(' Ingrese el pasword >> ')
        password = Encriptar().encode(password)
        usuario = Usuario(nombre = nombre , password = password)
        usuario_insertado = DAOU.insertar(usuario)
        log.debug(f' usuario insertado')
        buscarUsuariopassword(nombre, password)
        validarLogin()
        inicioSesion()
        
    elif  opcion == 3:
        id_usuario = int(input( ' Escribe el ID  a modificar >> '))
        no = input(' Escribe el nombre a modificar >> ')
        pas = input(' Escribe el password a modificar >> ')
        pas = Encriptar().encode(pas)
        usuario = Usuario(id_usuario,no,pas)
        usuario_actualizado = DAOU.actualizar(usuario)
        log.debug(f' Usuario Actualizado {usuario_actualizado}')
        
    elif opcion == 4:
        id_usuarioU = int(input(' Escribe el ID a eliminar >> '))
        usuario = Usuario(id_usuario=id_usuarioU)
        usuario_eliminado = DAOU.eliminar(usuario)
        log.debug(f' Usuario eliminado {usuario_eliminado}')
else:
    log.debug(' Salimos de la aplicacuion')
        
        
    
        
         

        
        
        
        
        