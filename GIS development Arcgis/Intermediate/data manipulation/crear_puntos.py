'''
crear shp con los nucleos urbanos de la provincia de burgos
Las capas deben de tener un SRC definido
'''

import arcpy
import os

arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'

shp_prv='PROVINCIA.shp'
shp_nuc='NUCLEOS.shp'

consulta=''' "NOMBRE"= 'BURGOS' '''

cursor=arcpy.da.SearchCursor(shp_prv,['SHAPE@'],consulta)

for row in cursor:
    geom_poly=row[0]
del cursor

lista_nucleos=[]

cursor2=arcpy.da.SearchCursor(shp_nuc,['SHAPE@'])

for row in cursor2:   
    geom_pnt = row[0]
    if geom_poly.contains(geom_pnt):
        lista_nucleos.append(geom_pnt)
del cursor2 

#ruta de salida
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

arcpy.CopyFeatures_management(lista_nucleos, os.path.join(ruta_out, 'nucleos_seleccionados.shp'))
print "proceso terminado"
