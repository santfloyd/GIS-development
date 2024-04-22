# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 21:13:47 2018

@author: ASUS
"""
#importación de la libreria arcpy

import arcpy
pdfPath = r"E:\C\Tesina_master_sig\PDF\Fase_1\Fase_I_carto.pdf"
pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfPath)
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\localidad_censo.pdf")
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\upz_censo.pdf")
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\zat_censo.pdf")
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\indicador_ISAI.pdf")
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\indicador_ASAI.pdf")
pdfDoc.appendPages(r"E:\C\Tesina_master_sig\PDF\Fase_1\indicador_SCRI.pdf")
pdfDoc.saveAndClose()
del pdfDoc

