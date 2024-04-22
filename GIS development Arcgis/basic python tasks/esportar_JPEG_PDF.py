# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:47:01 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mxd):
    if df.name=="Crime_Inset":
        arcpy.mapping.ExportToJPEG(mxd, "C:\GeoSpatialTraining\ArcGIS10\ejercicios\crime_inset.jpg")
        arcpy.mapping.ExportToPDF(mxd, "C:\GeoSpatialTraining\ArcGIS10\ejercicios\crime_inset.pdf")