"""
lectura de lineas
clase implicada: QgsGeometry
"""

proyecto=QgsProject.instance()

capa_ferro=proyecto.mapLayersByName('FERROCARRIL')[0]
#acceso a las entidades
for i in capa_ferro.getFeatures([187]):
    #acceso a geometria
    geom = i.geometry()
    print(QgsWkbTypes.displayString(geom.wkbType())) #imprime tipo de geometria
    #VERIFICAR SI UNA GEOMETRIA ES MUILTIPLE
    print('multipart? ', geom.isMultipart())
    #acceso a las coordenadas como es multiparte se usa asMultyPolyline
    multi= geom.asMultiPolyline()
    print(len(multi))
    #recorrido por la multilinea
    for m in multi:
        for punto in m:
            print(punto.x(), punto.y())
            
        
    
    