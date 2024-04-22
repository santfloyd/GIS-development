#importar mapping
import arcpy.mapping
#definir el mapa
mxd=arcpy.mapping.MapDocument("CURRENT")
#mostrar la lista de capas
print arcpy.mapping.ListLayers(mxd)
#mostrar la lista de dataframes
print arcpy.mapping.ListDataFrames(mxd)
#iterar en las capas de dataframes y mostrar sus nombres (sirve solo con la variable df en la loop)
for df in arcpy.mapping.ListDataFrames(mxd):
   print df.name
