"""
transformacr crs toda la capa
"""

proyecto=QgsProject.instance()

capa_mun=proyecto.mapLayersByName('MUNICIPIO')[0]

#SISTEMA DE REF

crs_destino = QgsCoordinateReferenceSystem(25830,QgsCoordinateReferenceSystem.EpsgCrsId) #el segundo parametro le indica que el primer parametro es el codigo epsg
ruta_salida=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\muni_25830.shp'
#devuelve una lista con dos valores un codigo de error si no error 0, y devuelve 
test= QgsVectorFileWriter.writeAsVectorFormat(capa_mun, ruta_salida,'UTF-8', crs_destino,'ESRI Shapefile') 
if test[0] ==  QgsVectorFileWriter.NoError:
    capa_reproj = QgsVectorLayer(ruta_salida,'MUN_25830','ogr')
    proyecto.addMapLayer(capa_reproj)
    print('capa reproyectada')
else:
    print(test)
    print('se ha producido un error')