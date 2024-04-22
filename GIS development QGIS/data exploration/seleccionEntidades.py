"""
metodos de seleccion de entidades
"""

proyecto=QgsProject.instance()
capa=proyecto.mapLayersByName('MUNICIPIO')[0]

#capa.selectAll() #seleccionar todo
#capa.removeSelection() #desseleccionar todo
#capa.select(100) #seleccionar por id (admite lista o rango)
#capa.select([100,200,300])
#capa.select(list(range(100,300)))
#capa.deselect(list(range(100,230)))
#print(capa.selectedFeatureCount()) #contar elementos seleccionados
bb = QgsRectangle(344093,4583913, 373119,4614689) #seleccionar por rectangulo
#metodos de seleccion
#SetSelection -> nueva seleccion
#AddToSelection -> anadr a la seleccion
#IntersectSelection -> intersectar selecciones
#RemoveFromSelection -> deseleccionar de la seleccion previa
capa.selectByRect(bb,QgsVectorLayer.SetSelection)
#bounding de la seleccion
#bb2=capa.boundingBoxOfSelected() #extension de la seleccion
#print(bb2.xMinimum(), bb2.yMinimum, bb2.xMaximum(), bb2.yMaximum()) 
#invertir seleccion
capa.invertSelection()