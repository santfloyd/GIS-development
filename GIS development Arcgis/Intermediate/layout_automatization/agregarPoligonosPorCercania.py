'''
Combinacion de poligonos a partir de su cercania
'''

import arcpy
import arcpy.mapping as mapp
import os



#ingreso al mxd actual abierto
mxd=mapp.MapDocument('CURRENT')

#valores de los parametros
capa_entrada=arcpy.GetParameterAsText(0)
capa_salida=arcpy.GetParameterAsText(1)
distancia=arcpy.GetParameter(2)
tolerance=arcpy.GetParameter(3)

#generacion de una capa intermedia
#capa_intermedia=os.path.dirname(capa_entrada)+'\\capa_intermedia.shp'
#arcpy.AddMessage(capa_intermedia)
#otra posibilidad es trabajar la intermedia en memoria
capa_intermedia='in_memory' #capa en memoria
#primer buffer
arcpy.Buffer_analysis(capa_entrada, capa_intermedia,distancia,dissolve_option='ALL')

#segundo buffer con distancia negativa para simplificar el buffer
arcpy.Buffer_analysis(capa_intermedia, capa_salida,distancia*(-0.9))
#generalizar
arcpy.Generalize_edit(capa_salida,tolerance)
#eliminar la capa intermedia
#arcpy.Delete_management(capa_intermedia)

#carga la capa
df=mapp.ListDataFrames(mxd)[0]
capa= mapp.Layer(capa_salida)
mapp.AddLayer(df, capa)
#refresco de la lista
arcpy.RefreshActiveView()
#refresco de la tabla de contenidos
arcpy.RefreshTOC()