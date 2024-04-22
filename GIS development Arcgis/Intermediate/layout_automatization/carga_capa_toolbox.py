'''
cargar una capa mediante toolbox
'''

import arcpy
import arcpy.mapping as mapp

try:
    #ingreso al mxd actual abierto
    mxd=mapp.MapDocument('CURRENT')
    
    #acceso al primer df
    df=mapp.ListDataFrames(mxd)[0]
    
    #recoge el valor del primer parametro
    ruta_capa=arcpy.GetParameterAsText(0)
    #referencia a la capa como objeto layer
    capa= mapp.Layer(ruta_capa)
    #cargar capa 
    mapp.AddLayer(df, capa)
    #refresco de la lista
    arcpy.RefreshActiveView()
    #refresco de la tabla de contenidos
    arcpy.RefreshTOC()
except:
    message="se ha producido un error catastrofico. Por favor incinere su equipo"
    arcpy.AddMessage(message)