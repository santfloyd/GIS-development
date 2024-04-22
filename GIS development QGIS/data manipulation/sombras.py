"""
usar herramienta de geoproceso
sombras de raster
"""

import processing

mde= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\DEM\mde1.asc'
rasterout= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\sombrasMDE1.tif'

parametros={'INPUT':mde,
            'BAND':1,
            'Z_FACTOR':1,
            'SCALE':1,
            'AZIMUTH':315,
            'ALTITUDE':45,
            'COMPUTE_EDGES':True,
            'ZEVENBERGEN':True,
            'COMBINED':False,
            'MULTIDIRECTIONAL':False,
            'OUTPUT':rasterout}
#el resultado es otro diccionario
#la clave [output] hace referencia a la capa resultado
resultado= processing.run('gdal:hillshade',parametros)
#mostrar resultados
iface.addRasterLayer(resultado['OUTPUT'],'SOMBRASMde1','gdal')