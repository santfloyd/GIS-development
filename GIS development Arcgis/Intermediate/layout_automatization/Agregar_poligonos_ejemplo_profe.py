#-------------------------------------------------------------------------------
# Name:        dialog_template
# Purpose:     template for dialog class in pyqt4
#
# Author:      jpalomav
#
# Created:     10/04/2017
# Copyright:   (c) jpalomav 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Creacion de un script asociado de agregacion 
por area de influencia utilizando PyQt4

'''
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFileDialog, QMessageBox
import arcpy
import os
import arcpy.mapping as mapp
import winsound


#load form
form_class = uic.loadUiType("Agregar_poligonos_ejemplo_profe.ui")[0]

#dialog class
class MyDialogClass(QtGui.QDialog, form_class):
    #init function
    def __init__(self, parent = None):
        #init class dialog
        QtGui.QDialog.__init__(self,parent)
        #run dialog
        self.setupUi(self)
        self.inicia()
        self.chk_fijo.stateChanged.connect(self.cambiaEstado)
        self.btn_entrada.clicked.connect(self.entrada)
        self.btn_salida.clicked.connect(self.salida)
        self.btn_salir.clicked.connect(self.salir)
        self.btn_ejecutar.clicked.connect(self.ejecutar)
    
    def inicia(self):
        self.cb_dist.setEnabled(False)
        self.cb_tol.setEnabled(False)
    
    def cambiaEstado(self):
        if self.chk_fijo.isChecked():
            self.cb_dist.setEnabled(True)
            self.cb_tol.setEnabled(True)
            self.txt_dist.setEnabled(False)
            self.txt_tol.setEnabled(False)
        else:
            self.cb_dist.setEnabled(False)
            self.cb_tol.setEnabled(False)
            self.txt_dist.setEnabled(True)
            self.txt_tol.setEnabled(True)
    
    def valida(self,numero):
        try:
            float(numero)
            return float(numero)
        except:
            QMessageBox.critical(None,'Error','El valor no es un numero')
            return None
    
    def entrada(self):
        fn = QFileDialog.getOpenFileName(None,'Capa de entrada',filter='*.shp')
        if str(fn) != '':
            self.txt_entrada.setText(str(fn))
    
    def salida(self):
        fn = QFileDialog.getSaveFileName(None,'Capa de salida',filter='*.shp')
        if str(fn) != '':
            self.txt_salida.setText(str(fn))

    def salir(self):
        app.quit()
    
    def ejecutar(self):
        fn_entrada = str(self.txt_entrada.text())
        fn_salida = str(self.txt_salida.text())
        if self.chk_fijo.isChecked():
            dist = float(str(self.cb_dist.currentText()))
            tol = float(str(self.cb_tol.currentText()))
        else:
            dist = self.valida(str(self.txt_dist.text()))
            tol = self.valida(str(self.txt_tol.text()))
            if dist == None or tol == None:
                return
        self.pb_progreso.setValue(25)
        fn_intermedio = os.path.dirname(fn_entrada)+'\\intermedio.shp'
        arcpy.Buffer_analysis(fn_entrada, fn_intermedio,dist,dissolve_option='ALL')
        self.pb_progreso.setValue(50)
        arcpy.Buffer_analysis(fn_intermedio,fn_salida,dist*(-0.9))
        self.pb_progreso.setValue(75)
        arcpy.Generalize_edit(fn_salida,tol)
        arcpy.Delete_management(fn_intermedio)
        self.pb_progreso.setValue(100)
        QMessageBox.information(None,'Proceso','Proceso terminado')

app = QtGui.QApplication(sys.argv)
myDialog = MyDialogClass(None)
myDialog.show()
app.exec_()