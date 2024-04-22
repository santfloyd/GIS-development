# -*- coding: utf-8 -*-
"""
Created on Mon May 07 19:40:14 2018

@author: ASUS
"""

#importar modulos
import os
import zipfile
#crear el fichero zip en modo w y señalando el modo comprimido ZIP_DEFLATED
zfile=zipfile.ZipFile("shapefiles1.zip", "w",zipfile.ZIP_DEFLATED)
#CREAR LA LISTA de archivos del path indicado
files=os.listdir("C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\data")
#escribe los archivos en el directorio creado con .wirte() el parametro es el nombre del directorio que creará
#dentro del zip más el nombre de cada archivo 
for f in files:
    zfile.write("data/" + f)
#hace otra loop para hacer el print a partir del metodo namelist() con nombres de los archivos anexados y una formatted string en el print
for f in zfile.namelist():
    print "Added %s" %f
    
#cierra
zfile.close()
    

