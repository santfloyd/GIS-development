'''
ejecicicos practicos carga de capas en orden alfabetio
'''

import os

#path de todas las capas y la extension
path=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'
extension='.SHP'

#instancia del proyecto
proyecto=QgsProject.instance()

#lista de capas con la extension .shp y oredenacion alfabetica
capas=[shp for shp in os.listdir(path) if shp.endswith(extension)]
capas.sort()
print(capas)

#por cada capa en la lista crear la capa vctorial desde el path y añadirla
for capa in capas:
    capa=QgsVectorLayer(os.path.join(path,capa),capa,'ogr')
    proyecto.addMapLayer(capa)
iface.zoomFull()
        
