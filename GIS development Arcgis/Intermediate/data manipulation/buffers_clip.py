'''
carreteras a menos de 1 km de los nucleos
'''

import arcpy
import os


arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

#shapes de salida
shp_out_buff=os.path.join(ruta_out, 'buffer_nuc_1000.shp')
shp_clip_buff=os.path.join(ruta_out, 'carre_clip_buff.shp')

#shp de trabajo
nucleos='NUCLEOS.shp'
carreteras='CARRETERA.shp'

#herramienta buffer
arcpy.Buffer_analysis(nucleos,shp_out_buff, 1000)

#herramienta clip
arcpy.Clip_analysis(carreteras,shp_out_buff, shp_clip_buff)

#opcionalmente se puede eliminar los intermedios
arcpy.Delete_management(shp_out_buff)

print('proceso terminado')