# -*- coding: utf-8 -*-
'''
filtrado kernel 5*5
'''

import arcpy
import numpy as np

#ruta del raster landasat
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\LANDSAT'

landsatb5=arcpy.Raster('2018-08-25-LC08-200032-20180825-B5.tif')

kernel=np.array([[1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]])

arrayb5=arcpy.RasterToNumPyArray(landsatb5,nodata_to_value=0)
arrayb5_copia=arrayb5.copy()

filas=landsatb5.height
columns=landsatb5.width
print(filas, columns)

marco=landsatb5.extent
esquina_ii=arcpy.Point(marco.XMin, marco.YMin)
res_alto= landsatb5.meanCellHeight
res_ancho=landsatb5.meanCellWidth

#por cada fila y por cada columna restando el tamaño del kernel para la posicion final de f y c (deja un espacio de 5x5 al final del raster)
for f in range(filas-5):
    for c in range(columns-5):
        print(arrayb5[f:f+5, c:c+5])
        #en la variable valor se almacena la suma de todos los valores resultantes de la
        #multiplicacion de una ventana igual al tamaño del kernel 5x5
        valor=(arrayb5[f:f+5, c:c+5]*kernel).sum()
        media=valor/25.0
        arrayb5_copia[f,c]=media
print(arrayb5_copia)

raster_filtrado=arcpy.NumPyArrayToRaster(arrayb5_copia, esquina_ii, res_alto, res_ancho)

ruta_out=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts'
raster_filtrado.save(ruta_out+'\\'+'filtro_5x5.tif')


print "proceso terminado"

