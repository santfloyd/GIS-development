# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 20:31:20 2018

@author: ASUS
"""
#improtar modulos necesarios
import os, ogr
#establecer el workspace
os.chdir('E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#establecer el driver
driver=ogr.GetDriverByName('ESRI Shapefile')
#establecer el datasource
DataSource=driver.Open('fires.shp', 0)
#establecer la layer OGR
layer=DataSource.GetLayer()
#guardar en una variable la layer a la que se le palica el metodo para recuperar su referencia espacial
target_layer=layer.GetSpatialRef()


print "La referencia espacial es:", target_layer
#aplicar el metodo para trnasformar a formato de esri
target_layer.MorphToESRI()
#sacar por pantalla la referencia espacial en texto con el metodo .ExportToWkt()
print "referencia espacial WKT:", target_layer.ExportToWkt()







