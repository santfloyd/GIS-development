'''
Seleccionar 
'''


import arcpy



shp_mun= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1-CASTELLANO\Datos\castilla-leon\MUNICIPIO.shp'
shp_car= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1-CASTELLANO\Datos\castilla-leon\CARRETERA.shp'
ruta_out= r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\proyectos\salidas_scripts\car_mun.shp'

arcpy.MakeFeatureLayer_management(shp_mun,'mun')
arcpy.MakeFeatureLayer_management(shp_car,'car')

consulta = ''' "NOM_MOPT" = 'E05'  '''

arcpy.SelectLayerByAttribute_management('car', 'NEW_SELECTION', consulta)
arcpy.SelectLayerByLocation_management('mun', 'INTERSECT','car', selection_type='NEW_SELECTION' )

arcpy.CopyFeatures_management('mun',ruta_out)

print 'proceso terminado'
