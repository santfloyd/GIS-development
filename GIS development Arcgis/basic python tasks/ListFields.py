# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:53:59 2018

@author: ASUS
"""

#Santiago Ortiz
#22/02/2018
import arcpy

arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
fieldlist=arcpy.ListFields("Building_Permits.shp")
for fld in fieldlist:
    print "%s is type of %s a length of %i" % fld.name, fld.type, fld.length
