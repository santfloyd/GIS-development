#carga raster

ruta=r"E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\DEM\mde1.asc"

capa=QgsRasterLayer(ruta, 'DEM1', 'gdal')

if capa.isValid():
    proyecto=QgsProject.instance()
    proyecto.addMapLayer(capa)
else:
    print("no se ha podido cargar la capa")
    