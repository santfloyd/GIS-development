'''
Created on 24/02/2021

@author: Usuario
'''
import arcpy

ruta_mxd=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo de aplicaciones SIG\proyectos\proyecto1.mxd"
if not arcpy.Exists(ruta_mxd):
    print 'Ruta no valida'
else:
    print(arcpy.Exists(ruta_mxd))