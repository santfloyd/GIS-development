
import arcpy

#Permito sobreescribir ficheros
arcpy.env.overwriteOutput = True

#Establezco la variable de entrada del fichero JSON
infile = arcpy.GetParameterAsText(0)
outpath = arcpy.GetParameterAsText(1)
outname = arcpy.GetParameterAsText(2)

#Abro el fichero txt con estructura GeoJSON para utilizarlo y lo leo para crear un objeto GeoJSON
f = open(infile)
myGeoJSON = f.read()




    #Convierto el objeto GeoJSON a un objeto geometry de ArcPy
polygon = arcpy.AsShape(myGeoJSON)
    #Exporto el objeto geometría para salvarlo
arcpy.FeatureClassToFeatureClass_conversion(polygon,outpath,outname)




print arcpy.GetMessage(2)

    
#Cierro fichero de texto y elimno variables
del polygon
f.close()