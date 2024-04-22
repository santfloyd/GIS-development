# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 12:23:36 2018

@author: ASUS
"""

#antes que nada se abre osgeo4w shell y se va hasta el directorio donde esta el raster
#se introduce el siguiente comando gdal_translate nombreinput.extension nombreoutput.extemnsion
#es posible usar -of y el tipo de formato de entrada antes del nombreinput pero no es del todo necesario

#importar modulos para trabajar con raster
import os
import gdal
from gdalconst import *

os.chdir(r'E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#identificar el driver para procesar de raster
driver = gdal.GetDriverByName('PNG')
driver.Register()
#ubicar el raster
filename='AUSTIN_EAST_NW1.png'
datasource=gdal.Open(filename, GA_ReadOnly)
print 'Columnas:', str(datasource.RasterXSize)
print 'Filas:', str(datasource.RasterYSize)
print 'Bands:', str(datasource.RasterCount)


#establcer la informacion georeferenciada del raster
transform=raster.GetGeoTransform()
YOrigin=transform[3]
print "YOrigin:", YOrigin
XOrigin=transform[0]
print "XOrigin:", XOrigin
Pixel_width=transform[1]
print "Pixel_width:", Pixel_width
Pixel_heigth=transform[5]
print "Pixel_heigth:", Pixel_heigth# negative value because it's measured from top