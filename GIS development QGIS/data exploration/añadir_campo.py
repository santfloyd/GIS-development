"""
ANADIR CAMPO
"""
from PyQt5.QtCore import QVariant #para definicion de tipos de datos

proyecto=QgsProject.instance()
capa=proyecto.mapLayersByName('PROVINCIAS')[0]
prov=capa.dataProvider()
#verificar existencia de campo
campos=capa.fields()
if campos.indexFromName('INDICE') == -1:#-1 que no exite indexFromName el indice al nombre de campo que se le pase
    #crear campo
    campo= QgsField('INDICE', QVariant.Double) #NOMBRE DE CAMPO Y TIPO DE DATO con QVariant
    #añadir campo
    prov.addAttributes([campo])
    #actializar estructura de campos
    capa.updateFields()

#inicializar valores del campo a 0
campos=capa.fields()
id_field=campos.indexFromName('INDICE')
for e in capa.getFeatures():
    prov.changeAttributeValues({e.id():{id_field:0}}) #se le pasa un dict-> la clave es el id y como valor otro dict con el id del campo y el valor NUEVO al que se quiere cambiar

