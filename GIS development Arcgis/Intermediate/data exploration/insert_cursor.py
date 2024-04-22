'''

'''

import arcpy
from math import sqrt



shp_prov= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\PROVINCIA.shp'

campos=arcpy.ListFields(shp_prov)

lista_nombres=[campo.name for campo in campos]
print(lista_nombres)
if not 'CC' in lista_nombres:
    arcpy.AddField_management(shp_prov,'CC','FLOAT',10,3) #10 numero de digitos 3 numero de decimales

cursor=arcpy.UpdateCursor(shp_prov)
for fila in cursor:
    area=fila.getValue('AREA')
    perim=fila.getValue('PERIMETER')
    cc=0.28*(perim/sqrt(area))
    fila.setValue('CC',cc)
    cursor.updateRow(fila) #fundamental
del cursor
print 'proceso terminado'
    
    
