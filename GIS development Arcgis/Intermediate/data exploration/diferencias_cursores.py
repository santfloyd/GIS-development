'''
cursores arcpy.da.SearchCursor y arcpy.SearchCursor
'''

import arcpy

shp_mun= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\MUNICIPIO.shp'

consulta=''' "POB91" > 100000 '''

#spatref si queremos que retorne en otro sistema de proyeccion
#los campos a seleccionar separados por ; 
#EL siguiente es ordenado por el campo pob91 A de ascendente D de descendente
cursor=arcpy.SearchCursor(shp_mun, consulta, '', 'NOMBRE;POB91', 'POB91 A') 

for fila in cursor:
    print fila.NOMBRE, fila.POB91

print 20*'-'  #20 guines 


#la diferencia es que con este cursor no se pueden ordenar los campos como con el otro cursor
#el orden de parametros tambien es diferente
#otra diferencia es que los campos vienen como lista con nombres de los campos y va en segunda posicion
#la consulta va en tercera posicion
#la referencia espacial va en cuarta posicion
#otra diferencia es que puede contener tokens
#una mas es que el acceso a las filas es por indice y no por nombre de campo
cursor2=arcpy.da.SearchCursor(shp_mun,['NOMBRE','POB91','SHAPE@AREA'],consulta,'')  #SHAPE@AREA es un token de geometria
#los tokens de geometria son campos virtuales que contienen caracteristicas espaciales que se crean en el momento dentro del cursor

for fila in cursor2:
    #indice de campos
    print fila[0],fila[1],fila[2]/1000000 #area en km cuadrados
del cursor2
    