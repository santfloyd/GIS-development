'''
creacion de centroides
'''

import arcpy
import os

#ruta del shape de provincias
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'

shp_mun='MUNICIPIO.shp'

punto=arcpy.Point()

cursor=arcpy.da.SearchCursor(shp_mun,['SHAPE@TRUECENTROID'])

lista=[]

for row in cursor:
    centroide = row[0]
    print centroide
    punto.X=centroide[0]
    punto.Y=centroide[1]
    geom_pnt=arcpy.PointGeometry(punto)
    lista.append(geom_pnt)
del cursor
   
#ruta de salida
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

arcpy.CopyFeatures_management(lista, os.path.join(ruta_out, 'centroides_mun.shp'))
print "proceso terminado"
    