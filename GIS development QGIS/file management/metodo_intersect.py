# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:03:38 2018

@author: ASUS
"""


import ogr, os
#definicion del workspace
os.chdir('E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#determinar el driver para manejar el archivo objetivo
driver=ogr.GetDriverByName('ESRI Shapefile')


#identificacion del archivo objetivo y abrirlo con el driver, 0 es en modo lectura
dataSource=driver.Open('Census_Tracts.shp',0)
dataSource1=driver.Open('railroad_capcog.shp',0)
#crear la layr con getlayer a partir del archivo de origen
layer=dataSource.GetLayer()
layer1=dataSource1.GetLayer()
#crear contadores para contabilizar el numero de entidades intersectadas en cada capa
numero=0
numero2=0
#bucle que recorre las entidades de la layer de referencia para intersectar con la layer objetivo
feature=layer.GetNextFeature()
while feature:
    #otro iterador que recorra las entidades de la capa objetivo
    linea=layer1.GetNextFeature()
    #recoje las geometrias de la capa de referencia dentro de la capa de referencia
    polygon=feature.GetGeometryRef()
    #crea un condicional para iterar en la capa objetivo
    while linea:
        #recupera las geometrias de las entidades de la capa objetivo almacenadas en la variable linea que itera en cada entidad
        lineas=linea.GetGeometryRef()
        #aplica la interseccion a la capa poligonal pasando como parametro la variable lineas
        intersec=polygon.Intersect(lineas)
        #si el resultado de la intersect es verdaero
        if intersec is True:
            #en la variable identificador recuera el valor del campo deseado desde el iterador sobre la capa de referencia
            identificador=feature.GetField('TRT2000')
            #incrementa el contador en uno
            numero=numero+1
            print "entidades de la capa de referencia poligonal:", identificador
            numero2=numero2+1
            feature.Destroy()
            feature = layer.GetNextFeature()
            layer1.ResetReading() # required if looping again
            break
        else:
            lineas.Destroy()
            break
    else: 
        layer.ResetReading() # required if looping again
        feature.Destroy()
        feature= layer1.GetNextFeature()
dataSource.Destroy()
dataSource1.Destroy()

print numero
print numero2        