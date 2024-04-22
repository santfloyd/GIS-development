#Santiago Ortiz
#11/02/2018
#EJERCICIO CONTROL DE ERRORES
import arcpy

try:
    arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
    #generar una capa temporal
    arcpy.MakeFeatureLayer_management("City of Austin - Owned Parcels", "City of Austin_Austin Housing Auth", )
    #seleccionar registros
    arcpy.


