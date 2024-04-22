'''
ejecicicos practicos fichero con info de capas
'''


#acceso al proyecto
proyecto=QgsProject.instance()

#referencia a las capas del proyecto
capas=proyecto.mapLayers()

#listas con nombre, ruta, tipo y extent de cada capa cargada en el proyecto
nom_capas=[capa.name() for capa in capas.values()]
ruta_capas=[capa.source() for capa in capas.values()]
type_capas=['vectorial' if capa.type()== QgsMapLayer.VectorLayer else 'raster' for capa in capas.values() ]
extent_capas=[capa.extent() for capa in capas.values()]

print(nom_capas)
print(ruta_capas)
print(extent_capas)
print(type_capas)

#funcion para escribir el informe
def imprimeFila(datos):
    datos_string=''
    for n, r, t, e in datos:
        datos_string+="""
                {nombre}   {ruta}     {type}     {extent}\n""".format(nombre=n, ruta=r, type=t, extent=e)
    return datos_string


#escribir en un archivo de texto segun la salida grafica solicitada
with open(r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\informe_ejercicio_practico_semana6.txt","w") as file:
    
    guiones=50*'*'
    
    #string entre comillas triples permite strings en varias lineas
    informacion="""
                informacion de capas en el proyecto
                {guiones}
                Nombre    ruta      tipo 0=vectorial     extent
                """.format(guiones=guiones)
                
    file.write(informacion)
     
    #agrupa en tuplas las listas de datos           
    datos=zip(nom_capas, ruta_capas, type_capas, extent_capas)
    
    file.write(imprimeFila(datos))       
               
    print('Escritura terminada')