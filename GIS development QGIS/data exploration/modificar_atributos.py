"""
modificar atributos 
"""

proyecto=QgsProject.instance()
capa=proyecto.mapLayersByName('PROVINCIAS')[0]
#definir proveedor
prov=capa.dataProvider()
#recorrido por las entidades
for e in capa.getFeatures():
    if e['NOMBRE'] == 'VALLADOLID1':
        id_campo=e.fieldNameIndex('NOMBRE') #ID DEL CAMPO DE INTERES
        prov.changeAttributeValues({e.id():{id_campo:'VALLADOLID'}}) #se le pasa un dict-> la clave es el id y como valor otro dict con el id del campo y el valor NUEVO al que se quiere cambiar
