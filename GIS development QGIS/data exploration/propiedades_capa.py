"""
acceder propiedades capas
"""

#acceso al proyecto

proyecto=QgsProject.instance()

#ACCESO A LA CAPA POR NOMBRE
capa=proyecto.mapLayersByName('MUNICIPIO')[0]

#visualizacion de propiedades
print(capa.source()) #path
print(capa.name()) #nombre
print(capa.type()) #tipo de dato
print(capa.geometryType()) #tipo de geometria
crs=capa.crs() # codigo de sistema de ref
print(crs)
print(crs.description()) #descripcion del sistema de ref
bb=capa.extent() #bounding box -> qgis Rectangle
print(bb.xMinimum(), bb.yMinimum, bb.xMaximum(), bb.yMaximum()) 
proveedor=capa.dataProvider() 
print(proveedor.description())
