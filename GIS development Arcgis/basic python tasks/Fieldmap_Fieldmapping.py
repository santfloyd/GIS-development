

import arcpy
from arcpy import env

#Variables inputs and output primero se establen el folder de entrada y el archivo de salida

arcpy.env.workspace = "C:\GeoSpatialTraining\PythonII"
outputFeature= "CountyMerge.shp"

#Crear Lista de features segundo se crea una lista de todas las entidades en ese folder de entrada

listaFeature = arcpy.ListFeatureClasses()
print listaFeature
#Crear tres field maps objects y un field mapping que los contenga tercero se crean los objetos fieldmap, uno por cada campo a crear y un objeto fieldmapping que los almacenará a todos los objetos fieldmap

fieldMap_STFIPS = arcpy.FieldMap()
fieldMap_COFIPS = arcpy.FieldMap()
fieldMap_TRACT = arcpy.FieldMap()
fieldmappings = arcpy.FieldMappings()

#Crear una value table que aloje los valores de las capas de entrada para la herramienta Merge cuerto se crea una tabla para luego almacenar ahí todos los valores fieldmap

valueTable = arcpy.ValueTable()

#Ejecuta la accion dentro de una lista si la capa comienza por County
for feature in listaFeature:            # loop para separar cada capa dentro de la lista de capas dentro del folder
    if feature.startswith("County"):   #selección de la capa si comienza por
        fieldmappings.addTable(feature) #añade cada capa a la coleccion de objetos fieldmap (tablas)
        fieldMap_STFIPS.addInputField(feature, "STFID",0,1)  #(table_dataset, field_name, {start_position}, {end_position} 
        fieldMap_COFIPS.addInputField(feature,"STFID",2,4)   #a cada objeto fieldmap creado antes se le indica que extraiga los datos de cada elemento en la lista de capas
        fieldMap_TRACT.addInputField(feature,"STFID",5,10)  #del campo entre comillas, desde la posición indicada hasta la posición indicada
        valueTable.addRow(feature)          #añade a la tabla creada antes fila a fila los valores de cada capa, entonces esta linea conserva las tablas 
                                            #originales en una sola tabla a la que se le sumaran los fieldmap con valores extraídos antes
field_STFIPS = fieldMap_STFIPS.outputField   #The properties of the output field are either set or returned in a Field object. property of fieldmap
field_STFIPS.name = "STFIPS"                 #se le da nombre al objeto fieldmap
fieldMap_STFIPS.outputField = field_STFIPS

field_COFIPS = fieldMap_COFIPS.outputField   #a una variable nueva se le indica que el output del fieldmap será un campo 
field_COFIPS.name = "COFIPS"                 #se le da nombre al campo que recibirá al objeto fieldmap
fieldMap_COFIPS.outputField = field_COFIPS   #se le indica al output del field map que será el campo con nombre

field_TRACT = fieldMap_TRACT.outputField
field_TRACT.name = "TRACT"
fieldMap_TRACT.outputField = field_TRACT


#Añadir el nuevo fieldmap object a fieldmappings object

fieldmappings.addFieldMap (fieldMap_STFIPS)  #añade los objetos fieldmap a la colección obejto fieldmapping
fieldmappings.addFieldMap (fieldMap_COFIPS)
fieldmappings.addFieldMap (fieldMap_TRACT)


#Run Merge Tool finalmente hace el merge

arcpy.Merge_management(valueTable, outputFeature, fieldmappings) #el ultimo argumento son los campos a transferir tras ser mapeados.


            














