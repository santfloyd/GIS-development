'''
seleccion por atributos y localizacion provincias castilla leon
'''

#importar librerias
import arcpy
import os

#identificar carpeta de trabajo
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'

#ruta de salida
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

#shapes de trabajo
muni="MUNICIPIO.shp"
stations="ESTACIONES.shp"

#creacion de capas virtuales
arcpy.MakeFeatureLayer_management(muni, 'municipio')
arcpy.MakeFeatureLayer_management(stations, 'estaciones')

#inspeccion de campos para crear la consulta
fieldlist=arcpy.ListFields(muni)

for field in fieldlist:
    print field.name, field.type

#query
consulta=''' "POB95" > 5000 ''' 

#primera selecion por atributos sobre la capa municipio
arcpy.SelectLayerByAttribute_management('municipio','NEW_SELECTION', consulta)

#una vez seleccionados los poligonos con mas de 500 habitantes 
#seleccion por interseccion y renovar la seleccion
arcpy.SelectLayerByLocation_management('estaciones', 'INTERSECT', 'municipio', selection_type='NEW_SELECTION')

#contador de elementos seleccionados finales
nes=arcpy.GetCount_management('municipio').getOutput(0) 
print 'Elementos seleccionados', nes

#crear shape de salida en el path generado
arcpy.CopyFeatures_management('municipio', os.path.join(ruta_out,'municipio_5000_estaciones.shp'))

print 'proceso terminado'


