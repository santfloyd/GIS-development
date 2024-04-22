'''
mismo bucle sin bucle for
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
cursor=arcpy.SearchCursor(capa)

#sin bucle
row=cursor.next() #aqui ya se esta en la primera fila
while row:
    print row.getValue('NOMBRE')
    row=cursor.next()
    

