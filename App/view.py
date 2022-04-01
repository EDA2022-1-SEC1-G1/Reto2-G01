"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
import sys
from DISClib.DataStructures import mapentry as me
default_limit = 1000000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        tipoMapa=input('Tipo de Mapa: \n1-PROBING\n2-CHAINING\n')
        if int(tipoMapa) == 1:
            tipoMapa ='PROBING'
        elif int(tipoMapa) == 2:
            tipoMapa='CHAINING'
        else:
            print('Numero no es una opcion')
        factorCarga=input('Factor de Carga: \n')
        catalogo=controller.cargarDatosCatalogo(str(tipoMapa), float(factorCarga))
        delta_time, deltamemory=controller.loadData(catalogo)
        print(' Numero Generos: '+str(controller.artistSize(catalogo)))
        print("Tiempo [ms]: ", f"{delta_time:.3f}", "||",
              "Memoria [kB]: ", f"{deltamemory:.3f}")
        
        
        


    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)

