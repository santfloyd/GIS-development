#-*- coding: utf-8 -*-

#modulos necesarios para abrir la conexion con postgres e importar al proyecto las capas vetoriales
from qgis.core import QgsVectorLayer, QgsDataSourceUri, QgsProject
from PyQt5.QtSql import *

#clase con parametros de conexion y carga de capas
class pgisQgis:
    host="localhost"
    port='5432'
    username="postgres"
    password="postgres"
    database="PROJDSIG"
    """
    El constructor admite un parametro database para que el usuario determine
    la base de datos a conectar
    """
    def __init__(self, database=None):
        self.host = pgisQgis.host
        self.port = pgisQgis.port
        self.username = pgisQgis.username
        self.password = pgisQgis.password
        if database == None:
            self.database=pgisQgis.database
        else:
            self.database=database
    
    #extraer todos los nombres de tablas en la base de datos
    #se usa la aproximacion con PyQt4.QtSql
    def tableNames(self): #solo se conecta a BBDD postgres
        db = QSqlDatabase.addDatabase("QPSQL"); #driver para postgres
        db.setHostName(pgisQgis.host);
        db.setPort(int(pgisQgis.port));
        db.setUserName(pgisQgis.username);
        db.setPassword(pgisQgis.password);
        db.setDatabaseName(pgisQgis.database);
        db.open();
        names=db.tables(QSql.Tables)
        return names


    def pgQgis(self, tablename, schema=None):
        #nombre de la columna con geometría en las tablas
        geometrycol = "geometry"

        #constructor con los componentes necesarios para abrir conexion
        uri = QgsDataSourceUri()

        #modificacion de atributos de la clase Uri con los parametros de conexion
        #port se debe transformar a str
        uri.setConnection(self.host, self.port, self.database, self.username, self.password)

        #establecer la fuente de datos
        
        if schema == None:
            uri.setDataSource ('public', tablename, geometrycol) #esquema, nombre de la tabla, nombre de la columna que almacena la geometria
        else:
            uri.setDataSource (schema, tablename, geometrycol) #esquema, nombre de la tabla, nombre de la columna que almacena la geometria
        
        #la clase QgsVectorLayer recibe la uri descompuesta 
        #únicamente con dbname, host, port y demás parámetros establecidos
        #en en setConnection y setDataSource 
        vlayer=QgsVectorLayer (uri.uri(False), tablename, "postgres")

        #añade la capa al proyecto
        proyecto=QgsProject.instance()
        proyecto.addMapLayer(vlayer)
        #mensaje de salida
        mensaje="Se ha cargado la capa {capa}".format(capa=tablename)
        return mensaje

