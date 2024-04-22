'''
Created on 24/02/2021

@author: Usuario
'''
#este codigo será la source de una toolbox
import arcpy

#recoger el parametro como texto
valor= arcpy.GetParameterAsText(0) #posicion del parametro en la toolbox en arcmap 

arcpy.AddMessage(valor)
mxd=map.MapDocument('CURRENT') #'CURRENT' -> EJECUTAR DESDE EL PROYECTO EN LA VENTANA DE ARCMAP
    #acceso al primer df
df0=map.ListDataFrames(mxd)[0] #primer df
capas=map.ListLayers(mxd, '', df0)


for capa in capas:
    if capa.visible:
        capa.visible = False
    else:
        capa.visible = True
        
        
        

#refrescar
arcpy.RefreshActiveView()