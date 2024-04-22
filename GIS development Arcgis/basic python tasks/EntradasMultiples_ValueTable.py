# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:24:42 2018

@author: ASUS
"""

import arcpy

#variables
infeature="C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\Hospitals.shp"
outfeatureclass="C:\GeoSpatialTraining\PythonII\HospitalsBuffer.shp"
vt=arcpy.ValueTable()
bufferunit="meters"
#valores de la value table de esta manera es que funciona una columna y se le añaden valores
#si se quisieran añadir valores en tres columnas tendria que arriba estar el 3 al crear la tabla
#e iria asi vt.addRow("'10' '20' '30'")
vt.addRow(10)
vt.addRow(20)
vt.addRow(30)


#herramienta
arcpy.MultipleRingBuffer_analysis(infeature, outfeatureclass, vt, bufferunit, "", "ALL")
print "DONE"