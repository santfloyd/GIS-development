'''
imprimir la tabla de atributos
'''

import arcpy

#para instalar la libreria toca toda la ruta
#C:\Python27\ArcGIS10.8\Scripts\pip install unicodecsv


shp_mun= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\MUNICIPIO.shp'

campos=arcpy.ListFields(shp_mun)

def imprimeCabecera(campos, ancho):
    cadena=''
    for campo in campos:
        if campo.type != 'Geometry': #no saca el campo de geometry
            cadena+=campo.name.ljust(ancho)
    print cadena
    print ancho*(len(campos)-1)*'-' #para formatear: el caracter'-' lo multiplica ancho * len de cada campo
    guiones=ancho*(len(campos)-1)*'-'
    return cadena+'\n'+ guiones+'\n'

cabecera=imprimeCabecera(campos, 15)

def imprimeFila(fila, campos, ancho):
    cadena=''
    for campo in campos:
        if campo.type != 'Geometry': #no saca el campo de geometry
            #como en un campo hay acentos es importante en lugar de usar str() usar unicode()
            cadena+= unicode(fila.getValue(campo.name)).ljust(ancho)
    print cadena
    return cadena


with open(r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\exportartabla_txt.txt","w") as file:
    file.write(cabecera)
    cursor=arcpy.SearchCursor(shp_mun)
    for fila in cursor:
        linea=imprimeFila(fila, campos, 15)
        #importante para poder escribir acentos
        file.write(linea.encode("UTF-8")+'\n')
    print(linea)



   

   


    