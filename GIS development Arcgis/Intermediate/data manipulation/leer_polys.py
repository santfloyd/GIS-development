'''
leer poligonos
'''

import arcpy
import os

#ruta del shape de provincias
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'

shp_carre='PROVINCIA.shp'


consulta=''' "NOMBRE" = 'BURGOS' '''

cursor=arcpy.da.SearchCursor(shp_carre,['SHAPE@'],consulta)

for fila in cursor:
    geom_poly=fila[0]
    for parte in geom_poly:
        for punto in parte:
            if punto != None:
                print punto.X, punto.Y
    