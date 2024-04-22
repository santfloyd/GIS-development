"""
lectura de poligonos
clase implicada: QgsGeometry
"""

proyecto=QgsProject.instance()

capa_prov=proyecto.mapLayersByName('PROVINCIAS')[0]
#acceso a las entidades
for i in capa_prov.getFeatures([2]):
    #acceso a geometria
    geom = i.geometry()
    print(QgsWkbTypes.displayString(geom.wkbType())) #imprime tipo de geometria
    multipo= geom.asMultiPolygon()
    print(len(multipo))
        #recorrido por la multiligon
    for poly in multipo:
        for p in poly: #estos serian anillos internos del poligono
            for punto in p:
                print(punto.x(), punto.y())
        print(50*'-') #separar los diferentes anillos