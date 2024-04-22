# -*- coding: utf-8 -*-
"""
Created on Mon May 07 19:25:51 2018

@author: ASUS
"""

#importar modulos
import os
import zipfile

#crear el archivo zip con la clase ZipFile con el primer parámetro el nombre del archivo
#el segundo es el modo, "w" es capaz de crear documento, el tercero es el tipo de compresion
#ZIP_STORED o ZIP_DEFLATED, EL PRIMERO ES NO comprimido y el segundo comprimido
zfile=zipfile.ZipFile("shapefiles.zip", "w", zipfile.ZIP_STORED)
#CREAR UNA LISTA DE ficheros que hay en el path indicado con os.listdir()
files=os.listdir("C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\data")
#una lopp iterando en la lista para añadirlos al zip dentro de la carpeta que 
#creará con el nombre que se pase como argumento
#slash en esa orientacion el otro no parece apropiado, piensa que es un path
#escribe los archivos en el directorio creado con .wirte() el parametro es el nombre del directorio
#dentro del zip más el nombre de cada archivo
for f in files:
    zfile.write("data/" + f)
#hace otra loop para hacer el print a partir del metodo namelist() con nombres de los archivos anexados y una formatted string en el print
for f in zfile.namelist():
    print "Added %s" %f
    
#cierra
zfile.close()