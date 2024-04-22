# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:42:27 2018

@author: ASUS
"""


import arcpy
arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
arcpy.AddField_management('Hospitals.shp', 'FullAddr', "TEXT", "50")
with arcpy.da.UpdateCursor('Hospitals.shp', "ADDRESS","CITY", "STATE", "ZIPCODE", "FullAddr") as cursor:
    for row in cursor:
        strAddress=row[0]
        strcity=row[1]
        strstate=row[2]
        strzip=row[3]
        strfulladd= strAddress + strcity + strstate + strzip
        print strfulladd
        row[4]=strfulladd
        cursor.updateRow(row)
    print "update complete"

            