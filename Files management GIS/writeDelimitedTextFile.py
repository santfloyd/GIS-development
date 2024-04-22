# -*- coding: utf-8 -*-
"""
Created on Tue May 01 13:32:25 2018

@author: ASUS
"""
#abrir el fichero con la info
f=open("C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\N_America.A2007275.txt", 'r')
#crea un archivo y lo abre gracias al mode w de open
fw=open("C:\GeoSpatialTraining\Conceptos medios python GIS\Exercises\N_America.A2007275_min.txt", 'w')
#escribe el texto siguiente para las cabeceras
fw.write("Latitud, Longidtud, Confidence" +"\n")
#loop para extraer los valores de cada lista o linea 
Lstfires=f.readlines()
for line in Lstfires:
    Lstfires=line.split(",")
    latitud=Lstfires[0]
    longitud=Lstfires[1]
    confidence=Lstfires[8]
    #escribe en ese orden las variables de arriba en la loop
    escritura=fw.write(latitud +","+ longitud +","+ confidence)
    #muestra lo que escribe
    print latitud +","+ longitud +","+ confidence
#cierra ambos archivos
f.close()
fw.close()
    
    
    