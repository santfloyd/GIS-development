#-*- coding: utf-8 -*-

#modulo para exportar mapas
from qgis.PyQt import QtGui
from qgis.core import QgsProject


#layers= QgsProject.instance().mapLayersByName("paraderos_indicadores")
#layer= layers[0]

#crear el layout
project=QgsProject.instance()
manager=project.layoutManager()
layoutName='Layout'
layout_list= manager.printLayouts()

#elimina layout duplicado, si lo hay y crea el layout
for layout in layout_list:
    if layout.name() == layoutName:
        manager.removeLayout(layout)
layout = QgsPrintLayout(project)
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)

#crea un espacio para el mapa en el layout
map= QgsLayoutItemMap(layout)
map.setRect(20,20,20,20)

#establecer extent
ms= QgsMapSettings()


#identifica las capas a cargar en el layout
for layer in QgsProject.instance().mapLayers().values():
    if layer.name() in ["paraderos_indicadores","malla_vial","muni_proj"]:
        ms.setLayers([layer]) #layer a ser mapeadas
#determina el extent
rect = QgsRectangle(ms.fullExtent())
rect.scale(1.0)
ms.setExtent(rect)
map.setExtent(rect)
map.setFrameEnabled(True) #dibujar el marco al rededor del elemento
layout.addLayoutItem(map)

#determina la posicion del espacio del mapa en el canvas
map.attemptMove(QgsLayoutPoint(5, 20, QgsUnitTypes.LayoutMillimeters))
map.attemptResize(QgsLayoutSize(180,180, QgsUnitTypes.LayoutMillimeters))

#configura la simbologia de las capas
capa_nombre = 'paraderos_indicadores'
rampa_nombre = 'Spectral'
campo_paraderos = 'poblacion_servida'
num_clases = 5
classification_method_paraderos = QgsClassificationJenks() #clasificacion por ruptura natural

paraderos= QgsProject().instance().mapLayersByName(capa_nombre)[0] #crear el objeto vectorial
estilo = QgsStyle().defaultStyle() #estilo por defecto
rampa_color = estilo.colorRamp(rampa_nombre) #rampa de color

renderer = QgsGraduatedSymbolRenderer() #renderizador por simbolo graduado
renderer.setGraduatedMethod(0) #0 para color 1 para tamaño
renderer.setClassAttribute(campo_paraderos) #establecer el campo para graduar
renderer.setClassificationMethod(classification_method_paraderos) #metodo de draduación
renderer.setMode(2) #modo de clasificacion "Jenks rupturas naturales"=2
renderer.setSymbolSizes(0.9,1.2) #min size, max size
renderer.updateClasses(paraderos, num_clases) #realizar el update segun el numero de clases deseado
renderer.updateColorRamp(rampa_color) #apliar rampa de color

paraderos.setRenderer(renderer) #aplicar el renderizador a la capa vectorial
paraderos.triggerRepaint() #repintar

capa_nombre1 = 'malla_vial'
malla_vial = QgsProject().instance().mapLayersByName(capa_nombre1)[0]

renderer1 = QgsLineSymbol() #renderizador de tipo linea
renderer1.setWidth(0.15) #ancho de linea
renderer1.setColor(QColor(Qt.darkMagenta)) #colorea con un color predefinido darkmagenta
malla_vial.setRenderer(QgsSingleSymbolRenderer(renderer1)) #aplicar el renderizador que a su vez contiene el metodo de simbolo único
malla_vial.triggerRepaint() #repintar

capa_nombre2="muni_proj"
municipio = QgsProject().instance().mapLayersByName(capa_nombre2)[0]

estilo2='outline red'
estilo2_defecto = QgsStyle().defaultStyle() #estilo por defecto
estilo2_nuevo = estilo2_defecto.symbol(estilo2) #aplica el nombre de estilo predefinido en QGIS
municipio.renderer().setSymbol(estilo2_nuevo)
municipio.triggerRepaint()

#añadir mapa base
urlWithParams = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
basemap = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  

if basemap.isValid():
    QgsProject.instance().addMapLayer(basemap)
else:
    print('invalid layer')

#para añadir la capa base al fondo es ncesario crear
#una instacncia de layerTreeRoot
#insertar un child -1 para que inserte en el último lugar la capa base
#que se le pasa a la clase QgsLayerTreeLayer
root = QgsProject.instance().layerTreeRoot()
root.insertChildNode(-1, QgsLayerTreeLayer(basemap))

#mapa de localizacion
map1= QgsLayoutItemMap(layout)
map1.setRect(10,10,10,10)
map1.setLayers(project.mapLayersByName("muni_proj"))
rect1 = QgsRectangle(ms.fullExtent())
rect1.scale(3.0)
map1.setExtent(rect1)
map1.setFrameEnabled(True) #dibujar el marco al rededor del elemento
layout.addLayoutItem(map1)
map1.attemptMove(QgsLayoutPoint(225, 20, QgsUnitTypes.LayoutMillimeters))
map1.attemptResize(QgsLayoutSize(60,60, QgsUnitTypes.LayoutMillimeters))


#añade leyenda
legend = QgsLayoutItemLegend(layout)
legend.setTitle("Leyenda")
layerTree= QgsLayerTree()
for layer in QgsProject.instance().mapLayers().values():
    if layer.name() in ["paraderos_indicadores","malla_vial","muni_proj"]:
        layerTree.addLayer(layer)
legend.model().setRootGroup(layerTree)
layout.addLayoutItem(legend)
#ubicacion de la escuqina inferior izquerda del elemento
legend.attemptMove(QgsLayoutPoint(230,120, QgsUnitTypes.LayoutMillimeters))

#añade escala
scalebar = QgsLayoutItemScaleBar(layout)
scalebar.setStyle('Line Ticks Bar')
scalebar.setUnits(QgsUnitTypes.DistanceKilometers)
scalebar.setNumberOfSegments(4)
scalebar.setNumberOfSegmentsLeft(0)
scalebar.setUnitsPerSegment(2.0)
scalebar.setLinkedMap(map)
scalebar.setUnitLabel('km')
scalebar.setFont(QFont('Arial',14))
scalebar.update()
layout.addLayoutItem(scalebar)

scalebar.attemptMove(QgsLayoutPoint(220,190, QgsUnitTypes.LayoutMillimeters))

#añade un titulo
title= QgsLayoutItemLabel(layout)
title.setText('Análisis de Accesibilidad Espacial a la red de transportes públicos en Bogotá, Colombia')
title.setFont(QFont('Arial',20))
title.adjustSizeToText()
layout.addLayoutItem(title)
title.attemptMove(QgsLayoutPoint(10,5,QgsUnitTypes.LayoutMillimeters))

#Añadir norte
north = QgsLayoutItemPicture(layout)
north.setPicturePath("C:/Program Files/QGIS 3.16/apps/qgis/svg/arrows/NorthArrow_11.svg")
layout.addLayoutItem(north)
north.attemptResize(QgsLayoutSize(20, 25,QgsUnitTypes.LayoutMillimeters))
north.attemptMove(QgsLayoutPoint(15,25,QgsUnitTypes.LayoutMillimeters)) 

#exporta como pdf
layout=manager.layoutByName(layoutName)
exporter =  QgsLayoutExporter(layout)

fn = 'E:/C/Master_geomatica/desarrollo_SIG/Desarrollo_de_aplicaciones_SIG/entrega3/salida_grafica/accesibilidad_poblacion_servida.pdf'
exporter.exportToPdf(fn, QgsLayoutExporter.PdfExportSettings())

