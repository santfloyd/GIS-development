# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 12:41:22 2018

@author: ASUS
"""

import arcpy

#La variable ‘output_graph_name’ define el nombre del gráfico salida de la tool SaveGraph tool. 
output_graph_name= 'Vertical_Bar_Graph'
#La variable ‘verticalBarGraph_bmp’ almacena el nombre del fichero salida que contiene el grafico
verticalBarGraph_bmp= r'C:\GeoSpatialTraining\PythonII\Exercises\verticalBarGraph.bmp'
#La variable ‘inputTemplate’define el nombre del template
inputTemplate=r'C:\GeoSpatialTraining\PythonII\Exercises\myGraph.tee'
#la variable ‘inputData’ define la feature class que se usa como fuente de datos del gráfico
inputData=r'C:\GeoSpatialTraining\ArcGIS10\GISProgramming101\Exercises\Data\New_Data\CityOfSanAntonio.gdb\CrimesBySchoolDistrict'

#create graph
graph=arcpy.Graph()
#add vertical bars to the grpah
graph.addSeriesBarVertical(inputData,'CrimeDens')
#Specify the title of the left axis
graph.graphAxis[0]='Crime Density'
#specify the title of the bottom axis
graph.graphAxis[2]='Name'
#specify the title of the graph
graph.graphPropsGeneral.title='Crime Density by school district'
#output graph created in-memory pasándole el template, el objeto graph de memoria y el nombre del gráfico
arcpy.MakeGraph_management(inputTemplate, graph, output_graph_name)
#save graph as an image  pasándole el nombre del gráfico de salida, el nombre del fichero del gráfico de barras y los parámetros que definen las propiedades de la salida
arcpy.SaveGraph_management(output_graph_name, verticalBarGraph_bmp, 'MAINTAIN_ASPECT_RATIO', '600', '375')
print 'graph saved'

