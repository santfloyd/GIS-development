'''
pdf por cada provincia con campos nombre, area (km2) perimetro (km)
'''


import arcpy
import arcpy.mapping as mapp
import winsound

#una vez cargada manualmente la capa al mxd
ruta_mxd = r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\proyecto4.mxd"

#acceder al proyecto
mxd = mapp.MapDocument(ruta_mxd)

#acceder al primer df
df=mapp.ListDataFrames(mxd)[0]

#acceder a la primera capa provincia
capa_prov=mapp.ListLayers(mxd, "", df)[0]

#campos de interes para el texto dinamico
campos_interes=['NOMBRE','SHAPE@AREA','SHAPE@LENGTH']

#cursor con los campos de interes
cursor= arcpy.da.SearchCursor(capa_prov, campos_interes)

#iterar en el cursor asignando a cada variable por el orden de campos pasados al cursor
for fila in cursor:
    nombre=fila[0]
    area=fila[1]
    perim=fila[2]
    
    #creacion de una consulta dinamica para la seleccion posterior
    consulta= ''' "NOMBRE" = '{nom}' '''.format(nom=nombre)
    print(consulta)
    #seleccionar la provincia con seleccion por atributos
    arcpy.SelectLayerByAttribute_management(capa_prov,'NEW_SELECTION',consulta)
    #zoom a la seleccion
    df.zoomToSelectedFeatures()
    #LISTAR ELEMENTOS GRAFICOS
    lista_graficos = mapp.ListLayoutElements(mxd, "TEXT_ELEMENT")
    for grafico in lista_graficos:
        #en el proyecto se les dio un nombre a cada elemento textual
        if grafico.name == 'txt_nombre':
            grafico.text = nombre
        if grafico.name == 'txt_area':
            grafico.text = str(area/1000000) #en km2
        if grafico.name == 'txt_perimetro':
            grafico.text = str(perim/1000) #en km
    #se modifica la ruta en cada iteracion en el cursor y el pdf de salida tiene el nombre de cada provincia
    ruta_pdf= r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\{nom}.pdf".format(nom=nombre)
    #exporta a pdf
    mapp.ExportToPDF(mxd,ruta_pdf)
    


#alarma de finalizacion
winsound.Beep(500,1000)