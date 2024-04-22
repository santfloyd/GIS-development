# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 08:36:33 2018

@author: ASUS
"""

import arcpy
mxd=arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyr in arcpy.mapping.ListLayers(mxd, "",df):
        if lyr.name=="School_Districts":
            arcpy.mapping.RemoveLayer(df,lyr)