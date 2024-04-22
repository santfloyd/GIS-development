# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:31:13 2018

@author: ASUS
"""

import arcpy.mapping
mxd=arcpy.mapping.MapDocument("CURRENT")
#iterar en lista de elementos de layout
for el in arcpy.mapping.ListLayoutElements(mxd):
#usa el metodo name
    print el.name
#iterar en lista de elementos layout pero solo con elementos de leyenda
for el in arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT"):
#usa el metodo name
    print el.name
#cambiar el título del elemento de leyenda àrticular
elLeg=arcpy.mapping.ListLayoutElements(mxd,"LEGEND_ELEMENT", "Crime Legend")[0]
elLeg.title="2018_pytho_GIS"    
