# -*- coding: utf-8 -*-
"""
Created on Thu May 03 10:49:09 2018

@author: ASUS
"""
#modulo para leer xml y objeto
from xml.dom import minidom
#variable y metodo .parse del objeto y nombre del archivo como parametro
domTree=minidom.parse("GeodatabaseXML2.xml")
#muestra la estructura del archivo, toas sus etiquetas, jerarquias y valores
print domTree.toxml()