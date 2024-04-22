# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 07:52:43 2018

@author: ASUS
"""
#Añadir capa a un grupo determinado
#import arcpy

       
import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
#define el df
for df in arcpy.mapping.ListDataFrames(mxd):
     df=arcpy.mapping.ListDataFrames(mxd, "Test_Performance")[0]
print df.name
#define la variable con la capa a añadir
addLayer=arcpy.mapping.Layer(r"C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\coa_parcels.shp")
#define el grupo objetivo
target_group_layer=arcpy.mapping.ListLayers(mxd, "nuevo_grupo", df)[0]
#añade la capa al final
arcpy.mapping.AddLayerToGroup(df,target_group_layer,addLayer,"BOTTOM")


