# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:48:48 2018

@author: ASUS
"""

import arcpy

arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
fcList=arcpy.ListFeatureClasses('','Polygon')
for fc in fcList:
    print "Adding field to:"+ fc
    arcpy.AddField_management(fc,"EditedBy","text","25")