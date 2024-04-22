# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:34:42 2018

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
#borrar capa
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyr in arcpy.mapping.ListLayers(mxd, "",df):
        if lyr.name=="School_Districts":
            arcpy.mapping.RemoveLayer(df,lyr)
#insertar capa
df=arcpy.mapping.ListDataFrames(mxd,"Crime")[0]
#layer de referencia
reflayer=arcpy.mapping.ListLayers(mxd, "Bexar_County_Boundary",df)[0]
#define la variable para luego ser usada el addlayer
insertLayer=arcpy.mapping.Layer(r"C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\School_Districts.lyr")
#añade la layer y señala el autoarreglo
arcpy.mapping.InsertLayer(df,reflayer,insertLayer,"AFTER")