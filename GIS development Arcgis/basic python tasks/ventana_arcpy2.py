import arcpy
arcpy.env.workspace="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data"
arcpy.Buffer_analysis("Streams", "Streams_Buffer_11022018", "1000 Feet", "FULL", "ROUND", "ALL", "") 
arcpy.Buffer_analysis("Streams", "Streams_Buffer_11022018_2", "1000 Meters", "FULL", "ROUND", "ALL", "")
