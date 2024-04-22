'''
crear un campo, un cursor tipo arcpy.da y tokens para guardar los datos en un .txt
'''

#modulos
import arcpy
from math import sqrt

#ruta del shape de provincias
shp_prov= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\PROVINCIA.shp'

#inspeccion de campos
campos=arcpy.ListFields(shp_prov)
lista_nombres=[campo.name.encode('utf8') for campo in campos] #encode utf-8 para impresion normal
print lista_nombres

#verificar si el campo a crear existe o no
if not 'CC' in lista_nombres:
    arcpy.AddField_management(shp_prov,'CC','FLOAT',10,3) #10 numero de digitos 3 numero de decimales
    cursor=arcpy.UpdateCursor(shp_prov)
    for fila in cursor:
        area=fila.getValue('AREA')
        perim=fila.getValue('PERIMETER')
        cc=0.28*(perim/sqrt(area))
        fila.setValue('CC',cc)
        cursor.updateRow(fila)
    del cursor
    print 'calculo terminado'
else:
    print 'campo ya existente'
    

#funcion para extraer los datos descriptivos    
def infoDesc(shape):
    desc=arcpy.Describe(shape)
    nombre_shp=desc.baseName
    path=desc.path
    
    return nombre_shp, path
    

#funcion para extraer solo los datos de los campos de interes (utiliza cursor .da y codificacion utf8 para los nombres)
def infoCampos(shape,lista_campos):
    
    cursor=arcpy.da.SearchCursor(shape,lista_campos)
    
    nombres=[]
    areas=[]
    perims=[]
    cc=[]
    for row in cursor:
        nombres.append(row[0].encode('utf8'))
        areas.append(row[1]/1000000)
        perims.append(row[2]/1000)
        cc.append(row[3])
        
    del cursor
    return nombres, areas, perims, cc


#funcion para extraer las estadisticas descriptivas de los campos para el resultado del informe
def estadisticas_campos(lista_areas,lista_perimetros,lista_cc):    
    total_area=sum(lista_areas)
    total_perim=sum(lista_perimetros)
    total_cc=sum(lista_cc)
    promedio_area=total_area/len(lista_areas)
    promedio_perimetro=total_perim/len(lista_perimetros)
    promedio_circularidad=total_cc/len(lista_cc)
    return total_area, total_perim, total_cc, promedio_area, promedio_perimetro, promedio_circularidad

#funcion para imprimir las filas en el informe
#usa el metodo format de las strings para formatear cada fila
def imprimeFila(datos):
    datos_string=''
    for n, a, p, c in datos:
        datos_string+="""
                {nombre}   {area}     {perimetro}     {circularidad}\n""".format(nombre=n, area=a, perimetro=p,circularidad=c)
    return datos_string


campos_interes=['NOMBRE','SHAPE@AREA','SHAPE@LENGTH','CC']

nombre_shp, path=infoDesc(shp_prov)
nombres, areas, perims, cc = infoCampos(shp_prov, campos_interes)
total_area, total_perim, total_cc, promedio_area, promedio_perimetro, promedio_circularidad = estadisticas_campos(areas, perims, cc)

#imprimir por pantalla
print 'nombre del shapefile:',unicode(nombre_shp)
print 'Ruta del shapefile:', path
print 'Nombres provincias:',nombres
print 'Areas de las provincias',areas
print 'Perimetros de las provincias:', perims
print 'Circularidad de las provincias:', cc
print 'Area total:', total_area
print 'Perimetro total:', total_perim
print 'Circularidad total:', total_cc
print 'Area media:', promedio_area
print 'Perimetro medio', promedio_perimetro
print 'Circularidad media:', promedio_circularidad

#escribir en un archivo de texto segun la salida grafica solicitada
with open(r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\informe_ejercicio_practico.txt","w") as file:
    
    guiones=50*'*'
    
    #string entre comillas triples permite strings en varias lineas
    encabezado="""
                ANALISIS DE COEFICIENTE DE CIRCULARIDAD
                {guiones}
                Datos de la capa
                {guiones}
                Nombre de la capa: {nombre_shp}
                Ruta: {path}
                Resultado
                {guiones}
                Nombre     Area(km2)     Perimetro(km)     Circularidad
                """.format(nombre_shp=nombre_shp,path=path,guiones=guiones).ljust(20)
    
    file.write(encabezado)
     
    #agrupa en tuplas las listas de datos           
    datos=zip(nombres, areas, perims, cc)
    
    file.write(imprimeFila(datos))       
               
    resumen="""
            RESUMEN
            {guiones}
            Area Media: {area_media} Km2
            Perimetro Medio: {perim_medio} km
            Circularidad Media: {cc_media}
            """.format(area_media=promedio_area,perim_medio=promedio_perimetro,cc_media=promedio_circularidad, guiones=guiones).ljust(20)
    
    file.write(resumen)
    
    print 'Escritura terminada'