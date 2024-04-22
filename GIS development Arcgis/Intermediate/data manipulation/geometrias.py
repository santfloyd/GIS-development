'''
LECTURA DE PUNTOS
'''

import arcpy


#ruta del shape de puntos
shp_pnt= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\NUCLEOS.shp'

cursor=arcpy.SearchCursor(shp_pnt)

for row in cursor:
    geom=row.shape
    punto = geom.firstPoint
    print punto.X, punto.Y
    break #para interrimpir en la primera iteracion
del cursor

#mediante .da
print "_____________"
cursor2=arcpy.da.SearchCursor(shp_pnt,['SHAPE@']) #el token trae la geometria directamente

for row in cursor2:
    geom=row[0]
    punto=geom.firstPoint
    print punto.X, punto.Y
    break
del cursor2
    