
import arcpy

try:
    arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
    arcpy.MakeFeatureLayer_management("City of Austin - Owned Parcels", "COA_Parcels")
    arcpy.SelectLayerByAttribute_management("COA_Parcels","NEW_SELECTION","PY_FULL_OW='AUSTIN HOUSING AUTHORITY'")
    arcpy.CopyFeatures_management("COA_Parcels","Austin Housing Auth")
except:
    print arcpy.GetMessages(2)

    

