'''
ejemplo de acceso a las capas
'''

#import

import arcpy
import arcpy.mapping as map


#ruta proyecto

ruta_mxd=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo de aplicaciones SIG\proyectos\proyecto1.mxd"

#definicion de funciones

def imprime_propiedades(capa):
    print 'Nombre:', capa.name
    print 'ruta:', capa.dataSource
    if capa.isFeatureLayer: 
        print 'Tipo vectorial'
    if capa.isRasterLayer:
        print 'Tipo raster'
    if capa.visible:
        'Estado visible'
    else:
        'Estado no visible'
    marco=capa.getExtent()
    print 'Limites', marco.XMin, marco.YMin, marco.XMax, marco.YMax
    print ''

#validez ruta

if not arcpy.Exists(ruta_mxd):
    print 'Ruta no valida'
else:
    #acceso al proyecto
    mxd=map.MapDocument(ruta_mxd) #'CURRENT' -> EJECUTAR DESDE EL PROYECTO EN LA VENTANA DE ARCMAP
    #acceso al primer df
    df0=map.ListDataFrames(mxd)[0] #primer df
    capas=map.ListLayers(mxd, '', df0)
    for capa in capas:
        imprime_propiedades(capa)
    
