# -*- coding: utf-8 -*-
"""
Created on Thu May 03 11:46:28 2018

@author: ASUS
"""

#importa modulo y objeto
from xml.dom import minidom
#parsea
xmldoc=minidom.parse("WitchFireResidenceDestroyed.xml")
#recupera los nodos y los lisat
childNodes=xmldoc.childNodes
#lista por etiqueta
eList=childNodes[0].getElementsByTagName("fire")
#itera en la lista de nodos y recupera los valores
for e in eList:
    #determina cuales tienen un attributo
    if e.hasAttribute("address"):
        #si lo tiene saca el valor
        print e.getAttribute("address")