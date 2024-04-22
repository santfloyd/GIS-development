'''
acceso a los elementos del layout
'''

import arcpy.mapping as mapp

ruta_mxd = r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\proyecto_automated_layout_MP5_1.mxd"

#acceder al proyecto
mxd = mapp.MapDocument(ruta_mxd)

#acceder a los elementos graficos del layout dentro del proyecto
#el segundo y tercero elemento es opcional
#se puede filtrar los elementos indicando el tipo de elemento
lista_graficos = mapp.ListLayoutElements(mxd, "TEXT_ELEMENT")
lista=mapp.ListLayoutElements(mxd, "LEGEND_ELEMENT")
lista_surro=mapp.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT")

for l in lista:
    print(l.type)
    print(l.name)


for grafico in lista_graficos:
    #solo imprimir los que tengan nombre definido en su propiedad element name
    #if grafico.name!="":
    print(grafico.type)
    print(grafico.name)

for l in lista:
    print(l.name)
    print(l.elementPositionX)

for sur in lista_surro:
    print(sur.name)
    print(sur.elementPositionX)