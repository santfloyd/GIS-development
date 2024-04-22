'''
Capas por cada entidad en capa de origen
'''

#importar modulos necesarios
import arcpy
import os

#ambiente de trabajo
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon'

#ruta de salida
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

#shape objetivo
shp="PROVINCIA.shp"

#campo objetivo
campo="NOMBRE"

#lista de campos en el shape
fieldlist=arcpy.ListFields(shp)

#imprimir nombre y tipo
for field in fieldlist:
    print "{} {} {}".format(field.name, ":", field.type)

#crear una capa virtual del shape objetivo
arcpy.MakeFeatureLayer_management(shp, 'provincia')

#crear un cursor para iterar    
searchcursor= arcpy.SearchCursor('provincia')


for row in searchcursor:
    #por cada fila crear una capa virtual nombrada con el valor del campo objetivo y a través de una seleccion por atributo
    #segun el campo objetivo
    #primer parametro nombre de la layer del shape objetivo
    #segundo parametro nombre de layer de salida (valor del campo objetivo)
    #tercero query valor del campo objetivo (hace las veces de id)
    arcpy.MakeFeatureLayer_management('provincia', '{}'.format(row.getValue(campo)),''' "NOMBRE" = '{}' '''.format(row.getValue(campo)))
  
    print "Generando capa para: "
    print row.getValue(campo)
    #crear la ruta con cada valor del campo objetivo
    path = os.path.join(ruta_out, '{}.shp'.format(row.getValue(campo)))
    print path
    #si ya existe terminar, de lo contrario crear una copia
    if arcpy.Exists(path):
        print 'shape existente'
    else:
        arcpy.CopyFeatures_management('{}'.format(row.getValue(campo)), path)
    print "Capa generada"


print 'proceso terminado'
    
    
