# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:35:32 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mxd):
    if df.name=="Crime_Inset":
        arcpy.mapping.PrintMap(mxd,"",df)