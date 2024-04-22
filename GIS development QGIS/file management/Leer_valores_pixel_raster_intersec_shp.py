# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 08:21:54 2018

@author: ASUS
"""
#importar modulos para trabajar con raster
import os, sys
import ogr,gdal
from gdalconst import *

#identiiicar el directorio
os.chdir('E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#identificar el driver 
driver=ogr.GetDriverByName('ESRI Shapefile')
#identificar el shp
shp=driver.Open('sites.shp',0)
#crear la layer OGR desde el shp
layer=shp.GetLayer()
#egistrar los driver internamente para el tratamiento de cualquier formato raster
#con el que se pueda trabajr, se eita tener que buscar el tipo de driver etc
gdal.AllRegister()
#identificacion del raster

raster=gdal.Open('raster.img', GA_ReadOnly)
#establecer el tamaño del raster
rows=raster.RasterYSize
col=raster.RasterXSize
bands=raster.RasterCount
#asegurarse del tamaño y numero de bandas
print "numero de bandas en raster:", bands


#establcer la informacion georeferenciada del raster
transform=raster.GetGeoTransform()
YOrigin=transform[3]
print "YOrigin:", YOrigin
XOrigin=transform[0]
print "XOrigin:", XOrigin
Pixel_width=transform[1]
print "Pixel_width:", Pixel_width
Pixel_heigth=transform[5]
print "Pixel_heigth: (negative value because it's measured from top)", Pixel_heigth # negative value because it's measured from top
print "Valores de cada punto:"
# loop through the features in the shapefile, get the x,y (used later for the offset values)
feature=layer.GetNextFeature()
while feature:
    #contador
    contador=0
    contador=contador+1
    #identificar la geometria de las entidades iteradas del shp
    entidades=feature.GetGeometryRef()
    #identificar las coordenadas x, y
    x=entidades.GetX()
    y=entidades.GetY()
    #calculo del offset del raster con base en las cooredandas x, y obtenidas del shape
    x_offset=int((x-XOrigin)/Pixel_width)
    y_offset=int((y-YOrigin)/Pixel_heigth)
    #obtener el id de cada entidad
    point_id = "Point ID: " + feature.GetFieldAsString('ID') + " valores de pixeles en cada banda (1, 2, 3):"
#otra loop en las bandas del raster identificadas mas arriba junto con las filas y columnas para
    #dar el valor de cada piwel en cada banda
    for b in range(bands):
        #usa getrasterbands para recuperar las bandas y el parametro es para que comiece en un hasta el final
        band=raster.GetRasterBand(b+1)
        #recupera los valores de los pixeles en forma de array de cada banda, los 0 son para no especificar los x, y
        data=band.ReadAsArray(0,0,col,rows)
        #crea una lista con los valores de offset que es el valor de cada pixel en cada banda primero con el y_offset
        valor = data[y_offset,x_offset] 
        #guardar en una variable el valor de cada pixel en cada banda para luego imprimir
        point_id = point_id + str(valor) + ' '
    #impromit los valores de offset
    print point_id
    #imprimir todos los valores conseguidos sus las coordenadas de cada y el offset correspondiente en el raster
    print "coordenada X:", x, "coordenada Y:", y, "X offset:", x_offset, ", Y offset:", y_offset    
    #ir a la siguiente entidad en la iteracion
    feature.Destroy()
    feature=layer.GetNextFeature()
#habilita el contenido
shp.Destroy()
print "terminado"
        