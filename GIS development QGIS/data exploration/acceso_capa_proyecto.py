#-*- coding: utf-8 -*-
'''
acceso a als capas del proyecto
mapLayers -> diccionario
mapLayerByName -> lista
'''

#acceso al proyecto
proyecto=QgsProject.instance()

#devuelve un diccionario
capas=proyecto.mapLayers()

for capa in capas.values():
    print(capa.name())
print(50*'-')
#acceso a una capa por su nombre
capas=proyecto.mapLayersByName('MUNICIPIO')

if len(capas)!=0:
    print(capas[0].name())