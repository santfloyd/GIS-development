# -*- coding: utf-8 -*-
"""
Created on Thu May 23 08:08:42 2019

@author: ASUS
"""

import pandas as pd
import geopandas as gpd 
from shapely.geometry import Point

df=pd.read_csv('movilidad_2015.csv')

pd.set_option('display.max_columns',100)
pd.set_option('display.max_colwidth',500)
pd.options.display.max_rows = 999

df=df.drop(['FACTOR_AJUSTE',
       'PONDERADOR_CALIBRADO', 'DIA_HABIL', 'DIA_NOHABIL', 'PICO_HABIL',
       'PICO_NOHABIL', 'VALLE_NOHABIL', 'VALLE_HABIL', 'PI_K_I', 'PI_K_II',
       'PI_K_III', 'FE_TOTAL', 'FACTOR_AJUSTE_TRANSMILENIO',
       'PONDERADOR_CALIBRADO_VIAJES'], axis=1)
print(df.columns)
print(df.shape)
print(df.head())

subdf=df[['MEDIO_PREDOMINANTE']]
counts_subdf=subdf.apply(pd.value_counts)
subdf= counts_subdf.fillna(0)
subdf['Medio'] = subdf.index
subdf.reset_index(inplace = True)
subdf = subdf[['Medio','MEDIO_PREDOMINANTE']]

print(subdf.sort_values(by=['MEDIO_PREDOMINANTE'], ascending=False).head(10))

subdf1=df[['ZAT_ORIGEN']]
counts_subdf1=subdf1.apply(pd.value_counts)
subdf1= counts_subdf1.fillna(0)
subdf1['zat'] = subdf1.index
subdf1.reset_index(inplace = True)
subdf1 = subdf1[['zat','ZAT_ORIGEN']]

print(subdf1.sort_values(by=['ZAT_ORIGEN'], ascending=False).head(10))

subdf2=df[['ZAT_DESTINO']]
counts_subdf2=subdf2.apply(pd.value_counts)
subdf2= counts_subdf2.fillna(0)
subdf2['zat'] = subdf2.index
subdf2.reset_index(inplace = True)
subdf2 = subdf2[['zat','ZAT_DESTINO']]

print(subdf2.sort_values(by=['ZAT_DESTINO'], ascending=False).head(10))
#es importante que las coordenadas sean escritas con punto flotante o habrá problemas para representar
df['LONGITUD_ORIGEN'] = df['LONGITUD_ORIGEN'].astype(str)
df['LONGITUD_ORIGEN'] = (df['LONGITUD_ORIGEN'].str[:3] + '.' + df['LONGITUD_ORIGEN'].str[3:]).astype(float)
print(df['LONGITUD_ORIGEN'])
df['LATITUD_ORIGEN'] = df['LATITUD_ORIGEN'].astype(str)
df['LATITUD_ORIGEN'] = (df['LATITUD_ORIGEN'].str[:1] + '.' + df['LATITUD_ORIGEN'].str[1:]).astype(float)
print(df['LATITUD_ORIGEN'])


df['geometry'] = df.apply(lambda x: Point(float(x.LONGITUD_ORIGEN), float(x.LATITUD_ORIGEN)), axis=1)
print(df['geometry'])
crs={'init': 'epsg:4326'}
df_geo = gpd.GeoDataFrame(df,crs =crs, geometry = df.geometry)
print(df_geo.crs)
print(type(df_geo))
print(df_geo['geometry'])
df_geo.to_file("Origen_viajes.shp")



#df_geo.to_file(driver = 'ESRI Shapefile', filename= "Origen_viajes.shp")
#df_geo1.to_file(driver = 'ESRI Shapefile', filename= "Destino_viajes.shp")

df1=df

df1['LONGITUD_DESTINO'] = df1['LONGITUD_DESTINO'].astype(str)
df1['LONGITUD_DESTINO'] = (df1['LONGITUD_DESTINO'].str[:3] + '.' + df1['LONGITUD_DESTINO'].str[3:]).astype(float)
print(df1['LONGITUD_ORIGEN'])
df1['LATITUD_DESTINO'] = df1['LATITUD_DESTINO'].astype(str)
df1['LATITUD_DESTINO'] = (df1['LATITUD_DESTINO'].str[:1] + '.' + df1['LATITUD_DESTINO'].str[1:]).astype(float)
print(df1['LATITUD_DESTINO'])



df1['geometry'] = df1.apply(lambda x: Point(float(x.LONGITUD_DESTINO), float(x.LATITUD_DESTINO)), axis=1)
df_geo1 = gpd.GeoDataFrame(df1,crs =crs, geometry = df1.geometry)
print(df_geo1.crs)
print(type(df_geo1))
df_geo1.to_file("Destino_viajes.shp")