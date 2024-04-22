'''
cursor con condicion
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
capa=getLayerByName(mxd, df0, 'MUNICIPIO')
cursor=arcpy.SearchCursor(capa, ''' "POB91"< 5000 ''')

#sin bucle
row=cursor.next() #aqui ya se esta en la primera fila
while row:
    print row.getValue('NOMBRE')
    row=cursor.next()
    
# CONDICIONAL aplicado por fila
for fila in cursor:
    fila.getValue('NOMBRE') == fila.NOMBRE
    print fila.getValue('NOMBRE')

#eliminar el cursor
del cursor
