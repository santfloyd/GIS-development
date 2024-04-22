# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:51:10 2018

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
ext=descFc.Extent
print "XMIN: %F" % (ext.XMin) 
print "YMIN: %F" % (ext.YMin)
print "XMAX: %F" % (ext.XMax)
print "YMAX: %F" % (ext.YMax)
