#-*- coding: utf-8 -*-
'''
añadir capa al proyecto
'''

#ruta capa
ruta=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\PROVINCIA.SHP'
#REFERENCIA A LA ACPA
capa=QgsVectorLayer(ruta,'prov','ogr')

#acceso al proyecto
proyecto=QgsProject.instance()

#verificar si la capa es valida
if capa.isValid():
    #se añade la capa
    proyecto.addMapLayer(capa)
else:
    print('la capa no es valida')
#zoom a la extension de todas las capas
iface.zoomFull()