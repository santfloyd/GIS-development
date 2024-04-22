"""
seleccion espacila combinada: espacial y por atributos
"""

proyecto=QgsProject.instance()
capa_prov=proyecto.mapLayersByName('PROVINCIAS')[0]
capa_esta=proyecto.mapLayersByName('ESTACIONES')[0]

#CONSULTA POR ATRIBUTOS
consulta=''' NOMBRE = 'BURGOS' '''

for i in capa_prov.getFeatures(consulta):
    geom_prov = i.geometry()
#lista de identificadores
ids=[]
#recorido por la lista  de entidades en estaciones
for i in capa_esta.getFeatures():
    #acceso a la geometria
    geom_esta = i.geometry()
    #test de inclusion
    if geom_prov.contains(geom_esta):
        #anadir el identificador de la entidad
        ids.append(i.id())
        
#visualizar las entidades seleccionadas segun la lista de ids incluidos
capa_esta.select(ids)
        