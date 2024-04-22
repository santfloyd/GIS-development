'''
filtrado de elementos e impresion de propiedades
'''


import arcpy.mapping as mapp

ruta_mxd = r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\proyecto4.mxd"

#acceder al proyecto
mxd = mapp.MapDocument(ruta_mxd)

#acceder a los elementos graficos del layout dentro del proyecto
#el segundo y tercero elemento es opcional
#se puede filtrar los elementos indicando el tipo de elemento
lista_graficos = mapp.ListLayoutElements(mxd, "TEXT_ELEMENT")

for grafico in lista_graficos:
    #solo imprimir los que tengan nombre definido en su propiedad element name
    if grafico.name!="":
        mensaje='nombre: '+grafico.name+', '+'tipo: '+grafico.type+', '+'X: '+str(grafico.elementPositionX)+', '+'Y: '+str(grafico.elementPositionY)
        print(mensaje)