# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:25:16 2018

@author: ASUS
"""

import ogr, os
#definicion del workspace
os.chdir('E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos')
#determinar el driver para manejar el archivo objetivo
driver=ogr.GetDriverByName('ESRI Shapefile')
#crear data source nuevo con aplicacion del driver identificado
ds=driver.CreateDataSource('N_America.shp')
#nombrar la capa vectorial e indicar el tipo de geometria
layer=ds.CreateLayer('N_America', geom_type=ogr.wkbPoint)
#asegurarse de que se creo una nueva capa vectorial
if os.path.exists('N_America.shp'):
    print 'layer existente:', layer.GetName()

#identificacion de cada campo, su nombre y tipo de dato con ogr.FieldDefn, primero crear campos en la layer OGR
fidDef=ogr.FieldDefn('latitud', ogr.OFTInteger64)
fidDef1=ogr.FieldDefn('longitud', ogr.OFTInteger64)
fidDef2=ogr.FieldDefn('bright', ogr.OFTInteger64)
fidDef3=ogr.FieldDefn('scan', ogr.OFTInteger64)
fidDef4=ogr.FieldDefn('trac', ogr.OFTInteger64)
fidDef5=ogr.FieldDefn('date', ogr.OFTString)
fidDef6=ogr.FieldDefn('time', ogr.OFTInteger64)
fidDef7=ogr.FieldDefn('satellite', ogr.OFTString)
fidDef8=ogr.FieldDefn('confid', ogr.OFTInteger64)
#Creación de los campos identificados en la layer, luego crear los campos en la layer OGR
layer.CreateField(fidDef)
layer.CreateField(fidDef1)
layer.CreateField(fidDef2)
layer.CreateField(fidDef3)
layer.CreateField(fidDef4)
layer.CreateField(fidDef5)
layer.CreateField(fidDef6)
layer.CreateField(fidDef7)
layer.CreateField(fidDef8)
#recuperar la layer con los campos creados en la variable featureDefn
featureDefn=layer.GetLayerDefn()
#abrir fichero de texto  
file1=open("E:\GeoSpatialTraining\Python_GIS_OPENSOURCE\datos\Datos\N_America.A2007275.txt", 'r')
#crear lista con el metodo readlines sobre el fichero de texto
Lstfires=file1.readlines()
print Lstfires
#loop para que de cada linea separe por coma y a cada variable le adjudique una division identificada por indice
for line in Lstfires:
    Lstfires=line.split(",")
    latitud=float(Lstfires[0])
    longitud=float(Lstfires[1])
    bright=float(Lstfires[2])
    scan=float(Lstfires[3])
    trac=float(Lstfires[4])
    date=str(Lstfires[5])
    time=float(Lstfires[6])
    satellite=str(Lstfires[7])
    confid=int(Lstfires[8])    


#todo lo siguiente dentro de la loop para que rellene cada campo en la layer OGR por cada valor de la lista de texto identificado
#en la variable point se indica el tipo de geometria con el metodo ogr.Geometry
    Point=ogr.Geometry(ogr.wkbPoint)
#se añade el punto con los valores de las variables identificadas en el bucle para lectura del csv
    Point.AddPoint(longitud, latitud)
#crear nueva entidad en la variable que almacena la layer
    feature=ogr.Feature(featureDefn)
#a cada entidad se le establece la geometria con los valores contenidos en la variable Point
    feature.SetGeometry(Point)
#rellena cada campo identificado y creado en la layer indicando el nombre y el valor
    feature.SetField('latitud', latitud)
    feature.SetField('longitud', longitud)
    feature.SetField('bright', bright)
    feature.SetField('scan', scan)
    feature.SetField('trac', trac)
    feature.SetField('date', date)
    feature.SetField('time', time)
    feature.SetField('satellite', satellite)
    feature.SetField('confid', confid)

#salva los registros recien creados
    layer.CreateFeature(feature)
#destruye las variables para que el iterador funcione correctamente tras cada iteracion
    Point.Destroy()
    feature.Destroy()
#destruye el datasource para habilitar su contenido    
ds.Destroy()
