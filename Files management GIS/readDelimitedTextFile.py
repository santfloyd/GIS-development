# -*- coding: utf-8 -*-
"""
Created on Tue May 01 09:50:01 2018

@author: ASUS
"""
#abre el fichero con la info
file1=open("C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\N_America.A2007275.txt", 'r')
#lee las lineas separadamente
Lstfires=file1.readlines()
#loop para que de cada linea separe por index de la lista que viene a ser cada linea
for line in Lstfires:
    Lstfires=line.split(",")
    latitud=float(Lstfires[0])
    longitud=float(Lstfires[1])
    confid=int(Lstfires[8])
    #solo devuelve lo valores indicados
    print "latitud es:" + str(latitud)  + "longitud es:" + str(longitud) + "valor de confianza es:" + str(confid)

file1.close()