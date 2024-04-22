for provider in QgsProviderRegistry.instance().providerList():
    print(provider)
    #gdal para rasters
    #ogr para vectoriales
    #postgres para postgres