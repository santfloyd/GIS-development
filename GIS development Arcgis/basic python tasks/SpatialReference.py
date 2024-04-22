# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:16:03 2018

@author: ASUS
"""

import arcpy
arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
#método listfeatureclasses
fcs=arcpy.ListFeatureClasses()
#iterador, aplicación método Describe() y del método SpatialReference
for fc in fcs:
    sr=arcpy.Describe(fc).SpatialReference
    #utiliza la propiedad Name de la variable sr
    if sr.Name == "Unknown":
        print fc + "has no spatial reference"
    else:
        print fc + ":" + sr.Name + "\n"