# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:01:06 2020

@author: ASUS
"""
#para instalar geopandas toca instalar manualmente las librerias gdal, pyproj, fiona, shapely y geopandas de la pagina
#de python binaries para windows
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
#para la tesis smart cities ya tengo los indicadores pero por upz, lo hare con esa capa
zat_indi=gpd.read_file('zat_indicadores.shp')
print(zat_indi.columns)

#%%
Promedio_ISAI_zat=zat_indi.sort_values('promedio_i',ascending=True)
Promedio_ISAI_zat=Promedio_ISAI_zat.reset_index(drop=True)
print(Promedio_ISAI_zat.head(15))
#Promedio_ISAI_UPZ.to_excel('Promedio_ISAI_UPZ.xls')
print(Promedio_ISAI_zat['promedio_i'].min())
#%%
Promedio_ASAI_zat=zat_indi.sort_values('promedio_a',ascending=True)
Promedio_ASAI_zat=Promedio_ASAI_zat.reset_index(drop=True)
print(Promedio_ASAI_zat.head(15))
#%%

sns.barplot(x='zat',y='promedio_i',data=Promedio_ISAI_zat,order=Promedio_ISAI_zat['zat'])
sns.dark_palette("purple")
plt.title('Promedio de índice ISAI a paraderos de autobús por ZAT',fontsize=18,color='navy')
plt.xlabel('Código ZAT',fontsize=10,color='black')
plt.ylabel('Índice de Accesibilidad Ideal',fontsize=14,color='black')
#plt.xlim(0,25)
plt.yticks(fontsize=9)
plt.xticks(rotation=90,fontsize=2)
#optimiza el espacio
plt.tight_layout()

plt.show()
#%%
sns.barplot(x='zat',y='promedio_a',data=Promedio_ASAI_zat,order=Promedio_ASAI_zat['zat'])
sns.dark_palette("green")
plt.title('Promedio de índice ASAI a paraderos de autobús por ZAT',fontsize=18,color='navy')
plt.xlabel('Código ZAT',fontsize=14,color='darkolivegreen')
plt.ylabel('Índice de Accesibilidad Efectiva',fontsize=14,color='darkolivegreen')
#plt.xlim(0,25)
plt.yticks(fontsize=9)
plt.xticks(rotation=90,fontsize=2)
#optimiza el espacio
plt.tight_layout()
plt.show()


