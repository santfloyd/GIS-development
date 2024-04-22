import arcpy
arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
try:
    arcpy.Buffer_analysis("Streams", "streams_buffer")
except:
    print arcpy.GetMessages()
    print arcpy.GetMessageCount()

