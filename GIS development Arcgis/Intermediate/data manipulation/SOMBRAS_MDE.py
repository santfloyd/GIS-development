'''
MAPA SE SOMBRAS
'''
import arcpy
import os
from arcpy import HillShade_3d
from arcpy.sa import Slope

raster_in=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\TIN_ToMDE.tif'

ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"
raster_sombras_out= os.path.join(ruta_out,'sombras.tif')
raster_pendientes_out= os.path.join(ruta_out,'pendientes.tif')

#licence cheking 3D ANALYST
if arcpy.CheckExtension('3D') == 'Available':
    #tomar la licencia del servidor
    arcpy.CheckOutExtension('3D')
    
    #herramienta para derivar sombras y pendientes
    HillShade_3d(raster_in,raster_sombras_out,315,45, True)
    Slope(raster_in,"DEGREE").save(raster_pendientes_out)
    
    #devolver la licencia al servidor
    arcpy.CheckInExtension('Spatial')
else:
    print 'licencia no disponible'
    
print 'proceso terminado'