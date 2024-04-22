'''
crear un TIN
y luego editarlo
'''

import arcpy
import os
from arcpy import CreateTin_3d
from arcpy import EditTin_3d

arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\DEM'

ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

tin_out= os.path.join(ruta_out,'TIN_edit_pnt.tif')
#shape para editar el TIN
shp_in=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\64032\64032puntos_cota.shp'

#licence cheking 3D ANALYST
if arcpy.CheckExtension('3D') == 'Available':
    #tomar la licencia del servidor
    arcpy.CheckOutExtension('3D')
    
    #herramienta para crear el TIN vacio
    CreateTin_3d(tin_out)
    
    #editar el TIN con base en puntos de cota
    #params es una string, <none> para campo de etiquetas si no se usan etiquetas
    #masspoints como se va a poblar el tin
    params=shp_in+' Cota <none> masspoints false'
    EditTin_3d(tin_out,params,False)
    
    #devolver la licencia al servidor
    arcpy.CheckInExtension('Spatial')
else:
    print 'licencia no disponible'
    
print 'proceso terminado'