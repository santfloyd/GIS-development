#-*- coding: utf-8 -*-
'''
acceso a als capas del proyecto
mapLayers -> diccionario
mapLayerByName -> lista
'''
from PyQt5.QtWidgets import QMessageBox

#acceso al proyecto
proyecto=QgsProject.instance()

#devuelve un diccionario
capas=proyecto.mapLayers()


nom_capas=[capa.name() for capa in capas.values()]
print(nom_capas)
numero_capas=len(nom_capas)
print(numero_capas)
#para concatener la lista se usa join a la cadena y map con una lambda para convertir a str y añadir un salto de line
mensaje='el proyecto tiene: '+str(numero_capas)+' '+'capas: '+'\n'+' '.join(map(lambda x: str(x)+'\n', nom_capas))
QMessageBox.information(None,'propiedades',mensaje)