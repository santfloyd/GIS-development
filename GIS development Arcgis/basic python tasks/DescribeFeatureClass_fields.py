# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:46:37 2018

@author: ASUS
"""

import arcpy

arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
descFc=arcpy.Describe("Streets.shp")
print "the sahpetype is:" + descFc.ShapeType
flds=descFc.Fields
for fld in flds:
    print "field: " + fld.Name
    print "Type: " + fld.Type
    print "Length: " + str(fld.Length)