# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 21:13:47 2018

@author: ASUS
"""
#importación de la libreria arcpy

import arcpy
pdfPath = r"E:\C\Tesina_master_sig\PDF\Fase_1\Fase_I_todo.pdf"
pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfPath)
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\Fase_I_texto.pdf")
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\Fase_I_carto.pdf")


pdfDoc.saveAndClose()
del pdfDoc

