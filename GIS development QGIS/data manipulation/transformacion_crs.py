"""
transformacr crs
"""

proyecto=QgsProject.instance()

capa_mun=proyecto.mapLayersByName('MUNICIPIO')[0]

#SISTEMA DE REF
crs_origen = capa_mun.dataProvider().crs()
crs_destino = QgsCoordinateReferenceSystem(25830,QgsCoordinateReferenceSystem.EpsgCrsId) #el segundo parametro le indica que el primer parametro es el codigo epsg
#punto de origen
punto_orig=QgsPointXY(354403,4613781)
#sistema de transformacion entre crs
paso = QgsCoordinateTransform(crs_origen, crs_destino, proyecto)
punto_destino=paso.transform(punto_orig)
print(punto_orig.x(),punto_orig.y())
print(punto_destino.x(),punto_destino.y())