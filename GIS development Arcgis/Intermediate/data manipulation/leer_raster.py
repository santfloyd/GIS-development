'''
leer raster
'''

import arcpy

#ruta del shape de provincias
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\sentinel2'

sentinel2=arcpy.Raster('30-S-YJ-2018-1-16-B11.tif')

#crear archivos xml de estadisticas
if sentinel2.minimum ==None:
    arcpy.CalculateStatistics_management(sentinel2)
    
print sentinel2.catalogPath, sentinel2.format, sentinel2.extent, sentinel2.width, sentinel2.height, \
sentinel2.meanCellHeight, sentinel2.minimum, sentinel2.maximum, sentinel2.mean


