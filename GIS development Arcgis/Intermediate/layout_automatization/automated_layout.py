'''
automatizar la plantilla
'''

import arcpy.mapping as mapp
import arcpy

#sonido cuando termine el proceso
import winsound


ruta_mxd = r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\proyecto4.mxd"
ruta_pdf= r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\mapa1.pdf"
#acceder al proyecto
mxd = mapp.MapDocument(ruta_mxd)

#acceder al primer df
df=mapp.ListDataFrames(mxd)[0]

#acceder a la primera capa
capa_mun=mapp.ListLayers(mxd, "", df)[0]

consulta= ''' "NOMBRE"= 'Posada de Valdeon' '''

print(consulta)
#seleccionar el municipio con seleccion por atributos
arcpy.SelectLayerByAttribute_management(capa_mun,'NEW_SELECTION', consulta)

#zoom a la seleccion
df.zoomToSelectedFeatures()

#acceso a los atributos de la capa con un cursor

cursor= arcpy.SearchCursor(capa_mun, consulta)

for fila in cursor:
    #nombre=fila.getValue('NOMBRE')
    nombre=fila.NOMBRE
    pob=fila.POB91

#LISTAR ELEMENTOS GRAFICOS
lista_graficos = mapp.ListLayoutElements(mxd, "TEXT_ELEMENT")
for grafico in lista_graficos:
    if grafico.name == 'txt_nombre':
        grafico.text = nombre
    if grafico.name == 'txt_pob':
        grafico.text = str(pob)
mapp.ExportToPDF(mxd,ruta_pdf)

print("proceso terminado")
#sonido cuando termine el proceso
winsound.Beep(500,1000)