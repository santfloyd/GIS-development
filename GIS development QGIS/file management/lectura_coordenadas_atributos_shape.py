# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:20:15 2018

@author: ASUS
"""
#importar modulos os para definir el workspace
import ogr, os
#definicion del workspace
os.chdir('E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#determinar el driver para manejar el archivo objetivo
driver=ogr.GetDriverByName('ESRI Shapefile')
#identificacion del archivo objetivo y abrirlo con el driver, 0 es en modo lectura
dataSource=driver.Open('fires.shp',0)
#crear la layr con getlayer a partir del archivo de origen
layer=dataSource.GetLayer()
#conteo de entidades en el shp
numFeatures=layer.GetFeatureCount()
print 'Feature count:' + str(numFeatures)
#determinar el extent de la capa
extent= layer.GetExtent()
print 'Extent', extent
# identificacion del limite izquierdo y superior
print 'left and Top:', extent[0],extent[3]
#limite derecho e inferior
print 'Right and Bottom:', extent[1],extent[2]
#identificar el sistepa de referencia espacial
SpatRef= layer.GetSpatialRef()
print 'Spatial reference:', SpatRef
#confirmar el nombre de la layer objetivo
nombre=layer.GetName()
print 'nombre:',nombre

#creacion de una variable feature que contenga el iterador sobre la layer, se puede usar tambien una for loop pero mejor esta
feature=layer.GetNextFeature()
while feature:
    #imprima cada feature
    print 'feature:', feature
    #identifica en la variable confidence las entidades con el campo CONFIDENCE
    confidence=feature.GetFieldAsString('CONFIDENCE')
    print 'confidence:', confidence
    #en la variable geometry identifica la geometria
    geometry=feature.GetGeometryRef()
    #en las veriables x,y extrae las coordenadas x, y
    x=str(geometry.GetX())
    y=str(geometry.GetY())
    print 'coordenada x:', x
    print 'coordenada x:', y
    #destruye la feature
    feature.Destroy()
    #inicia en la siguiente entidad y hace todo el loop
    feature=layer.GetNextFeature()
#cierra el data soruce una vez termina todos los procesos    
dataSource.Destroy()