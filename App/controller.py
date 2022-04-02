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
 """

import config as cf
import model
import csv
import tracemalloc
import time
import csv
csv.field_size_limit(2147483647)



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def inicializarCatalogo( factorCarga):
    return model.inicializarCatalogo(factorCarga)

# Funciones para la carga de datos
def loadGeneros(catalogo, tamanioArchivo):
    tagsfile = cf.data_dir + 'Spotify/spotify-artists-utf8-'+tamanioArchivo+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtistGenero(catalogo, artist)

def loadArtists(catalogo, tamanioArchivo):
    tagsfile = cf.data_dir + 'Spotify/spotify-artists-utf8-'+tamanioArchivo+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtistsId(catalogo, artist)

def loadCanciones(catalogo, tamanioArchivo):
    tagsfile = cf.data_dir + 'Spotify/spotify-tracks-utf8-'+tamanioArchivo+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for cancion in input_file:
        model.addCancionId(catalogo, cancion)

def loadAlbumes(catalogo, tamanioArchivo):
    tagsfile = cf.data_dir + 'Spotify/spotify-albums-utf8-'+tamanioArchivo+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for album in input_file:
        model.addAlbumId(catalogo, album)

def loadAlbumesAnio(catalogo, tamanioArchivo):
    tagsfile = cf.data_dir + 'Spotify/spotify-albums-utf8-'+tamanioArchivo+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for album in input_file:
        model.addAlbumAnio(catalogo, album)

def loadArtistasPopularidad(catalogo, tamanioArchivo):
    tagsfile = cf.data_dir + 'Spotify/spotify-artists-utf8-'+tamanioArchivo+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtistaPopularidad(catalogo, artist)

def loadCancionesPaises(catalogo, tamanioArchivo):
    tagsfile = cf.data_dir + 'Spotify/spotify-tracks-utf8-'+tamanioArchivo+'.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for cancion in input_file:
        model.addCancionesPaises(catalogo, cancion)


def loadData(catalogo, tamanioArchivos):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadGeneros(catalogo, tamanioArchivos)
    loadArtists(catalogo, tamanioArchivos)
    loadCanciones(catalogo, tamanioArchivos)
    loadAlbumes(catalogo, tamanioArchivos)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)
    return (delta_time,delta_memory)

# Funciones de ordenamiento
def listaOrdenadaAlbumesAnio(catalogo,anio):
    return model.listaOrdenadalbumesAnio(catalogo,anio)
def listaOrdenadaArtistasPopularidad(catalogo, popularidad):
    return model.listaOrdenadaArtistasPopularidad(catalogo,popularidad)
def listaOrdenadaPaisCanciones(catalogo, codigoPais):
    return model.listaOrdenadaPaisCanciones(catalogo, codigoPais)

# Funciones de consulta sobre el catálogo

def generosSize(catalogo):
    return model.generosSize(catalogo)
def artistasSize(catalogo):
    return model.artistsSize(catalogo)
def cancionesSize(catalogo):
    return model.cancionesSize(catalogo)
def albumesSize(catalogo):
    return model.albumesSize(catalogo)

# Funciones para medir tiempos de ejecucion


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
