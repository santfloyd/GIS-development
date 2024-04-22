# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:02:33 2018

@author: ASUS
"""

import arcpy
arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
# ‘with’para crear el cursor. La sentencia ‘with’abre y cierra el cursor sin necesidad de preocuparte por los bloqueos
#El primer argumento a pasar al método SearchCursor es el nombre de la feature class que utilizaremos. El segundo parámetro es una tupla que contiene los campos a devolver por la query, y el tercero es la cláusula where. La cláusula where queda “Facility = ‘High School’. 
with arcpy.da.SearchCursor("Schools.shp", ("FACILITY","NAME") "\"FACILITY\"=\'HIGH SCHOOL\'") as cursor:
#Itera a través de cada registro del SearchCursor e imprime el nombre de cada colegio. Utilizamos el bucle ‘for’. También empleamos la función ‘sorted()’ para ordenar los contenidos del cursor. 
    for row in sorted(cursor):
#Para acceder a los vaores de un campo/columna es suficiente con usar el número de índice del campo en la tupla
        print "High school name:" + row[1]
        