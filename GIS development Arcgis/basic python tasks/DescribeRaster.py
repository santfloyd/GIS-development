# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:58:59 2018

@author: ASUS
"""


import arcpy

arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\AUSTIN_EAST_NW"
descRaster=arcpy.Describe("AUSTIN_EAST_NW.sid")
ext=descRaster.Extent
print "XMIN: %F" % (ext.XMin) 
print "YMIN: %F" % (ext.YMin)
print "XMAX: %F" % (ext.XMax)
print "YMAX: %F" % (ext.YMax)
#además del extent de arriba, describir el SRID
sr=descRaster.SpatialReference
print sr.Name
print sr.Type