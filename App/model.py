"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo
def cargarDatosCatalogo(tipoMapa, factorCarga):
    catalog={
                'generos':None
    }

    catalog['generos'] = mp.newMap(34500, 
                        maptype = tipoMapa,
                        loadfactor = factorCarga)
    return catalog


# Funciones para creacion de datos
def addArtistGenero(catalogo, artista):

    generosArtista=artista['genres']

    if generosArtista != '[]':
        listaGenerosArtista=eval(artista['genres'])
        for genero in listaGenerosArtista:
            if mp.contains(catalogo['generos'], genero) == False:
                listaArtistas=lt.newList()
                lt.addLast(listaArtistas, artista)
                mp.put(catalogo['generos'],genero,listaArtistas)
            else:
                llaveValorGenero=mp.get(catalogo['generos'],genero)
                listaArtistas=me.getValue(llaveValorGenero)
                lt.addLast(listaArtistas, artista)
    else:
        llaveVacio='No tiene'
        if mp.contains(catalogo['generos'],llaveVacio)==False:
            listaArtistas=lt.newList()
            lt.addLast(listaArtistas, artista)
            mp.put(catalogo['generos'],llaveVacio,listaArtistas)
        else:
            llaveValorGenero=mp.get(catalogo['generos'],llaveVacio)
            listaArtistas=me.getValue(llaveValorGenero)
            lt.addLast(listaArtistas, artista)
        

# Funciones de consulta
def artistSize(catalogo):
    return mp.size(catalogo['generos'])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
