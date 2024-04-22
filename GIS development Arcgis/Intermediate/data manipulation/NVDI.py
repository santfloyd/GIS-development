'''
CALCULO DE NVDI
'''

import arcpy
import numpy as np

#ruta del raster landasat
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\LANDSAT'

landsatb5=arcpy.Raster('2018-08-25-LC08-200032-20180825-B5.tif')

landsatb4=arcpy.Raster('2018-08-25-LC08-200032-20180825-B4.tif')

arrayb5=arcpy.RasterToNumPyArray(landsatb5).astype("float32")
arrayb4=arcpy.RasterToNumPyArray(landsatb4).astype("float32")

nvdi= (arrayb5-arrayb4)/(arrayb5+arrayb4)

#salvar a NVDI
marco=landsatb5.extent

#lower-left corner
esquina_ii=arcpy.Point(marco.XMin, marco.YMin)

#resolution
res_alto= landsatb5.meanCellHeight
res_ancho=landsatb5.meanCellWidth


raster_nvdi=arcpy.NumPyArrayToRaster(nvdi, esquina_ii, res_alto, res_ancho )

ruta_out=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts'
raster_nvdi.save(ruta_out+'\\'+'nvdi.tif')


print "proceso terminado"
    



