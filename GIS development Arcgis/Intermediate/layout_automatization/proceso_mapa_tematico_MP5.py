#-*- coding: utf-8 -*-
'''

'''

#para que funcionara se debió instalar pyqt4 con el python de arcgis asi
#ir a C:\Python27\ArcGIS10.8\scripts> y luego instalar con
#.\pip.exe install <path_al_archivo_wheel>\PyQt4-4.11.4-cp27-cp27m-win32.whl
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import QMessageBox, QFileDialog

import arcpy
import arcpy.mapping as mapp

#load form
form_class = uic.loadUiType("proceso_mapa_tematico_MP5.ui")[0]

#dialog class
class MyDialogClass(QtGui.QDialog, form_class):
    #init function
    def __init__(self, parent = None):
        #init class dialog
        QtGui.QDialog.__init__(self,parent)
        #run dialog
        self.setupUi(self)
        self.cancelar.clicked.connect(self.cerrar)
        self.ejecutar.clicked.connect(self.ejecutar_auto_layout)
        self.entrada_explora.clicked.connect(self.entrada)
        self.salida_explora.clicked.connect(self.salida)
        self.year_selector.valueChanged.connect(self.spin_box)
        self.class_selector.valueChanged.connect(self.spin_box)
        self.legend_check.stateChanged.connect(self.chck_box)
        self.scalebar_check.stateChanged.connect(self.chck_box)
        self.northarrow_check.stateChanged.connect(self.chck_box)
        #self.progressBar.stateChanged.connect(self.increase_progressBar)
        
    #def increase_progressBar(self, progressBar):
     #   progressBar.setValue(0)
        
    def cerrar(self):
        #cerrar
        app.quit()
        
    def spin_box(self):
        self.year_selector.setRange(1976,2013)
        self.class_selector.setRange(1,30)
    
    def chck_box(self):
        if self.legend_check.isChecked():
            self.legend_check.setEnabled(True)
        if self.scalebar_check.isChecked():
            self.legend_check.setEnabled(True)
        if self.northarrow_check.isChecked():
            self.northarrow_check.setEnabled(True)
        

    def valida_input(self, cadena):
        #validar valor de entrada
        if cadena.lower().endswith('.mxd'):
            return cadena
        else:
            QMessageBox.critical(None,"Error","La herramienta solo admite archivos tipo Shapefile (.shp)")
            return None
    
    def valida_output(self, cadena):
        #valida output
        if cadena.lower().endswith('.pdf'):
            return cadena
        else:
            QMessageBox.critical(None,"Error","La herramienta solo exporta archivos tipo PDF (.pdf)")
            return None
     
    def entrada(self):
        fn = QFileDialog.getOpenFileName(None,'Capa de entrada',filter='*.mxd')
        if str(fn) != '':
            self.entrada_casilla.setText(str(fn))
    
    def salida(self):
        fn = QFileDialog.getSaveFileName(None,'Capa de salida',filter='*.pdf')
        if str(fn) != '':
            self.salida_casilla.setText(str(fn))   
    
    def ejecutar_auto_layout(self):
        self.progressBar.setValue(0)
        #convertir a string el formato Qstring que devuelve .text()
        input_mxd=self.valida_input(str(self.entrada_casilla.text()))
        output_pdf=self.valida_output(str(self.salida_casilla.text()))
        
        #acceder al proyecto y al df
        mxd = mapp.MapDocument(input_mxd)
        df=mapp.ListDataFrames(mxd)[0]
        #identificar la capa de interes
        lyr = arcpy.mapping.ListLayers(mxd, "paro_ccaa_1976_2013", df)[0]
        #reclasificar la simbologia que previamente en el proyecto se establecio en 
        #graduated colors
        lyr.symbology.reclassify()
        #cambiar los valores de clasificacion respecto a los valores introducidos por el usuario
        lyr.symbology.valueField = str(self.year_selector.text())
        lyr.symbology.numClasses = int(self.class_selector.text())
        #extent del df para la impresion de los mapas
        Extent = lyr.getExtent(True)
        df.extent = Extent 
        arcpy.RefreshActiveView()
        self.progressBar.setValue(20)
        #elementos graficos y textuales del layout
        lista_txt = mapp.ListLayoutElements(mxd, "TEXT_ELEMENT")
        #en el proyecto se les dio un nombre a cada elemento textual
        for txt in lista_txt:
            if txt.name == 'Title':
                txt.text = unicode(self.title_map.text())
            if txt.name == 'Subtitle':
                txt.text = str(self.year_selector.text())
            if txt.name == 'descripcion':
                txt.text = unicode(self.descripcion_map.text())
            if txt.name == 'proyecto':
                txt.text = unicode(self.project.text())
            if txt.name == 'autor':
                txt.text = unicode(self.author_map.text())
        self.progressBar.setValue(40)
        if self.legend_check.isChecked:
            #incluir el elemento legend
            legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT","Legend")[0]
            #modificar la posicion x para que aparezca dentro del layout
            legend.autoAdd = True
            legend.elementPositionX = legend.elementPositionX + 29.5
            print("leyend is checked")
        self.progressBar.setValue(60)
        if self.scalebar_check.isChecked():
            #incluir elemento scale bar
            scalebar = arcpy.mapping.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT",'Scale Bar')[0]
            
            #modificar la posicion x para que aparezca dentro del layout
            scalebar.elementPositionX = scalebar.elementPositionX + 26.7
            print("scalebar is checked")
        self.progressBar.setValue(80)
        if self.northarrow_check.isChecked():
            #incluir elemento norte
            north = arcpy.mapping.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT",'North Arrow')[0]
            
            #modificar la posicion x para que aparezca dentro del layout
            north.elementPositionX = north.elementPositionX + 4.5
            print("northarrow is checked")
        
        #exporta a pdf
        mapp.ExportToPDF(mxd, output_pdf)
        del mxd
        self.progressBar.setValue(100)
        QMessageBox.information(None,'Proceso','Proceso terminado')
        
app = QtGui.QApplication(sys.argv)
myDialog = MyDialogClass(None)
myDialog.show()
app.exec_()