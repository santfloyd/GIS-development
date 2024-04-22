# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:38:47 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
analysis=arcpy.mapping.AnalyzeForMSD(mxd)
for key in ('messages','warnings','errors'):
    print "----" + key.upper()+"----"
    vars=analysis[key]
    for ((message, code),layerlist) in vars.iteritems():
        print "  ", message, "(CODE %i)" % code
        print " applies to:",
        for layer in layerlist:
            print layer.name,
            print
