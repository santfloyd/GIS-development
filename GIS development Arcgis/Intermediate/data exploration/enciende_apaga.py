'''
apaga o enciende las capas 
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
    if valor == 'Encender':
        capa.visible = True
    else:
        capa.visible = False
#refrescar
arcpy.RefreshActiveView()
