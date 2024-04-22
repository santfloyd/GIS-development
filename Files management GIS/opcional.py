# -*- coding: utf-8 -*-
"""
Created on Thu May 03 11:59:57 2018

@author: ASUS
"""

#importa modulo y objeto
from xml.dom import minidom
#parsea
xmldoc=minidom.parse("WitchFireResidenceDestroyed.xml")
#recupera los nodos y los lisat
eList=xmldoc.getElementsByTagName("Name")
#lista por etiqueta
print(len(eList))
print(eList[0].attributes['Name'].value)
for e in eList:
    print(e.attributes['Name'].value)