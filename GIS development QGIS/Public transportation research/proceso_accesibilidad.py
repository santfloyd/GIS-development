#-*- coding: utf-8 -*-

#__________************************************_________________
#Paso 1
#CARGA DE SHAPES A POSTGRES

#Es necesario añadir el path donde se encuentran
#los scripts para la ejecución
sys.path.append('E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\entrega3\proyecto_DSIG')

#importar la clase con el atributo para insertar a Postgres y otras
#que se usaran más adelante
import pgUtils

#instalar la extension postgis
#pgUtils.pgPostgis()

#path de la carpeta con toda la cartografia
path_dir="E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\entrega3\cartografia"
pgUtils.insert_shapes(path_dir)

#________________*******************************________________
#Paso 2
#CARGA DE TABLAS POSTGRES A QGIS 
import ingestaPGIS2QGIS as pq

#llamar la clase con funciones para carga de capas a QGIS
o1=pq.pgisQgis()

#llama al método para recuperar el nombre de las tablas en la BBDD
noms=o1.tableNames() 
print(noms)

#cargar tablas a QGIS
for nom in noms:
    #parametros: nombre de tabla, sistema de coordenadas, esquema
    print(o1.pgQgis(nom)) #la funcion recibe el nombre del esquema, en caso de ninguna por defecto busca en 'public'


#______**************************__________________________    
#funciones

 


#___________________*********************************________________
#Procesamiento

#desde pgUtils se usa la funcion de seleccion
#print(pgUtils.selectFromTable("upla_proj"))

#desde pgUtils se usa la funcion de union y sacar el nombre de las tablas
#para verificar
#los parametros son tabla_nueva,tabla1,campo1,tabla2,campo2,database por defecto None y recoge la que se defina en settings
print(pgUtils.joinByAttri("upz_censo","upla_proj","uplcodigo","informacion_demografica","upz"))
print(pgUtils.areaCalc("upz_censo","area_mcuadrados"))
#carga de la nueva capa
print(o1.pgQgis("upz_censo"))

#calculo de poblacion estimada por cada ZAT según la población
#en cada UPZ resultante del join anterior
#parametros: tabla1, tabla2, nueva tabla, campo de interes, database (por defecto PROJDSIG)
print(pgUtils.sumaProporcional("zat_actualizada_geomcorreg","upz_censo","zat_censo","personas"))
#carga de la nueva capa
print(o1.pgQgis("zat_censo"))

#intalar extension pgRouting en la BBDD
#pgUtils.pgRoutingextension()

#generar la topologia de red con el tramero
#acepta nombre capa tramero, nombre campo sentido de via, BBDD por defecto PROJDSIG
pgUtils.topologiaRed("malla_vial","mvisvia")

#enriquecer la tabla de malla vial con camposde longitud, máxima velocidad de tránsito y costo temporal
#de tránsito por cada tramo lineal
pgUtils.lineMeassure("malla_vial")

#generar indice espacial
pgUtils.indexEspacial("malla_vial")
#print(o1.pgQgis("malla_vial"))

#claculo de recorrido a travez de la geomteria vial
#con un rango de 400 mts
#parametros capa de calles, capa de puntos de paraderos, capa de salida
pgUtils.areaServicio("malla_vial","paraderos_sitp_bogota_d_c_proj","areas_servicio_line")
print(o1.pgQgis("areas_servicio_line"))

#creación de poligonos a partir de los extremos de cada recorrrido a travez de la geometria de calles
#paramteros capa lineal de areas de servicio y capa de salida
pgUtils.poly_areaServicio("areas_servicio_line","areas_servicio")
print(o1.pgQgis("areas_servicio"))

#calcular un buffer circular al rededor de cada paradero 
pgUtils.buffer("areas_servicio_line","paraderos_sitp_bogota_d_c_proj","buffer_paraderos")

#extraccion de los tramos lineles que cada buffer comprende
pgUtils.buffer_intersect("malla_vial","buffer_paraderos","ntrcodigo","interseccion_buffer_malla")
print(o1.pgQgis("interseccion_buffer_malla"))
#calculo de indicadores finales
pgUtils.indicadores("interseccion_buffer_malla","upz_censo","paraderos_sitp_bogota_d_c_proj", "buffer_paraderos","areas_servicio_line","areas_servicio","gid","paraderos_indicadores")
print(o1.pgQgis("paraderos_indicadores"))