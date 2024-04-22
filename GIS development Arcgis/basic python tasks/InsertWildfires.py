# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:55:02 2018

@author: ASUS
"""

#importar modulos
import arcpy, os
#workspace
arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\WildfireData\WildlandFires.mdb"
#abrir fichero de texto con la info a importar, solo lectura
fle=open("C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\WildfireData\NorthAmericaWildfires_2007275.txt", "r")
#crear lista para almacenar las lineas en ese fichero .txt
listfires=fle.readlines()
#crear cursor
cursor=arcpy.InsertCursor("FireIncidents")
#crear contador para evaluar el progreso de la importación
counter=1
#loop para leer en la primera lista de lineas del fichero .txt
for fire in listfires:
    #if statement para saltar al primer registro que es la cabecera con el texto "Latitude"
    if 'Latitud' in fire:
        continue
    #crea sub lista con los valores separados por coma en el .txt
    valores=fire.split(",")
    #variables contenidos en la sublista, individualizados gracias al separador
    latitude=float(valores[0])
    longitude=float(valores[1])
    confide=int(valores[2])
    #crear objeto tipo punto que alamacenará las coordenadas x y de cada registro
    pnt=arcpy.Point(longitude,latitude)
    #crear un nuevo registro (feature) en el insert cursor con el método newRow()
    feature=cursor.newRow()
    #asignar la geometrá del objeto point al shapefile en el campo shape, así como del otro campo confide
    feature.shape=pnt
    feature.setValue("CONFIDENCEVALUE", confide)
    #inserta nuevo registro
    cursor.insertRow(feature)
    #muestra el progreso y actualiza el contador
    arcpy.AddMessage("Record number"+str(counter)+"written to feature class")
    counter=counter+1
del cursor
fle.close()
    