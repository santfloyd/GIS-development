# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:19:53 2018

@author: ASUS
"""

import arcpy, os
#output feature class
outputfc=arcpy.GetParameterAsText(0)
#the templete feature class that defines the attributes schema
#los atributos de la plantilla que tendrá la salida
fclasstemplete=arcpy.GetParameterAsText(1)
#open the file to read
fle=open(arcpy.GetParameterAsText(2),"r")
arcpy.CreateFeatureclass_management(os.path.split(outputfc)[0],os.path.split(outputfc)[1],"point",fclasstemplete)
listfires=fle.readlines()
#emplea insertcursor sobre el parametro de entrada que dio el usuario como salida
cursor=arcpy.InsertCursor(outputfc)

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
    