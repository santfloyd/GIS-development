# -*- coding: utf-8 -*-
"""
Created on Tue May 01 15:01:08 2018

@author: ASUS
"""

import os

oldfilename="C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\N_America.A2007275_min.txt"
newfilename="C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\N_America.A2007275_nuevonombre.txt"
#funcion que devuelve que ayuda a indicar el carvhico que cambio de nombre (experimento)
def printfilename(file):
    if file.endswith("nuevonombre.txt"):
        print "nuevo nombre:" + file
    elif file.endswith("min.txt"):
        print "viejo nombre" + file
    else:
        print "otros nombres:" + file
#imprimir la lista de ficheros que comiencen por la cadena buscada
print "viejo nombre de fichero"
#uso de metodo de os listdir para iterar en el directorio pasado como argumento
for file in os.listdir("C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises"):
    #usa el metodo startswith
    if file.startswith("N_America"):
        printfilename(file)
  #renombra, funciona igual que replace, el segundo argumento por el primero
os.rename(oldfilename, newfilename)
#vuelve a hacer el listado de ficheros para comprobar el cambio
for file in os.listdir("C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises"):
    #usa el metodo startswith
    if file.startswith("N_America"):
       printfilename(file)