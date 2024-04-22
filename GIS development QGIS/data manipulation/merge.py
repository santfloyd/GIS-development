"""
usar herramienta de geoproceso
unir dos capas vectoriales
"""

import processing

shp1= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\CARRETERA.SHP'
shp2= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\FERROCARRIL.SHP'

shpout= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\car_fer.shp'

parametros={'LAYERS':[shp1,shp2],
            'CRS':shp1,
            'OUTPUT':shpout}
#el resultado es otro diccionario
#la clave [output] hace referencia a la capa resultado
resultado= processing.run('native:mergevectorlayers',parametros)
#mostrar resultados
iface.addVectorLayer(resultado['OUTPUT'],'CAR_FER','ogr')