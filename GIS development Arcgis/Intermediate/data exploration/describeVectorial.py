'''
Descripcion de un archivo shp
'''

import arcpy

ruta_shp=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1_CASTELLANO\Datos\castilla_leon\MUNICIPIO.SHP'

desc=arcpy.Describe(ruta_shp)

print 'Propiedades comunes '

print 'propiedad baseName', desc.baseName
print 'propiedad CatalogPath', desc.catalogPath
print 'propiedad dataType', desc.dataType
print 'propiedad extension', desc.extension
print 'propiedad name', desc.name
print 'propiedad path', desc.path
print hasattr(desc,'shapeType')
print ' '
print 'propiedades especificas del feature class'
print 'featureType', arcpy.Describe(ruta_shp).featureType
print 'shapeType', arcpy.Describe(ruta_shp).shapeType
print 'extent', desc.extent
print 'SpatialReference', desc.spatialReference.name
 
ruta_raster=r'E:\C\Master_geomatica\desarrollo_SIG\Desarrollo_de_aplicaciones_SIG\PL1-CASTELLANO\Datos\sentinel2\30-S-YJ-2018-1-16-B11.tif'

desc_2=arcpy.Describe(ruta_raster)

print 'Propiedades comunes '

print 'propiedad baseName', desc_2.baseName
print 'propiedad CatalogPath', desc_2.catalogPath
print 'propiedad dataType', desc_2.dataType
print 'propiedad extension', desc_2.extension
print 'propiedad name', desc_2.name
print 'propiedad path', desc_2.path
print ' '
print 'propiedades especificas del feature class'
print 'featureType', desc_2.bandCount
print 'shapeType', desc_2.format
print ' '
print 'propiedades especificas arcpy.raster'
raster=arcpy.Raster(ruta_raster)
print 'height', raster.height
print 'width', raster.width
print 'resolution', raster.meanCellHeight
print 'spatialRef', raster.spatialReference.name
print 'min', raster.minimum
print 'max', raster.maximum
