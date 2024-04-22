#importar mapping
import arcpy.mapping
#definir el mapa
mxd=arcpy.mapping.MapDocument("CURRENT")
#iterar en lista de capas y mostrar sus nombres
for lyr in arcpy.mapping.ListLayers(mxd):
    print lyr.name
#mostrar la lista de dataframes
print arcpy.mapping.ListDataFrames(mxd)
#iterar en las capas de dataframes y mostrar sus nombres (sirve solo con la variable df en la loop)
for df in arcpy.mapping.ListDataFrames(mxd):
   print df.name
#referenciar un proyecto con path
mxd1=arcpy.mapping.MapDocument("C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Crime.mxd")
#definir como df la capa en la primera posoción [0] del proyecto mxd1 en el layer group "Inset_map" 
df=arcpy.mapping.ListDataFrames(mxd1, "Inset_map")[0]
# muestra el nombre de la primera capa del proyecto mxd1, primer parametro, sin wildcard, segundo parametro, del dataframe df. ultimo parametro de la funcion listlayers 
#y primera posición de la lista df y el método name
print arcpy.mapping.ListLayers(mxd1, "", df) [0].name

