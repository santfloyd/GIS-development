# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:50:10 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
msd=("C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Crime.msd")
arcpy.mapping.ConvertToMSD(mxd,msd, "","NORMAL","NORMAL")