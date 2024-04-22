
'''

'''

#modulos necesarios
import arcpy
import os
from arcpy import HillShade_3d
import matplotlib.pyplot as plt

#indicar el directorio de trabajo y el raster de entrada
arcpy.env.workspace=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts'
raster_in='TIN_ToMDE.tif'

#especificar la ruta de salida para cada uno de las capas raster necesarias para el desarrollo de la practica
ruta_out=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"
raster_sombras1_out= os.path.join(ruta_out,'sombras1.tif')
raster_sombras2_out= os.path.join(ruta_out,'sombras2.tif')
raster_sombreado_combinado= os.path.join(ruta_out,'sombreado_combinado.tif')
raster_sombreado_combi_dataset= os.path.join(ruta_out,'sombreado_combi_dataset.tif')

"______________________________________________________________FUNCIONES_________________________________________________________________________"

#funcion para procesar el MDE y producir una capa de sombras con los parametros indicados por el usuario
def Sombras(raster_in, raster_out, azimuth, elevation, shadow_model=True):
    HillShade_3d(raster_in, raster_out, azimuth, elevation, shadow_model)

#funcion para producir la capa de sombras combinada
def Sombreado_Combinado(sombras1, sombras2):
        sombras1_raster=arcpy.Raster(sombras1)
        sombras2_raster=arcpy.Raster(sombras2)
        #valores minimo y maximo de las capas de sombra de entrada
        min_raster=sombras1_raster.minimum
        max_raster=sombras2_raster.maximum
        print("valores minimos y maximos raster de entrada:",min_raster, max_raster)
        
        #suma de las dos capas de sombras
        sombras3=sombras1_raster+sombras2_raster
        min_sombras3 = sombras3.minimum
        max_sombras3 = sombras3.maximum
        print("valores minimos y maximos de la suma de rasters de entrada:",min_sombras3, max_sombras3)
        
        #calculo del desplazamiento de la sumatoria de capas
        desplazamiento=sombras3-min_sombras3
        min_desplazamiento = desplazamiento.minimum
        max_desplazamiento = desplazamiento.maximum
        print("valores minimos y maximos de desplazamiento:",min_desplazamiento, max_desplazamiento)
        
        #escalado de la capa desplazada para ajustar al rango de una capa de 8 bits (0-254)
        sombreado_combinado=desplazamiento*max_raster/(max_desplazamiento-min_desplazamiento)
        print("valores minimos y maximos raster combinado:",sombreado_combinado.minimum, sombreado_combinado.maximum)
        
        sombreado_combinado.save(raster_sombreado_combinado)
        #se realiza una copia de la capa escalada indicando el tipo de pixel de 8 bits. Matplotlib ahora es capaz de representarlo
        arcpy.CopyRaster_management('sombreado_combinado.tif','sombreado_combi_dataset.tif', format="TIFF", pixel_type="8_BIT_UNSIGNED")

#funcion para convertir las capas de sombras a arrays y poder ser representados con Matplotlib    
def Raster_ToArray(raster1,raster2, raster3):
    sombra_oblicua1=raster1
    sombra_oblicua2=raster2
    sombra_cenital=raster3
    sombra_oblicua1_array=arcpy.RasterToNumPyArray(sombra_oblicua1)
    sombra_oblicua2_array=arcpy.RasterToNumPyArray(sombra_oblicua2)
    sombra_cenital_array=arcpy.RasterToNumPyArray(sombra_cenital)
    return sombra_oblicua1_array, sombra_oblicua2_array, sombra_cenital_array

#funcion para graficar las tres capas de salida de la practica
def Plot_Sombras(sombras1,sombras2,sombras_combi):
    plt.subplot(1,3,1)
    plt.imshow(sombras1,cmap="gray")
    plt.title("Sombras Azi=315, Ele=45")
    plt.axis('off')
    plt.subplot(1,3,2)
    plt.imshow(sombras2,cmap="gray")
    plt.title("Sombras Azi=45, Ele=30")
    plt.axis('off')
    plt.subplot(1,3,3)
    plt.imshow(sombras_combi,cmap="gray")
    plt.title("Sombras combinado")
    plt.axis('off')
    plt.show()
"__________________________________________________Calculo y grafica de sombreado combinado   ___________________________________________________"    
#bloque try-except para captura de errores en caso de que las capas ya existan
try:
    #chequeo de extension 3D
    if arcpy.CheckExtension('3D') == 'Available':
        arcpy.CheckOutExtension('3D')
        
        #llama a la funcion Sombras para producir las capas de sombras
        Sombras(raster_in,raster_sombras1_out,315,45)
        Sombras(raster_in,raster_sombras2_out,45,30)
        
        
        arcpy.CheckInExtension('Spatial')
        
            
    else:
        print 'licencia no disponible'
        
    #llama a las funciones para calculo de sombreado combinado, conversion a arrays y, finalmente, grafico de las tres capas
    sombras_combinado= Sombreado_Combinado(raster_sombras1_out, raster_sombras2_out)
    
    sombra_oblicua1_array, sombra_oblicua2_array, sombra_cenital_array= Raster_ToArray(raster_sombras1_out,raster_sombras2_out,raster_sombreado_combi_dataset)
    
    Plot_Sombras(sombra_oblicua1_array, sombra_oblicua2_array,sombra_cenital_array)

#si se produce error en el bloque try, ejecuta el bloque except
except:
    #si la capa de sombreado combinado ya existe, muestra en pantalla que ya existe o de lo contrario lo calcula (suponiendo que las capas de sombras
    #individuales ya existen porque se generaron en otro proyecto o porque se ejecuto parcialmente el bloque try
    if arcpy.Exists(raster_sombreado_combinado):
        print 'raster existente'
    else:
        sombras_combinado= Sombreado_Combinado(raster_sombras1_out, raster_sombras2_out)
    
    #llama funciones de conversion de raster a array y graficacion de las capas
        
    sombra_oblicua1_array, sombra_oblicua2_array, sombra_cenital_array= Raster_ToArray(raster_sombras1_out,raster_sombras2_out,raster_sombreado_combi_dataset)
    
    Plot_Sombras(sombra_oblicua1_array, sombra_oblicua2_array,sombra_cenital_array)
    
print 'proceso terminado'