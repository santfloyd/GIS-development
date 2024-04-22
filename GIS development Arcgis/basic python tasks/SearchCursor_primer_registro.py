# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:58:59 2018

@author: ASUS
"""


import arcpy

arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
searchcursor=arcpy.SearchCursor("Schools.shp", "\"FACILITY\" = \'HIGH SCHOOL\'")
#EL METODO NEST VA EN MINUSCULA
row=searchcursor.next()
#IMPRIMIR EL VALOR DEL CAMPO FACILITY
print row.FACILITY
