'''
lectura de raster
'''

import arcpy
import numpy as np

#ruta del shape de provincias
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\sentinel2'

sentinel2=arcpy.Raster('30-S-YJ-2018-1-16-B11.tif')

array=arcpy.RasterToNumPyArray(sentinel2)

#retorna filas y luego columnas
print array.shape

alto,ancho=array.shape

media= np.mean(array)

media_=np.sum(array)/(ancho*alto)

print media, media_