"""
DESCRIPCION DEL SISTEMA DE REFERENCIA ESPACIAL
"""

proyecto=QgsProject.instance()

capa_mun=proyecto.mapLayersByName('MUNICIPIO')[0]
#SISTEMA DE REF
crs = capa_mun.dataProvider().crs()
#imprimir en codigo epsg
print(crs.authid())
#CREACION DE UN SISTEMA DE REFERENCIA
n_crs= QgsCoordinateReferenceSystem(25830,QgsCoordinateReferenceSystem.EpsgCrsId) #el segundo parametro le indica que el primer parametro es el codigo epsg
print(n_crs.authid())

