'''
filtrado kernel 3*3
'''

import arcpy

#ruta del raster landasat
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\LANDSAT'

landsatb5=arcpy.Raster('2018-08-25-LC08-200032-20180825-B5.tif')

kernel=[1,1,1,
        1,1,1,
        1,1,1]

arrayb5=arcpy.RasterToNumPyArray(landsatb5)
arrayb5_copia=arrayb5.copy()

filas=landsatb5.height
columns=landsatb5.width

marco=landsatb5.extent
esquina_ii=arcpy.Point(marco.XMin, marco.YMin)
res_alto= landsatb5.meanCellHeight
res_ancho=landsatb5.meanCellWidth

for f in range(1,filas-1):
    for c in range(1,columns-1):
        #multiplicar cada pixel por cada valor correspondiente en el kernel de 3x3
        #f-1 la fila a la izquierda de la instancia de f, igual c-1 columna a la izquierda de la instancia de c
        #hasta conformar un cuadrado de 3x3
        valor1=arrayb5[f-1,c-1]*kernel[0]
        valor2=arrayb5[f-1,c]*kernel[1]
        valor3=arrayb5[f-1,c+1]*kernel[2]
        valor4=arrayb5[f,c-1]*kernel[3]
        valor5=arrayb5[f,c]*kernel[4]
        valor6=arrayb5[f,c+1]*kernel[5]
        valor7=arrayb5[f+1,c-1]*kernel[6]
        valor8=arrayb5[f+1,c]*kernel[7]
        valor9=arrayb5[f+1,c+1]*kernel[8]
        #calcular la media de todas las multiplicaciones anteriores
        media=(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8+valor9)/9.0
        #asignar el valor medio al pixel central que seria la instancia de f y c
        arrayb5_copia[f,c]=media

raster_filtrado=arcpy.NumPyArrayToRaster(arrayb5_copia, esquina_ii, res_alto, res_ancho)

ruta_out=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts'
raster_filtrado.save(ruta_out+'\\'+'filtro_3x3.tif')


print "proceso terminado"
        
        

