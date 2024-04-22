# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 15:49:54 2018

@author: ASUS
"""

# Nombre: Santiago Ortiz  
# Fecha: febrero 5 de 2018 
# Objetivo: Este script se usará para probar la funcionalidad provista por el lenguaje 
#Python. This script will be used to test the basic functionality provided by the 


#1
myName = 'John Doe' 
print myName
#2
a = 'Hello'
b = ' World' 
c = a + b 
print c
#3
theString = 'Floodplain.shp' 
theLayer = theString[0:10] 
print theLayer
#4
a = 10 
b = 20 
c = a + b
print c
#5
fcList = ['Hydrants', 'Water Mains', 'Valves', 'Wells']
print fcList[0] 
print fcList[3]
#6
fcList = ['Water Mains', 'Hydrants', 'Wells', 'Valves'] 
fcList.append('Blowoff Valves') 
fcList.sort() 
print len(fcList) 
for lyr in fcList: 
    print lyr
#7
dictLayers = {'Roads':0, 'Airports':1, 'Railroads':2}
print dictLayers['Railroads']
#8
dictLayers = {'Roads':0, 'Airports':1, 'Railroads':2} 
listLayers = dictLayers.keys() 
for lyr in listLayers:
    print lyr
#9
listLayers = ["Roads","Airports","Railroads"] 
fc = listLayers[1] 
if fc == 'Roads': 
    print "Found the Roads layer"
elif fc == 'Airports': 
    print "Found the Airports layer"
else: 
    print "Found the Railroads layer"
    
#10
dictLayers = {"Roads":"Polyline","Rail":"Polyline","Parks":"Polygon","Schools":"Point"} 
listLayers = dictLayers.keys() 
for lyr in listLayers: 
    if dictLayers[lyr] == "Polyline": 
        print lyr
#11
import math
print dir(math)
#12 dos lineas al piso seguidas
print math.floor.__doc__
#13
print math.floor(102.4)
