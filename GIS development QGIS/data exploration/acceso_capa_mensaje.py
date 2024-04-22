#-*- coding: utf-8 -*-
'''
acceso al proyecto
'''

from PyQt5.QtWidgets import QMessageBox

proyecto=QgsProject.instance()


ruta=proyecto.fileName()
nombre=proyecto.baseName()
titulo=proyecto.title()
mensaje='ruta: '+ruta+'\n'+'Nombre: '+ \
    nombre+'\n'+'Titulo'+titulo
QMessageBox.information(None,'propiedades',mensaje)