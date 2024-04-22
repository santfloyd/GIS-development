# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 08:41:03 2018

@author: ASUS
"""

#requiere un layer de referencia por eso no puede usarse en un dataframe vacio
#PARA INSERTAR CAPA EN OTRO DATAFRAME HACE FALTA ACTIVARLO SI EN MXD ES CURRENT O INDICAR LA RUTA
import arcpy
mxd=arcpy.mapping.MapDocument("CURRENT")
#define el df
df=arcpy.mapping.ListDataFrames(mxd,"Test_Performance")[0]
#layer de referencia
reflayer=arcpy.mapping.ListLayers(mxd, "District_Crime_Join",df)[0]
#define la variable para luego ser usada el addlayer
insertLayer=arcpy.mapping.Layer(r"C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\School_Districts.lyr")
#añade la layer y señala el autoarreglo
arcpy.mapping.InsertLayer(df,reflayer,insertLayer,"AFTER")