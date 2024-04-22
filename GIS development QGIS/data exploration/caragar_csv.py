#carga de csv#-*- coding= utf-8 -*-
import os
#la ruta para csv requiere de un prefijo file:/// , añadir a la URI variables y al final .format("delimitador", "nombre colum X", "nombre columna Y")
ruta_csv=r'E:/C/Master_geomatica/desarrollo_SIG/Desarrollo_de_aplicaciones_SIG/PL1_CASTELLANO/Datos/vertices.csv'

#para que lo coja toca especificar todos los parametros, encoding, delimeter, X, Y, y crs
uri= 'file:///'+ruta_csv+'?encoding={}&delimiter={}&xField={}&yField={}&crs={}'.format("utf-8",";","X","Y","epsg:25830")
print(uri)
capa= QgsVectorLayer(uri, 'VERTICES','delimitedtext') #path, alias, para csv se usa el provider delimitedtext

#verificar si la capa es valida
if capa.isValid():
    #acceder al proyecto
    proyecto = QgsProject.instance()
    proyecto.addMapLayer(capa) #como el objeto QgsVectorLayer hace parte de los objetos QgsMapLar se puede pasar sin problema
else:
    print("no se ha podido cargar la capa csv")