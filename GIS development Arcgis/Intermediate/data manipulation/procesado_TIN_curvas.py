'''
editar TIN para introducir curvas y puntos de cotas
'''

import arcpy
import os
from arcpy import CreateTin_3d
from arcpy import EditTin_3d


arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\DEM'

ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

tin_out= os.path.join(ruta_out,'TIN_pntlin.tif')
#shape para editar el TIN
shp_in_pnt=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\64032\64032puntos_cota.shp'
shp_in_curvas=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\64032\64032curvas_nivel.shp'
shp_in_linrotura=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\64032\64032hidrog_lin.shp'

#licence cheking 3D ANALYST
if arcpy.CheckExtension('3D') == 'Available':
    #tomar la licencia del servidor
    arcpy.CheckOutExtension('3D')
    
    #herramienta para crear el TIN vacio
    CreateTin_3d(tin_out)
    
    #editar el TIN con base en puntos de cota
    #params es una string, <none> para campo de etiquetas si no se usan etiquetas
    #masspoints como se va a poblar el tin
    #la string consiste en ruta del shpe, campo de elevancion, campo de etiquetas, tipo de algoritmo (para puntos se usa masspoints), utilizar la z de la geometria (como ya se uso en el primer lugar va false)  
    params1=shp_in_pnt+' cota <none> masspoints false'
    params2=shp_in_curvas+' cota <none> softline false'
    #las lineas de rotura no tienen cota asi que va none en lugar del nombre del campo
    params3=shp_in_linrotura+' <none> <none> hardline false'
    #para incluir varias capas al parametro de edittin_3d van separados por ;
    params=params1+';'+params2+';'+params3
    
    #cada capa separada por ; cuando son varias capas
    EditTin_3d(tin_out,params,False)
    
    #devolver la licencia al servidor
    arcpy.CheckInExtension('Spatial')
else:
    print 'licencia no disponible'
    
print 'proceso terminado'