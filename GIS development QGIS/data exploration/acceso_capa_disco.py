#-*- coding: utf-8 -*-

'''
acceder a una capa vectorial
en disco
'''

#acceso (ruta,nombre,proveedor)
ruta=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\PROVINCIA.SHP'
capa=QgsVectorLayer(ruta,'prov','ogr')
print(capa.name())
print(capa.featureCount())