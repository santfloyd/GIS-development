"""
lectura de puntos
clase implicada: QgsGeometry
"""

proyecto=QgsProject.instance()

capa_esta=proyecto.mapLayersByName('ESTACIONES')[0]
#acceso a las entidades
for i in capa_esta.getFeatures():
    #acceso a geometria
    geom = i.geometry()
    print(geom.type()) #saca texto 0 punto 1 linea 3 polygon
    print(geom.wkbType()) #devuelve un enumerador que parte de 1 point
    print(QgsWkbTypes.displayString(geom.wkbType())) #devuelve el string asociado al enumerador
    #acceso a las coordenadas del punto
    punto= geom.asPoint() #devuelve QgsPointXY
    print(punto.x(), punto.y())
    break
    
    
