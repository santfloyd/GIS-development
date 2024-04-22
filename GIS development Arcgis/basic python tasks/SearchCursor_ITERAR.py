# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:50:56 2018

@author: ASUS
"""


import arcpy

arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
searchcursor=arcpy.SearchCursor("Schools.shp", "\"FACILITY\" = \'HIGH SCHOOL\'")
#EL METODO NEST VA EN MINUSCULA
for row in searchcursor:
#obtener el valor del campo name, TODOS LOS NOMBRES DE LOS COLEGIOS 
    print row.NAME