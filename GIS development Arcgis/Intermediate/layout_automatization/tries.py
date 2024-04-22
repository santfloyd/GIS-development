# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:54:27 2021

@author: Usuario
"""

import os
import arcpy
import arcpy.mapping as mapp

ruta=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\proyecto_automated_layout_MP5_1.mxd"

dir_=os.path.dirname(ruta)

#print(os.path.split(ruta)[1])
#print(dir_)

#ruta de salida del pdf
#ruta_pdf= os.path.join(os.path.dirname(ruta), str(os.path.split(self.salida_casilla.text())[1]))

mxd = mapp.MapDocument(ruta) #"CURRENT SOLO SIRVE EN LA VENTANA DE ARCMAP NO EN CODIGO QUE SE EJECUTA TRAS BAMBALINAS"
df=mapp.ListDataFrames(mxd,"Layers")[0]

#lista_graficos = mapp.ListLayoutElements(mxd, "GRAPHIC_ELEMENT")

#print(lista_graficos)


lyr = arcpy.mapping.ListLayers(mxd, "paro_ccaa_1976_2013", df)[0] 
print(lyr.name)
print(lyr.symbologyType)
print(lyr.symbology.numClasses)
print(lyr.symbology.valueField)
lyr.symbology.reclassify()
lyr.symbology.valueField = "2013"
lyr.symbology.numClasses = 5
print(lyr.symbologyType) 
print(lyr.symbology.numClasses)
print(lyr.symbology.valueField)

Extent = lyr.getExtent(True)
df.extent = Extent 

arcpy.RefreshActiveView()
arcpy.RefreshTOC()
mxd.save()

# arcpy.MakeFeatureLayer_management(lyr,"paro_lyr")
# lyrFile = arcpy.mapping.Layer("paro_lyr")
# lyrSymbolClass = lyrFile.symbology
# print(lyrSymbolClass)

# arcpy.MakeFeatureLayer_management("parcels.shp", "parcels_lyr")
# 

# if lyr.symbologyType == "GRADUATED_COLORS":
#     lyr.symbology.reclassify()
#     lyr.symbology.valueField = "2013"
#     lyr.symbology.numClasses = 3 
# 
# 
# arcpy.RefreshActiveView()
# arcpy.RefreshTOC()


# arcpy.management.MakeFeatureLayer(lyr, "paro")
# lyrFile = arcpy.mapping.Layer("paro")
# arcpy.mapping.UpdateLayer(df, lyr, lyrFile, True)
# lyrSymbolClass = lyrFile.symbology
# print(lyrSymbolClass)
                                         

