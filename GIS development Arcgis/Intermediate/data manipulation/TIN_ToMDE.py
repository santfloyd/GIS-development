'''
CONVERSION DE TIN A RASTER
'''
import arcpy
import os
from arcpy import TinRaster_3d


tin_in=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\TIN_pntlin.tif'

ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"
raster_out= os.path.join(ruta_out,'TIN_ToMDE.tif')

#licence cheking 3D ANALYST
if arcpy.CheckExtension('3D') == 'Available':
    #tomar la licencia del servidor
    arcpy.CheckOutExtension('3D')
    
    #herramienta para convertir a raster
    TinRaster_3d(tin_in,raster_out,'FLOAT','LINEAR','CELLSIZE 10')
    
    #devolver la licencia al servidor
    arcpy.CheckInExtension('Spatial')
else:
    print 'licencia no disponible'
    
print 'proceso terminado'