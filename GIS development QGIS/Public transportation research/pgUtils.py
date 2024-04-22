'''
Clase para formalizar la conexion con la base de datos
'''

#importa la clase Settings del modulo mySettings
#necesario para llamar los atributos de la clase que a su vez son los parametros de conexion
from mySettings import Settings
settings=Settings()
#importar el modulo propio 
import ingestaPGIS2QGIS as pq


#importar los modulos necesarios para establecer la conexion y manejar las geometrias sin problemas
from PyQt5.QtSql import *
from qgis.core import QgsVectorLayer, QgsDataSourceUri
from sqlalchemy import *
from geoalchemy2 import *
import geopandas as gpd
import os
import processing

#instalar la extension postgis en la BBDD para soportar geometrias    
def pgPostgis(database=None):
    connection=pgConnect(database)
    install_ext="""CREATE EXTENSION postgis;"""
    connection.execute(install_ext)
    if database == None:
        print("se instaló la extensión postgis en {database}".format(database=Settings.database))
    else:
        print("se instaló la extensión postgis en {database}".format(database=database))

#funcion para insertar capas vectoriales en la BBDD postgres
def insert_shapes(path_shapes,schema="public",database=None):
    """
    conecta a la base de datos especificada en mySettings o a la indicada por el usuario
    """
    #lista de archivos dentro del directorio objetivo
    for file in os.listdir(path_shapes):
        #si termina con la extensión .shp
        if file.endswith(".shp"):
            #reconforma el path del shape para ser leído por geopandas
            shape_path=os.path.join(path_shapes,file)
            #extrae solo el nombre del shape para nombrar la tabla en postgres
            name=os.path.splitext(os.path.basename(shape_path))[0]
            
            if database==None:
                #crear el objeto settings que cree en la clase setings en mysettings.py
                settings=Settings()
                #cadena para abrir conección con los parámetros por defecto almacenados en el objeto settings
                engine = create_engine("postgresql+psycopg2://{usr}:{pwd}@{host}:{port}/{db}".format(usr=settings.user,pwd=settings.password,host=settings.host,port=settings.port,db=settings.database))
                #lectura del shape
                gdf = gpd.read_file(shape_path)
                #carga de shapes a la base de datos, si ya existe la reemplaza
                gdf.to_postgis(name, engine,if_exists="replace",schema=schema)
                
            else:
                #en caso que se estipule una base de datos diferente, se modifica el atributo database del obejto settings
                settings=Settings(database)
                engine = create_engine("postgresql+psycopg2://{usr}:{pwd}@{host}:{port}/{db}".format(usr=settings.user,pwd=settings.password,host=settings.host,port=settings.port,db=settings.database))
                gdf = gpd.read_file(shape_path)
                gdf.to_postgis(name, engine,if_exists="replace",schema=schema)
       
            mensaje="Se ha insertado la tabla {table} con éxito".format(table=name)
            print(mensaje)
    mensaje_final="proceso terminado"
    return mensaje_final

#funcion para estabñecer conexion directa con una base de datos
#admite un parametro si no se le pasa abre la conexion con los valores por defecto
#en el modulo Settings
def pgConnect(database=None):
    """
    conecta a la base de datos especificada en mySettings o a la indicada por el usuario
    """
    #conexion con valores por defecto
    if database ==None:
        
        #crear el objeto settings que cree en la calse setings en mysettings.py
        settings=Settings()
        #conexion
        engine = create_engine("postgresql+psycopg2://{usr}:{pwd}@{host}:{port}/{db}".format(usr=settings.user,pwd=settings.password,host=settings.host,port=settings.port,db=settings.database))
        #conecta
        connection= engine.connect()
    #si se le pasa otra base de datos abre la conexion con esa base de datos
    else:
        settings=Settings(database)
        engine = create_engine("postgresql+psycopg2://{usr}:{pwd}@{host}:{port}/{db}".format(usr=settings.user,pwd=settings.password,host=settings.host,port=settings.port,db=settings.database))
        connection= engine.connect()
    #devuelve la conexion
    return connection

#funcion para componer uri de una capa vectorial
def uri_con(layer, schema='public'):
    settings=Settings()
    #nombre de la columna con geometría en las tablas
    geometrycol = "geometry"
    #fuente de las capas de entrada
    uri = QgsDataSourceUri()
    uri.setConnection(settings.host, settings.port, settings.database, settings.user, settings.password)
    #si la capa termina con _proj tiene geometria
    uri.setDataSource (schema, layer, geometrycol)
    return uri.uri()
    print(uri.uri())

    
#funcion de selccion
def selectFromTable(table, database=None):
    #usa la funcion de conexion
    connection=pgConnect(database)
    query_sql="""SELECT * FROM {table}""".format(table=table)
    selection = connection.execute(query_sql).fetchall()
    return selection
    
#funcion de union
def joinByAttri(tabla_nueva,tabla1,campo1,tabla2,campo2,database=None):
    #usa la funcion de conexion
    connection=pgConnect(database)
    query_sql_join="""CREATE TABLE {tabla_nueva} AS SELECT {tabla1}.*, {tabla2}.* FROM {tabla1} LEFT JOIN {tabla2} ON {tabla2}.{campo_tabla2} = {tabla1}.{campo_tabla1}""".format(tabla_nueva=tabla_nueva,tabla1=tabla1,tabla2=tabla2,campo_tabla1=campo1,campo_tabla2=campo2)
    connection.execute(query_sql_join)
    #o1=pq.pgisQgis()
    #noms=o1.tableNames() 
    #print(noms)
    #return noms
    
#funcion calcular rutas
def areaCalc(tabla,new_field,database=None):
    connection=pgConnect(database)
    query_sql="""ALTER TABLE {tabla} ADD COLUMN {new_field} NUMERIC;
                UPDATE {tabla} SET {new_field}=st_area(geometry);""".format(tabla=tabla,new_field=new_field)
    connection.execute(query_sql)
    print("se calculó área en el campo {new_field} en la tabla {tabla}".format(tabla=tabla,new_field=new_field))

#funcion poblacion aproximada segun proporcion espacial entre 
#area de dos capas poligonales 
def sumaProporcional(tabla1, tabla2, new_table, campo_pob, database=None):
    connection=pgConnect(database)
    sql_function="""CREATE OR REPLACE FUNCTION public.proportional_sum(geometry, geometry, numeric) RETURNS numeric AS $BODY$
                    SELECT $3 * areacalc FROM (
                    SELECT (ST_Area(ST_Intersection($1, $2))/ST_Area($2))::numeric AS areacalc) AS areac; 
                    $BODY$
                    LANGUAGE sql VOLATILE;"""
    
    query_sql="""CREATE TABLE {new_table} AS SELECT a.zatcod, a.geometry, ROUND(SUM(public.proportional_sum(a.geometry, b.geometry, b.{campo_pob}))) AS poblacion_proporcional FROM
                public.{tabla1} AS a, public.{tabla2} as b WHERE ST_Intersects(a.geometry, b.geometry) GROUP BY a.fid, a.zatcod, a.geometry;""".format(new_table=new_table,tabla1=tabla1,tabla2=tabla2,campo_pob=campo_pob)
    connection.execute(sql_function)
    connection.execute(query_sql)
    print("se calculó población aproximada en la tabla {new_table}".format(new_table=new_table))

#crear extension pgrouting en la BBDD
def pgRoutingextension(database=None):
    connection=pgConnect(database)
    install_ext="""CREATE EXTENSION pgrouting;"""
    connection.execute(install_ext)
    if database == None:
        print("se instaló la extensión pgRouting en {database}".format(database=Settings.database))
    else:
        print("se instaló la extensión pgRouting en {database}".format(database=database))


#funcion para generar topologia de la red
#a partir de la malla vial de la ciudad
#recibe nombre de la capa con tramero, nombre de campo con tramos en una sola direcion y nombre de BBDD
def topologiaRed(tablavial,campo_oneway,database=None):
    """
    Construir la topología que es básicamente construir la red conectando 
    los nodos únicos a través de los vínculos (calles)
    """
    connection=pgConnect(database)
    query_fields="""ALTER TABLE public.{tablavial} ADD COLUMN source integer;
                    ALTER TABLE public.{tablavial} ADD COLUMN target integer;""".format(tablavial=tablavial)
    #parametros topologia nombre de la capa, tolerancia, columna de geometria, índice espacial
    query_topo="""SELECT pgr_createTopology('{tablavial}',0.001,'geometry','gid')""".format(tablavial=tablavial)
    query_linestring="""ALTER TABLE {tablavial}
                        ALTER COLUMN geometry TYPE geometry(linestring,3116) USING ST_GeometryN(geometry, 1);""".format(tablavial=tablavial) #convertir multigeometria a geometrya simple
    query_analyze_topo="""SELECT pgr_analyzeGraph('{tablavial}',0.000002,'geometry','gid')""".format(tablavial=tablavial) #solo funciona si la geometria es linestringno multilinestring
    query_analyze_oneway="""SELECT pgr_analyzeOneway('{tablavial}', 
                            ARRAY['','B','TF'],
                            ARRAY['', 'B', 'FT'], 
                            ARRAY['', 'B', 'FT'], 
                            ARRAY['', 'B', 'TF'], 
                            oneway:='{campo_oneway}');""".format(tablavial=tablavial,campo_oneway=campo_oneway)
    connection.execute(query_fields)
    connection.execute(query_topo)
    connection.execute(query_linestring)
    connection.execute(query_analyze_topo)
    connection.execute(query_analyze_oneway)
    print("se ha generado la topologia de red y análisis de topología en {tablavial}".format(tablavial=tablavial))

def lineMeassure(tablavial, database=None):
    """
    Enriquecer la tabla de trameros urbanos con 
    campos como longitud, costo y velocidad de transeunte promedio
    """
    connection=pgConnect(database)
    query_length="""ALTER TABLE public.{tablavial} ADD COLUMN length double precision;
                    UPDATE public.{tablavial} SET length=st_length(geometry);""".format(tablavial=tablavial)
    query_max_vel="""ALTER TABLE public.{tablavial} ADD COLUMN max_walk_speed double precision;
                    UPDATE public.{tablavial} SET max_walk_speed=1.3;""".format(tablavial=tablavial)
    query_cost= """ALTER TABLE public.{tablavial} ADD COLUMN cost double precision;
                UPDATE public.{tablavial} SET cost=length/max_walk_speed;""".format(tablavial=tablavial)
    query_nulls= """DELETE FROM {tablavial} WHERE source IS Null;
                    SELECT * FROM {tablavial} WHERE source IS NULL;""".format(tablavial=tablavial)
    connection.execute(query_length)
    connection.execute(query_max_vel)
    connection.execute(query_cost)
    connection.execute(query_nulls)
    print("Campos costo, longitud y velocidad máxima creados y se elminaron las entradas nulas en {tablavial}".format(tablavial=tablavial))

def indexEspacial(tablename, database=None):
    """
    Funcion para crear index espacial
    """
    connection=pgConnect(database)
    query_index="""CREATE INDEX {indexcol}
                    ON {tablename} USING GIST (geometry);""".format(tablename=tablename,indexcol=tablename+"_idx")
    print("índice espacial creado en {tablename}".format(tablename=tablename))

def areaServicio(layer_streets,layer_points,outputTable):
    """
    Esta función realiza recortes de la capa vial haciendo un reorrido por las vias a partir de cada paradero
    y agrupa por cada identificador una entidad independiente de tipo lineal
    """
    #importa clase Settings para extraer sus atributos de conexion
    settings=Settings()
    #PARAMETROS DE AREA DE SERVICIO
    #es util correr en consola processing.algorithmHelp("qgis:serviceareafromlayer")
    #la salida se carga a postgres directamente al pasar una string con los datos de conexion en la forma que processing.run acepta
    #el nombre de la salida de este primer algortimo es el nombre de salida insertado por el usuario con el prefijo _line
    out_def=outputTable #nombre de tabla intermedia
    print("tabla intermedia: {out_def}".format(out_def=out_def))
    str_output__line = "postgis:dbname=\'" + settings.database + "\' host=" + settings.host + " port=" + settings.port + " user=" + settings.user + " password=" + settings.password + " table=\"public\".\"" + out_def + "\" (geometry) sql="
    parametros_serv={'INPUT':layer_streets,
                'START_POINTS':layer_points,
                'TRAVEL_COST':400,
                'SPEED_FIELD':"max_walk_speed",
                'TOLERANCE':0.000002,
                'STRATEGY':0,
                'OUTPUT_LINES':str_output__line}
    
    processing.run('qgis:serviceareafromlayer',parametros_serv)
    
    #cargar a QGIS
    o1=pq.pgisQgis()
    if outputTable in o1.tableNames():
        o1=pq.pgQgis(outputTable)
    #string identico al anterior para almacenar la saluda del siguiente algoritmo en esta funcion
    #con la diferencia de que la tabla de salida es el insertado por el usuario  
        print("recorridos por la geometría calculados y cargados")

#recoge la capa de saluda de la funcion anterior    
def poly_areaServicio(layer_area_service_line,outputTable):        
    """
    Crea un poligono convexo a partir de los puntos extremos de cada entidad lineal resultante
    de recorrer 400 mts las calles desde cada paradero
    """
    
    #generar un objeto vectorial a partir de la URI de la tabla de salida del algortimo anterior
    #llama la funcion uri_con definida en la linea 92
    #importa clase Settings para extraer sus atributos de conexion
    settings=Settings()
    
    str_output_db = "postgis:dbname=\'" + settings.database + "\' host=" + settings.host + " port=" + settings.port + " user=" + settings.user + " password=" + settings.password + " table=\"public\".\"" + outputTable + "\" (geometry) sql="
    #layer_input = QgsVectorLayer(uri_con(outputTable+"_line"), outputTable, "postgres")
    #parametros crear poligonos area de servicio
    #input line layer, field to group by, type of resulting geometry (3 to convex hull), y parametros de carga para almacenar en postgres)
    parametros_poly={'FIELD':'gid',
                    'INPUT':layer_area_service_line,
                    'OUTPUT':"TEMPORARY_OUTPUT",
                    'TYPE':3
    }
    
    result=processing.run('qgis:minimumboundinggeometry',parametros_poly)
    
    #insertar a postgres
    parametros_qgisToPostgres={'INPUT':result['OUTPUT'],
                    'DATABASE':settings.database,
                    'TABLENAME':outputTable,
                    'PRIMARY_KEY':'gid',
                    'GEOMETRY_COLUMN':'geometry',
                    'OVERWRITE':True,
                    'DROP_STRING_LENGTH':True
                    
    }
    processing.run('qgis:importintopostgis', parametros_qgisToPostgres)
    
    #cargar a QGIS
    o1=pq.pgisQgis()
    if outputTable in o1.tableNames():
        o1=pq.pgQgis(outputTable)
    #string identico al anterior para almacenar la saluda del siguiente algoritmo en esta funcion
    #con la diferencia de que la tabla de salida es el insertado por el usuario  
        print("areas de servicio calculadas y cargadas")


def buffer(layer_areasServ_lineal, layer_points, buffer_output, database=None):
    """
    crear campos nuevos en la capa de tramos dentro de un rango de 400 mts y crea una capa nueva
    que es un buffer circular al rededor de cada paradero para computar indicadores de accesibilidad
    """
    connection=pgConnect(database)
    query_length="""ALTER TABLE {layer_areasServ_lineal} ADD COLUMN length NUMERIC;
                    UPDATE {layer_areasServ_lineal} SET length = ST_length(geometry)""".format(layer_areasServ_lineal=layer_areasServ_lineal)
    query_buffer="""CREATE TABLE {buffer_output} AS SELECT *, (SELECT ST_Buffer(geometry, 400)) FROM {layer_points}; """.format(layer_areasServ_lineal=layer_areasServ_lineal, buffer_output=buffer_output, layer_points=layer_points)
    query_area="""ALTER TABLE {buffer_output} ADD COLUMN area double precision;
                  UPDATE {buffer_output} SET area = ST_AREA(st_buffer);""".format(buffer_output=buffer_output)
    connection.execute(query_length)
    connection.execute(query_buffer)
    connection.execute(query_area)
    print("Capa enriquecida: {layer_areasServ_lineal} y capa creada: {buffer_output}".format(layer_areasServ_lineal=layer_areasServ_lineal,buffer_output=buffer_output))
    
def buffer_intersect(layer_streets, buffer_input, campo_ID, intersect_output, database=None):
    """
    funcion para hacer una interseccion entre la capa de buffer circular y la malla vial original, 
    para calcucal el índicador ISAI que es el resultado de dividir la longitud de los tramos de cada intersección de calles con 
    cada buffer circular por el área del buffer circular calculado
    """
    connection=pgConnect(database)
    query_intersect="""CREATE TABLE {intersect_output} AS SELECT buffer.gid, buffer.{campo_ID}, st_union(ST_INTERSECTION(calles.geometry, buffer.st_buffer))
                  FROM {layer_streets} AS calles, {buffer_input} AS buffer
                  WHERE ST_Intersects(calles.geometry, buffer.st_buffer)
                  GROUP BY buffer.gid, buffer.{campo_ID};""".format(layer_streets=layer_streets, buffer_input=buffer_input,campo_ID=campo_ID,intersect_output=intersect_output)
    query_length="""ALTER TABLE {intersect_output} ADD COLUMN length numeric;
                    UPDATE {intersect_output} SET length = ST_length(st_union);""".format(intersect_output=intersect_output)
    connection.execute(query_intersect)
    connection.execute(query_length)
    print("Capa creada y enriquecida: {intersect_output}".format(intersect_output=intersect_output))
 
 
def indicadores(intersect_input,layer_census, layer_points, buffer_input,layer_areasServ_lineal,layer_areasServ_poly,campo_ID,indicadores_output, database=None):
    """
    Crear una tabla de paraderos con toda la información de las otras tablas creadas con la información necesaria, se hacen 4 join con el 
    campo “ntrcodigo” a la tabla paraderos y una selección de las columnas para la nueva tabla
    """
    connection=pgConnect(database)
    
    query_joins="""CREATE TABLE {indicadores_output} AS select 
                        paradero.{campo_ID}, paradero.ntrnombre, paradero.ntrdirecci, paradero.geometry,
                        inter.length AS buf_tramo_length,
                        buffer.area AS buf_circular_area,
                        tramos_areas_ser.length AS areas_serv_length,
                        areas_poli.area AS area_serv_area
                        from {layer_points} AS paradero 
                        inner join {intersect_input} AS inter on paradero.{campo_ID} = inter.{campo_ID}
                        inner join {buffer_input} AS buffer on inter.{campo_ID}=buffer.{campo_ID}
                        inner join {layer_areasServ_lineal} AS tramos_areas_ser on buffer.{campo_ID} = tramos_areas_ser.{campo_ID}
                        inner join {layer_areasServ_poly} AS areas_poli on tramos_areas_ser.{campo_ID} = areas_poli.{campo_ID};""".format(indicadores_output=indicadores_output,campo_ID=campo_ID,layer_points=layer_points,intersect_input=intersect_input,buffer_input=buffer_input,layer_areasServ_lineal=layer_areasServ_lineal,layer_areasServ_poly=layer_areasServ_poly)
    query_indicadores="""CREATE INDEX {indicadores_output}_idx ON {indicadores_output} USING GIST (geometry);
                         ALTER TABLE {indicadores_output} ADD COLUMN isai numeric;
                         UPDATE {indicadores_output} SET isai =  buf_tramo_length / buf_circular_area;
                         ALTER TABLE {indicadores_output} ADD COLUMN asai numeric;
                         UPDATE {indicadores_output} SET asai =  areas_serv_length/area_serv_area;
                         ALTER TABLE {indicadores_output} ADD COLUMN scri numeric;
                         UPDATE {indicadores_output} SET scri =  buf_circular_area/area_serv_area;""".format(indicadores_output=indicadores_output)
    query_pob="""ALTER TABLE {indicadores_output} ADD COLUMN poblacion_servida numeric;
                UPDATE {indicadores_output}
                SET poblacion_servida = i.poblacion_servida 
                FROM (SELECT buffer.gid, buffer.area/{layer_census}.area_mcuadrados * {layer_census}.personas AS poblacion_servida 
                FROM {buffer_input} AS buffer, {layer_census} AS {layer_census} 
                WHERE ST_intersects(buffer.geometry, {layer_census}.geometry)) AS i WHERE {indicadores_output}.gid = i.gid;""".format(indicadores_output=indicadores_output,layer_census=layer_census,buffer_input=buffer_input)
    connection.execute(query_joins)
    connection.execute(query_indicadores)
    connection.execute(query_pob)
    print("Capa creada y enriquecida: {indicadores_output}".format(indicadores_output=indicadores_output))
 
    