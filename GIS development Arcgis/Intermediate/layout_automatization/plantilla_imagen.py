'''
plantilla con imagen genrada en tiempo real
'''

import arcpy
import arcpy.mapping as mapp

#se debio actualizar matplotlib mediante eclipse para que dejara guardar en jpg
import matplotlib.pyplot as plt
import os
import winsound



ruta_mxd = r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\sesion4\Teoria\sesion4_2c.mxd"
ruta_out= r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts"

ruta_imagen=os.path.join(ruta_out,'grafica_pob2.jpg')

ruta_pdf=os.path.join(ruta_out,'mapa_grafica2.pdf')

mxd = mapp.MapDocument(ruta_mxd)
df=mapp.ListDataFrames(mxd)[0]
capa_mun=mapp.ListLayers(mxd, "", df)[0]

#seleccion del municipio
#si el mxd no tiene la ruta de los shapes la consulta sale invalida, toca rapair source
consulta= ''' "NOMBRE" = 'Carmenes' '''
print(consulta)
arcpy.SelectLayerByAttribute_management(capa_mun,'NEW_SELECTION', consulta)
df.zoomToSelectedFeatures()

#obtencion de datos
cursor= arcpy.SearchCursor(capa_mun, consulta)

for fila in cursor:
    nombre=fila.NOMBRE
    pob91=fila.POB91
    pob95=fila.POB95
del cursor 

#creacion de grafica
datos=[pob91, pob95]
etiquetas=[1,2] #no es el texto de la etiqueta, sino el lugar en la grafica
plt.figure(figsize=(5,5)) #el tamano de la grafica
plt.title('Evolucion habitantes')
plt.bar(etiquetas,datos,width=0.5,align='center')
plt.xticks(etiquetas,['1991','1995'])
plt.savefig(os.path.join(ruta_imagen))

#modificar los graficos del layout
lista_graficos=mapp.ListLayoutElements(mxd)
for grafico in lista_graficos:
    if grafico.name == 'txt_nombre':
        grafico.text = nombre
    if grafico.name == 'img_grafica':
        #metodo para insertar la imagen en la ruta especificada
        grafico.sourceImage=ruta_imagen
mapp.ExportToPDF(mxd, ruta_pdf)
winsound.Beep(250,1000)