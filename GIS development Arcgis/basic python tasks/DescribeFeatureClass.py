# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:40:28 2018

@author: ASUS
"""

import arcpy

arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
descFc=arcpy.Describe("Streets.shp")
print "the sahpetype is:" + descFc.ShapeType
