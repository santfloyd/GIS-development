'''
seleccion por atributo

1. crear una capa virtual (makeFeatureLayer)
2. crear una consulta de tipo SQL
3. aplicar la seleccion
4. contar elementos seleccionados
5. guardar la seleccion en un nuevo shp
6. mejora para evitar el problema de existencia del archivo de salida
 
'''
import arcpy




ruta_shp=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\provincia.shp'

ruta_out='E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\leon.shp'

if arcpy.Exists(ruta_out):
    arcpy.Delete_management(ruta_out)
#crear capa virtual
arcpy.MakeFeatureLayer_management(ruta_shp,'prov')

#query
consulta=''' "NOMBRE" = 'LEON' ''' #NOMBRE DE CAMPO EN COMILLAS DOBLES, VALROES EN COMILLA SIMPLE, TODO EN COMILLA TRIPLE

arcpy.SelectLayerByAttribute_management('prov', 'NEW_SELECTION', consulta)

nes=arcpy.GetCount_management('prov').getOutput(0) #cuenta el numero de elementos y cuando hay seleccion da esa cuenta

print 'Elementos seleccionados', nes

arcpy.CopyFeatures_management('prov', ruta_out)

print 'proceso terminado'



