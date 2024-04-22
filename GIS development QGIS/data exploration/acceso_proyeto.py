#-*- coding: utf-8 -*-
'''
acceso al proyecto
'''


#acceso al proyecto
proyecto=QgsProject.instance()
#imprime ruta
print(proyecto.fileName())
#imrpime nombre
print(proyecto.baseName())
###imprime titulo
print(proyecto.title())
#