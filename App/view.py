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
default_limit = 100000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Examinar los álbumes en un año de interés")
    print('2- Encontrar los artistas por popularidad')
    print('3- Encontrar las canciones por popularidad')
    print('4- Encontrar la canción más popular de un artista en un pais')
    
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        tamanioarchivo=input('\nSeleccione el Tamanio de archivo: \n1-small\n2-large\n')
        if int(tamanioarchivo)==1:
            tamanioarchivo='small'
        elif int(tamanioarchivo)==2:
            tamanioarchivo='large'
        factorCarga=input('Factor de Carga: \n')
        catalogo=controller.inicializarCatalogo(float(factorCarga))
        delta_time, deltamemory=controller.loadData(catalogo, str(tamanioarchivo))
        print('Numero Generos: '+str(controller.generosSize(catalogo)))
        print('Numero Artistas: '+str(controller.artistasSize(catalogo)))
        print('Numero canciones: '+str(controller.cancionesSize(catalogo)))
        print('Numero Albumes: '+str(controller.albumesSize(catalogo)))
        print("Tiempo carga datos[ms]: ", f"{delta_time:.3f}", "||",
              "Memoria carga datos[kB]: ", f"{deltamemory:.3f}")

    elif int(inputs[0]) == 1:
        anio=input('Anio de interes: ')
        controller.loadAlbumesAnio(catalogo,str(tamanioarchivo))
        listaAlbumesAnio=controller.listaOrdenadaAlbumesAnio(catalogo, anio)
        print(listaAlbumesAnio)

    elif int(inputs[0]) == 2:
        popularidad=int(input('Ingrese la Popularidad (sin decimal): '))
        controller.loadArtistasPopularidad(catalogo,tamanioarchivo)
        listaArtistasPopularidad=controller.listaOrdenadaArtistasPopularidad(catalogo,popularidad)
        print(listaArtistasPopularidad)
        
    elif int(inputs[0])==3:
        popularidadCanciones = int(input("Ingrese la popularidad de la canción (sin decimal): "))
        controller.loadCancionesPopularidad(catalogo, tamanioarchivo)
        listaCancionesPopularidad=controller.listaOrdenadaCancionesPopularidad(catalogo, popularidadCanciones)
        print(listaCancionesPopularidad)

    elif int(inputs[0])==4:
        codigoPais=input('Ingrese el codigo del pais: ')
        nombreArtista=input('Ingrese nombre Artistas: ')
        controller.loadCancionesPaises(catalogo,tamanioarchivo)
        listaPaisCanciones=controller.listaOrdenadaPaisCanciones(catalogo, codigoPais)
        print(controller.cancionPopularArtistaPais(catalogo, listaPaisCanciones, nombreArtista))

    else:
        sys.exit(0)