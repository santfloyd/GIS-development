"""
crear un buffer sobre una capa
crear un nuevo shp de salida 
clase implicada->QgsVectorFileWriter 
"""
from PyQt5.QtCore import QVariant

proyecto=QgsProject.instance()

capa_ferro=proyecto.mapLayersByName('FERROCARRIL')[0]
#RUTA SALIDA
shp_salida=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\buffer_ferro_qgis_2.shp'

#crear los campos para el shp de salida
campos= QgsFields()
campo= QgsField('distancia', QVariant.Double)
campos.append(campo)
#sistema de referencia
crs= capa_ferro.dataProvider().crs() #el mismo de la capa de entrada
#crear capa de salida
shp = QgsVectorFileWriter(shp_salida, 'UTF-8',campos,QgsWkbTypes.Polygon,crs,'ESRI Shapefile')
#crear el buffer y rellenar el shp
for i in capa_ferro.getFeatures():
    geom=i.geometry()
    #verificar si la geometria es correcta
    if geom != None:
        #crear el buffer
        b = geom.buffer(200,50)
        #crear una nueva entidad (fila)
        nf=QgsFeature() #devuelve una fila vacia
        #rellenar la entidad
        #geometria
        nf.setGeometry(b)
        #atributos
        nf.setAttributes([200])
        #añadir la fila al shp
        shp.addFeature(nf)

del shp
#anadir el resultado al proyecto
capa_buffer=QgsVectorLayer(shp_salida,'Buffer_200','ogr')
proyecto.addMapLayer(capa_buffer)