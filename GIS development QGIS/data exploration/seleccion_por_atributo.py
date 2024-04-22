"""
seleccion por atributo
"""

proyecto=QgsProject.instance()
capa=proyecto.mapLayersByName('MUNICIPIO')[0]
#consulta
consulta='POB95 >= 5000'
#elminar seleccion previa
capa.removeSelection()
#ACCESO A LAS ENTIDADES (SIMILAR A LOS CURSORES DE ARCPY)
#entidades= capa.getFeatures(consulta) #es muy flexible, sin pasarle nada coge todo, consulta coge consulta o si recibe id coge los id
entidades=capa.getFeatures(QgsFeatureRequest().setFilterExpression(consulta)) #es equivalente a la linea anterior, pero admite tambien rectangulos cambiando a setFilterRect o por ids setFilterFids
ids= [ent.id() for ent in entidades] #getFeatures devuelve un objeto con metodos como id
capa.select(ids)

capa2=proyecto.mapLayersByName('PROVINCIAS')[0]
#consulta2='NOMBRE = \'BURGOS\'' #REQUIERE contrabara y escape o SE PUEDE COMO EN LA LINEA SIGUIENTE 
consulta2='''NOMBRE = 'BURGOS' '''
entidades2= capa2.getFeatures(consulta2)
ids2= [ent.id() for ent in entidades2]
capa2.select(ids2)