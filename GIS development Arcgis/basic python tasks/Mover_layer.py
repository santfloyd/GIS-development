# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:38:38 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
df=arcpy.mapping.ListDataFrames(mxd, "Crime")[0]
#itera entre las capas del dataframe
for lyr in arcpy.mapping.ListLayers(mxd, "", df):
    if lyr.name== "School_Districts":
        moveLayer= lyr
        #los nombres deben coincidir
    if lyr.name== "District_Crime_Join":
        refLayer= lyr
arcpy.mapping.MoveLayer(df, refLayer, moveLayer, "BEFORE")
