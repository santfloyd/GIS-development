#carga de capa en una sola linea con variables iface QgisInterface
#atencion a los nombres de las capas

ruta_vec= r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\CARRETERA.SHP"
ruta_ras=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\DEM\mde2.asc"

#CARGA vectorial ES UNA REFERENCIA A LA CAPA O UN NONE
capa_vec = iface.addVectorLayer(ruta_vec, 'CARRETERAS', 'ogr')
capa_ras = iface.addRasterLayer(ruta_ras, 'DEM2', 'gdal')
if not capa_vec:
    print("no se ha podido cargar la capa vectorial")
    
if not capa_ras:
    print("no se ha podido cargar la capa raster")



