'''
leer lineas
'''

import arcpy


#ruta del shape de provincias
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'

shp_carre='CARRETERA.shp'

consulta=''' "NOM_MOPT" = 'E05' '''

cursor=arcpy.da.SearchCursor(shp_carre,['SHAPE@'],consulta)

contador=0

for fila in cursor:
    contador +=1
    print 'linea '+ str(contador)
    print 20*'-'
    geom_lin= fila[0]
    primer_punto=geom_lin.firstPoint
    ultimo_punto=geom_lin.lastPoint
    for parte in geom_lin:
        for punto in parte:
            print punto.X, punto.Y

