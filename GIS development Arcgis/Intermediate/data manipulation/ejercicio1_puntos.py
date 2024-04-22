'''
Desplaza las geometrias de punto en X e Y, la distancia que se le indique

@author: Santiago Alejandro Ortiz Hernandez
'''

import arcpy
import os

arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

#shape de salida
shp_out=os.path.join(ruta_out, 'nucleos_trasladados.shp')

#shape de puntos
shp_nuc='NUCLEOS.shp'


#si existe la capa de salida la elimina y hace nuevamente una copia
if arcpy.Exists(shp_out):
                arcpy.Delete_management(shp_out)
else:
    arcpy.Copy_management(shp_nuc, shp_out)

def translate_XY(shp, increment_list=None):
    if increment_list == None:
        increment_list = [0, 0]
    
    #uso de token XY sobre la capa de salida recien copiada
    cursor=arcpy.da.UpdateCursor(shp_out,['SHAPE@XY'])
    
    #cursor para almacenar los incrementos
    for row in cursor:
        
        #para realizar el update es necesario usar una lista dentro de otra lista 
        #y asi coincide con el output del token shape@xy para cada fila
        cursor.updateRow([[row[0][0]+increment_list[0],row[0][1]+increment_list[1]]])
        print([[row[0][0]+increment_list[0],row[0][1]+increment_list[1]]])
    del cursor 
    return

#lista con incremento en X e Y
incremento_XY=[200,150]

translate_XY(shp_out, incremento_XY)

print "proceso terminado"
