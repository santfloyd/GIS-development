# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:30:17 2018

@author: ASUS
"""

#modulos
import HTMLParser
import urllib
import sys
#crea variable con la url
urlString="http://www.geospatialtraining.com/"
#funcion que abre la pagina y parsea la info
def getImage(addr):
    u=urllib.urlopen(addr)
    data=u.read()
    splitPath=addr.split('/')
    print splitPath
    fName=splitPath.pop(2)
    print "saving %s" % fName
    f=open(fName, "wb")
    f.write(data)
    f.close()
#crae la clase parseimages para extraer imagenes de una web se define
#la lcase htmlparser reemplazando el metodo handle_starttag() para buscar <img>
class parseImages(HTMLParser.HTMLParser):
    def handle_starttag(self,tag,attrs):
        if tag=='img':
            for name,value in attrs:
                if name=='src':
                    getImage(urlString + '/' + value)

#abrir instancia parse images
IParser=parseImages()
#abrir url y sacar encabezados
u=urllib.urlopen(urlString)
print "Opening URL\n==============================="
print u.info()
#pasa contenidos a la instancia parse images
IParser.feed(u.read())
IParser.close()
