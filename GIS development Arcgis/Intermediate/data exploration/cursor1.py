'''
SEARCH CURSOR
'''


import arcpy
import arcpy.mapping as map

#identificar carpeta de trabajo
ruta_mxd=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\proyecto1.mxd'

def getLayerByName(mxd, df, nombre):
    capas=map.ListLayers(mxd, '', df)
    for capa in capas:
        if capa.name==nombre:
            return capa
        
mxd=map.MapDocument(ruta_mxd)
df0=map.ListDataFrames(mxd)[0]
capa=getLayerByName(mxd, df0, 'PROVINCIA')

#cuando ya se ha recorrido el cursor, hay que volverlo a declarar con otra variable cursor2 para volver a usarlo
cursor=arcpy.SearchCursor(capa)
for fila in cursor:
    print fila.getValue('NOMBRE')

#eliminar el cursor
del cursor

#mejor usar with
#with arcpy.SearchCursor(capa) as cursor:
#for fila in cursor:
    #print fila.getValue('Nombre')
    
#para no hacer un bucle for usar while y next



