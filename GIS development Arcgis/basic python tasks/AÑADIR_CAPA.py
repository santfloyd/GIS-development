# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:41:11 2018

@author: ASUS
"""

import arcpy
mxd=arcpy.mapping.MapDocument("CURRENT")
#define el df
df=arcpy.mapping.ListDataFrames(mxd,"Crime")[0]
#define la variable para luego ser usada el addlayer
addLayer=arcpy.mapping.Layer(r"C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\School_Districts.lyr")
#añade la layer y señala el autoarreglo
arcpy.mapping.AddLayer(df,addLayer,"AUTO_ARRANGE")
#Añadir capa a un grupo determinado

