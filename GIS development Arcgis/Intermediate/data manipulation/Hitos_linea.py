'''
Hitos kilometricos 
'''

import arcpy
import os

#ruta del shape de provincias
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'

shp_carre='CARRETERA.shp'

consulta=''' "FID" = 1302 '''

cursor=arcpy.da.SearchCursor(shp_carre,['SHAPE@', 'SHAPE@LENGTH'],consulta)

distance=1000
puntos=[]
for fila in cursor:
    geom_lin= fila[0]
    longi= fila[1]
    distancias=range(0,int(longi),distance)
    for d in distancias:
        punto=geom_lin.positionAlongLine(d,False)
        puntos.append(punto)

#ruta de salida
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

arcpy.CopyFeatures_management(puntos, os.path.join(ruta_out, 'hitos_carretera.shp'))
print "proceso terminado"