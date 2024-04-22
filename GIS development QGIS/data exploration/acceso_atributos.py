"""
ACCEDER A TODAS LAS ENTIDADES
"""

proyecto=QgsProject.instance()
capa=proyecto.mapLayersByName('PROVINCIAS')[0]

#ACCESO A ENTIDADES
entidades=capa.getFeatures()
for e in entidades:
    print(e.attribute('NOMBRE'))
    #generar un dict (EQUIVALENTE A LA LINEA ANTERIOR)
    print(e['NOMBRE'])