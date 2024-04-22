# -*- coding: utf-8 -*-
"""
Created on Thu May 03 11:07:19 2018

@author: ASUS
"""
#importar clase y modulo 
from xml.sax.handler import ContentHandler
import xml.sax
#crea el objeto parser
xmlParser= xml.sax.make_parser()
#añade la clase para verificar si esa bien estrucurado
xmlParser.setContentHandler(ContentHandler())
#bloque try para controlar el error y sacar mensajes
try:
    xmlParser.parse("GeodatabaseXML2.xml")
    print "it is good fomarted"
except Exception, err:
    print "Error in XML file" + str(err)