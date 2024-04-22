# -*- coding: utf-8 -*-
"""
Created on Tue May 01 14:06:08 2018

@author: ASUS
"""

import os
#donde se va a buscar
path="C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\data"
#patron buscado
pattern="*.shp; *.dbf"

#devuelve los directorios que coinciden con el patron con el uso de la función endswith()
#esta funcion es la que hace todo el trabajo y sera llamada por la funcion printdirectory
#el primer argumento beberá de la entrada que le da la funcion printdirectory que es el indice
#en una lista, el segundo argumento es el segundo que le pasa la printdirecory y lo mismo el tercero
def printfiles(dirlist, spacecount, typelist):
    for file in dirlist:
        for ext in typelist:
            if file.endswith(ext):
                #rjust justifica a la derecha el argumento es la cantidad de espacio que justifica
                #en este caso sería la longitud de direntry en la funcion printdirectory
                print "/".rjust(spacecount+1)+file
                break
#devuelve el path de los directorios que coinciden con el patron
#le pasa los argumentos a la funcion printfiles
def printdirectory(dirEntry,typelist):
    print dirEntry[0] + "/"
    printfiles(dirEntry[2],len(dirEntry[0]), typelist)
    
#convierte la cadena de la variable pattern en una lista
extList=[]
for ext in pattern.split(";"):
    #se indica que el * es un comodin 
    extList.append(ext.lstrip("*"))
#se crea una loop con la funcion os.walk para navegar entre directorios llama a la funcion printdirectory
#a su vez esta llama a la funcion printfiles
for directory in os.walk(path):
    printdirectory(directory,extList)
    
    
    