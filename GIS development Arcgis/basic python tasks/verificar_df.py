# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:02:31 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mxd):
    df=arcpy.mapping.ListDataFrames(mxd, "Test_Performance")[0]
for lyr in arcpy.mapping.ListLayers(df):
    print lyr.name