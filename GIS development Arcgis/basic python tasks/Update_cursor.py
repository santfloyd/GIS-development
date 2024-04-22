# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:26:53 2018

@author: ASUS
"""

#modulo
import arcpy
#workspace
arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
#añade campo, nombre de campo, tipo y caracteres
arcpy.AddField_management("Hospitals.shp", "FullAddr", "TEXT", "50")
#crea cursor
updcursor=arcpy.UpdateCursor("Hospitals.shp")
#bucle para obtener valores de varios campos, variable que concatena las otras primeras
for row in updcursor:
    strAdress=row.ADDRESS
    strCity=row.CITY
    strstate=row.STATE
    strzip=row.ZIPCODE
    strFullAddress= strAdress + "," + strCity + "," +  strstate + "," + strzip
    #seValue método para acualizar las filas, admite nombre campo, el que se creó, y el valor o en este caso la variable con valores
    row.setValue("FullAddr", strFullAddress)
    #ejecita el cursor para que se inserte en cada fila
    updcursor.updateRow(row)
print "Update Complete"
#desbloquea los datos despues de la insercion
del updcursor
    