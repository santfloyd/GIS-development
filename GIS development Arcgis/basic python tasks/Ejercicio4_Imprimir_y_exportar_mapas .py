# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:09:50 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
arcpy.mapping.PrintMap(mxd)