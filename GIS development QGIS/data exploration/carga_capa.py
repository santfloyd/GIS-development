#-*- coding= utf-8 -*-

"""
carga de una capa vectorial
"""

#path
ruta= r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\PROVINCIA.SHP"

#referencia al objeto capa

capa= QgsVectorLayer(ruta, "PROVINCIAS","ogr") #path, alias, provider

#verificar si la capa es valida
if capa.isValid():
    #acceder al proyecto
    proyecto = QgsProject.instance()
    proyecto.addMapLayer(capa) #como el objeto QgsVectorLayer hace parte de los objetos QgsMapLar se puede pasar sin problema
else:
    print("no se ha podido cargar la capa")