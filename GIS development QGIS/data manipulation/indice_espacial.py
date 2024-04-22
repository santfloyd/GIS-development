"""
creacion de un indice espacial
busqueda de vecinos cercanos
"""

proyecto=QgsProject.instance()

capa_esta=proyecto.mapLayersByName('ESTACIONES')[0]
#crear indice espacial
ind_esp= QgsSpatialIndex()
#rellenar el indice con entidades
for i in capa_esta.getFeatures():
    ind_esp.insertFeature(i)
#busqueda de los vecinos cercanos. Devuelve lista de ids
punto=QgsPointXY(260806,4637930)
vecinos=ind_esp.nearestNeighbor(punto,10) #5 primero vecinos
#visualizar los vecinos 
capa_esta.select(vecinos)
#ver algunos atributos de las entidades seleccionadas
for i in capa_esta.getFeatures(vecinos):
    print(i['X'],i['Y'])
    