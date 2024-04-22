'''
derivar NVDI de landsat
'''
import arcpy
import os

#usa un archivo de texto para reclasificar el raster por eso el modulo byascciifile
from arcpy.sa import *

arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\sagunto'

file_reclass='reclass_raster.txt'

ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"
raster_out= os.path.join(ruta_out,'nvdi_RECLASS.tif')

#licence cheking 3D ANALYST
if arcpy.CheckExtension('Spatial') == 'Available':
    #tomar la licencia del servidor
    arcpy.CheckOutExtension('Spatial')
    
    #bandas roja e infraroja
    #Float para no perder decimales, esa funcion va en arcpy no es la misma que float
    b_r= Float(Raster('sagtm3.tif'))
    b_ir= Float(Raster('sagtm4.tif'))
    
    nvdi=(b_r-b_ir)/(b_r+b_ir)
    
    #reclasificar raster de entrada y fichero ascii de reclasificacion
    nvdi_reclass=ReclassByASCIIFile(nvdi, file_reclass).save(raster_out)
    
    #devolver la licencia al servidor
    arcpy.CheckInExtension('Spatial')
else:
    print 'licencia no disponible'
    
print 'proceso terminado'
