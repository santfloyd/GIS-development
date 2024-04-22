
import arcpy, os

featureClass = "C:/GeoSpatialTraining/ArcGIS10/GISProgramming101/Exercises/Data/Schools.shp"
workspace = os.path.dirname(featureClass)


#Comienza sesion de edicion
edit = arcpy.da.Editor(workspace)

#Activamos la edicion
edit.startEditing(False)

#Comienza la operación
edit.startOperation()

with arcpy.da.UpdateCursor(featureClass,("FACILITY", "VERIFIED"), where_clause="FACILITY = 'HIGH SCHOOL'") as cursor:
    for row in cursor:
        row[1]= '(='
        cursor.updateRow(row)
    print "update complete"
    
#Paramos la sesion de edicion

edit.stopOperation()

#Cerramos Sesion

edit.stopEditing(True)


