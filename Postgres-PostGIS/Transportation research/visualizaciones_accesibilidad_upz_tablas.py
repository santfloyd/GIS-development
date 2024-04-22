# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:01:06 2020

@author: ASUS
"""

#importar librerias necesarias para cargar el archivo, convertirlo a un marco de datos espacial y crear las geometrias de punto
import pandas as pd
#from sqlalchemy import create_engine 
import numpy as np
import geopandas as gpd 
from shapely.geometry import Point
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',100)
pd.set_option('display.max_colwidth',500)
pd.options.display.max_rows = 999

#%%
paraderos=gpd.read_file('paraderos_isai_asai.shp')
print(paraderos.columns)
UPZ=gpd.read_file('UPZ.shp')
print(UPZ.columns)
#%%
print('paradero crs:', paraderos.crs)
print('UPZ crs:',UPZ.crs)
#%%
UPZ_paraderos = gpd.sjoin(paraderos, UPZ, op = "within")
print(UPZ_paraderos.head())
print(UPZ_paraderos.columns)
print(UPZ_paraderos.crs)

#%%
#Promedio_ISAI_ASAI_UPZ=UPZ_paraderos.groupby(['upz','NOMBRE']).agg({'ISAI':'mean','ASAI':'mean'})
Promedio_ISAI_ASAI_UPZ=UPZ_paraderos.groupby('upz').agg({'ISAI':'mean','ASAI':'mean'})
Promedio_ISAI_ASAI_UPZ=Promedio_ISAI_ASAI_UPZ.reset_index()
#%%
Promedio_ISAI_UPZ=Promedio_ISAI_ASAI_UPZ.sort_values('ISAI',ascending=True)
Promedio_ISAI_UPZ=Promedio_ISAI_UPZ.reset_index(drop=True)
print(Promedio_ISAI_UPZ.head(15))
#Promedio_ISAI_UPZ.to_excel('Promedio_ISAI_UPZ.xls')
print(Promedio_ISAI_UPZ['ISAI'].min())
#%%
Promedio_ASAI_UPZ=Promedio_ISAI_ASAI_UPZ.sort_values('ASAI',ascending=True)
Promedio_ASAI_UPZ=Promedio_ASAI_UPZ.reset_index(drop=True)
print(Promedio_ASAI_UPZ.head(15))
#%%

sns.barplot('upz','ISAI',data=Promedio_ISAI_UPZ,order=Promedio_ISAI_UPZ['upz'])
sns.dark_palette("purple")
plt.title('Promedio de índice ISAI a paraderos de autobús por UPZ',fontsize=18,color='navy')
plt.xlabel('Código UPZ',fontsize=10,color='black')
plt.ylabel('Índice de Accesibilidad Ideal',fontsize=14,color='black')
#plt.xlim(0,25)
plt.yticks(fontsize=9)
plt.xticks(rotation=90,fontsize=9)
#optimiza el espacio
plt.tight_layout()

plt.show()
#%%
sns.barplot('upz','ASAI',data=Promedio_ASAI_UPZ,order=Promedio_ASAI_UPZ['upz'])
sns.dark_palette("green")
plt.title('Promedio de índice ASAI a paraderos de autobús por UPZ',fontsize=18,color='navy')
plt.xlabel('Código UPZ',fontsize=14,color='darkolivegreen')
plt.ylabel('Índice de Accesibilidad Efectiva',fontsize=14,color='darkolivegreen')
#plt.xlim(0,25)
plt.yticks(fontsize=9)
plt.xticks(rotation=90,fontsize=9)
#optimiza el espacio
plt.tight_layout()
plt.show()

#%%
Localidades=gpd.read_file('localidades.shp')
rutas_cortas=gpd.read_file('Rutas_cortas.shp')
rutas_largas=gpd.read_file('rutas_largas.shp')
print('Localidades crs:',Localidades.crs)
print('rutas_cortas crs:',rutas_cortas.crs)
print('rutas_largas crs:',rutas_largas.crs)
#%%
Localidades_rutas_cortas = gpd.sjoin(rutas_cortas, Localidades, op = "intersects")
print(Localidades_rutas_cortas.head(50))
print(Localidades_rutas_cortas.columns)
print(Localidades_rutas_cortas.crs)
print(Localidades_rutas_cortas.shape)

#%%
Localidades_rutas_cortas_=Localidades_rutas_cortas.groupby('NOMBRE').agg({'route_shor':"nunique"})
Localidades_rutas_cortas_=Localidades_rutas_cortas_.reset_index()
print(Localidades_rutas_cortas_.shape)
print(Localidades_rutas_cortas_)

#%%
Localidades_rutas_largas = gpd.sjoin(rutas_largas, Localidades, op = "intersects")
print(Localidades_rutas_largas.head())
print(Localidades_rutas_largas.columns)
print(Localidades_rutas_largas.crs)
#%%
Localidades_rutas_largas_=Localidades_rutas_largas.groupby('NOMBRE').agg({'route_shor':"nunique"})
Localidades_rutas_largas_=Localidades_rutas_largas_.reset_index()
print(Localidades_rutas_largas_.shape)
print(Localidades_rutas_largas_)
#%%

rutas_localidades_consolidado=Localidades_rutas_largas_.merge(Localidades_rutas_cortas_,on='NOMBRE')
print(rutas_localidades_consolidado)
#%%
rutas_localidades_consolidado.to_excel('rutas_localidades_consolidado.xls')
#%%
Localidades_paraderos = gpd.sjoin(paraderos, Localidades, op = "within")
print(Localidades_paraderos.head())
print(Localidades_paraderos.columns)
print(Localidades_paraderos.crs)
#%%
print(Localidades_paraderos['NOMBRE'].nunique())
#%%
Promedio_ISAI_ASAI_Localidades=Localidades_paraderos.groupby(['CODIGO_LOC','NOMBRE']).agg({'ISAI':'mean','ASAI':'mean'})
Promedio_ISAI_ASAI_Localidades=Promedio_ISAI_ASAI_Localidades.reset_index()
print(Promedio_ISAI_ASAI_Localidades.shape)
Promedio_ISAI_ASAI_Localidades.to_excel('Promedio_ISAI_ASAI_Localidade.xls')
#%%
Promedio_ISAI_Localidades=Promedio_ISAI_ASAI_Localidades.sort_values('ISAI',ascending=True)
Promedio_ISAI_Localidades=Promedio_ISAI_Localidades.reset_index(drop=True)
print(Promedio_ISAI_Localidades.head())
#Promedio_ISAI_UPZ.to_excel('Promedio_ISAI_UPZ.xls')
print(Promedio_ISAI_Localidades['ISAI'].min())
#%%
Promedio_ASAI_Localidades=Promedio_ISAI_ASAI_Localidades.sort_values('ASAI',ascending=True)
Promedio_ASAI_Localidades=Promedio_ASAI_Localidades.reset_index(drop=True)
print(Promedio_ASAI_Localidades.head())

#%%
sns.barplot('CODIGO_LOC','ISAI',data=Promedio_ISAI_Localidades,order=Promedio_ISAI_Localidades['CODIGO_LOC'])
sns.light_palette("green")
plt.title('Promedio de índice ISAI a paraderos de autobús por Localidad',fontsize=18,color='navy')
plt.xlabel('Código Localidad',fontsize=10,color='black')
plt.ylabel('Índice de Accesibilidad Ideal',fontsize=14,color='black')
#plt.xlim(0,25)
plt.yticks(fontsize=9)
plt.xticks(rotation=70,fontsize=9)
#optimiza el espacio
plt.tight_layout()

plt.show()

#%%
sns.barplot('CODIGO_LOC','ASAI',data=Promedio_ASAI_Localidades,order=Promedio_ASAI_Localidades['CODIGO_LOC'])
sns.dark_palette("green")
plt.title('Promedio de índice ASAI a paraderos de autobús por Localidad',fontsize=18,color='navy')
plt.xlabel('Código Localidad',fontsize=14,color='darkolivegreen')
plt.ylabel('Índice de Accesibilidad Efectiva',fontsize=14,color='darkolivegreen')
#plt.xlim(0,25)
plt.yticks(fontsize=9)
plt.xticks(rotation=70,fontsize=9)
#optimiza el espacio
plt.tight_layout()
plt.show()