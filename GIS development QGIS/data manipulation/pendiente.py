"""
usar herramienta de geoproceso
pendiente de raster
"""

import processing

mde= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\DEM\mde1.asc'
rasterout= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\pendMDE1.tif'

parametros={'INPUT':mde,
            'BAND':1,
            'SCALE':1,
            'AS_PERCENT':False,
            'COMPUTE_EDGES':True,
            'ZEVENBERGEN':True,
            'OUTPUT':rasterout}
#el resultado es otro diccionario
#la clave [output] hace referencia a la capa resultado
resultado= processing.run('gdal:slope',parametros)
#mostrar resultados
iface.addRasterLayer(resultado['OUTPUT'],'PendMde1','gdal')