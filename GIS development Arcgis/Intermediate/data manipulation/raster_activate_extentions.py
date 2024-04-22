'''
consulta a un raster
'''

import arcpy
import os
from arcpy.sa import ExtractByAttributes 

arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\DEM'
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

dem='mde1.asc'
raster_out= os.path.join(ruta_out,'mde1_filtrado.tif')

#licence cheking spatial analyst
if arcpy.CheckExtension('Spatial') == 'Available':
    #tomar la licencia del servidor
    arcpy.CheckOutExtension('Spatial')
    #herramienta de consulta al raster por extraccion de atributos
    #usa una consulta y salva
    consulta=''' "VALUE" >= 1000 AND "VALUE" <= 1500 '''
    new_dem=ExtractByAttributes(dem, consulta).save(raster_out)
    
    #devolver la licencia al servidor
    arcpy.CheckInExtension('Spatial')
else:
    print 'licencia no disponible'
    
print 'proceso terminado'