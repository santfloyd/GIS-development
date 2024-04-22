# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 13:56:29 2018

@author: ASUS
"""
#importar modulos para trabajar con raster
import os
import gdal
from gdalconst import *

os.chdir(r'E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#identificar el driver para procesar de raster
driver = gdal.GetDriverByName('Gtiff') # using this driver bc supports driver.CreateCopy() (not all do, weird)
#ubicar el raster
raster='raster.img'
#especificar nombre de raster de salida
copy_raster='raster1.img'
#abrir el raster a copiar
source_datasource=gdal.Open(raster)
#usar createcopy con el primer parametro el nombre del output y como input el raster abierto con el driver en modo lectura
target_raster=driver.CreateCopy(copy_raster,source_datasource, 0)

#para optimizar memoria 
source_datasource=None
target_raster=None

print "copiado"