# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:16:16 2018

@author: ASUS
"""

import ogr, os
#definicion del workspace
os.chdir('E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#determinar el driver para manejar el archivo objetivo
driver=ogr.GetDriverByName('ESRI Shapefile')


#identificacion del archivo objetivo y abrirlo con el driver, 0 es en modo lectura
dataSource=driver.Open('Building_Permits.shp',0)
dataSource1=driver.Open('Census_Tracts.shp',0)
#crear la layr OGR con getlayer a partir del archivo de origen
layer=dataSource.GetLayer()
layer1=dataSource1.GetLayer()

#filtro a cada capa
print "Building total:",  layer.GetFeatureCount()
layer.SetAttributeFilter("SUBDESC=  'Commercial'")
print "Entidades filtradas Building:", layer.GetFeatureCount()

print "Census total:",layer1.GetFeatureCount()
layer1.SetAttributeFilter("TRT2000= '002416'")
print "Entidades filtradas Census:", layer1.GetFeatureCount()
#adicional a estos filtros se aplicara un filtro espacial que recoje los filtros ya hechos y OGR copia la ultima estancia
#del elemento en este caso layer y layer1
#filtro espacial, se crea una variable que tiene un iterador sobre la capa con la cual se quiere intersectar la capa
#de interes, en este caso itera sobre la capa poligonal con el filtro aplicado antes
layer_ref=layer1.GetNextFeature()
#luego  la variable recien creada se pasa dentro de otra variable que recoje las geometrias de la seleccion hecha con 
#el filtro anterior.
poly=layer_ref.GetGeometryRef()
#se aplica el metodo setspatialfilter sobre la capa de puntos y se pasa como parametro la variable anterior que tiene las 
#geometrias de las entidades filtradas
layer.SetSpatialFilter(poly)
print "la cantidad de edificios comerciales dentro del poligono censal es:",layer.GetFeatureCount()
#destuye para habilitar su contenido
dataSource.Destroy()
dataSource1.Destroy()