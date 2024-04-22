# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:27:48 2019

@author: ASUS
"""

#importar librerias necesarias para cargar el archivo, convertirlo a un marco de datos espacial y crear las geometrias de punto
import pandas as pd
#from sqlalchemy import create_engine 
import numpy as np
import geopandas as gpd 
from shapely.geometry import Point
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',100)
pd.set_option('display.max_colwidth',500)
pd.options.display.max_rows = 999

#%%
#engine = create_engine('postgresql://postgres:POSTGRES@localhost:5432/postgres')


Hora_inicio=['00:00:00','04:00:00','06:00:00','09:00:00','15:00:00','19:00:00','23:00:00','04:00:00','08:00:00','20:00:00','00:00:00','05:00:00','09:00:00','18:00:00']
Hora_final=['03:59:00','05:59:00','08:59:00','14:59:00','18:59:00','22:59:00','03:59:00','07:59:00','19:59:00','23:59:00','04:59:00','08:59:00','17:59:00','23:59:00']
Periodo=['Tarde en la noche','temprano','hora pico mañana','medio día','hora pico tarde','noche','Tarde en la noche','Sabado mañana','Sabado medio día','Sabado noche','Domingo noche','Domingo mañana','Domingo medio día','Domingo noche']
Dia_semana=['entre semana','entre semana','entre semana','entre semana','entre semana','entre semana','entre semana','Sabado','Sabado','Sabado','Domingo','Domingo','Domingo','Domingo']
lapso=[1,2,3,6,4,4,1,4,12,4,7,4,9,7]
df0=pd.DataFrame()
df0['Hora_inicio'] = pd.Series(Hora_inicio)
df0['Hora_final'] = pd.Series(Hora_final)
df0['Periodo'] = pd.Series(Periodo)
df0['Dia_semana'] = pd.Series(Dia_semana)
df0['lapso'] = pd.Series(lapso)
time_format = '%H:%M:%S'
df0['Hora_inicio']=pd.to_timedelta(df0['Hora_inicio']) #, unit='s'
df0['Hora_final']=pd.to_timedelta(df0['Hora_final']) #, unit='s'
#df0.to_sql(name='inputs', con=engine, if_exists='replace',index=True)	


df=pd.read_csv("agency.txt",sep=',')
#df.to_sql(name='gtfs_bogota_agency', con=engine, if_exists='replace',index=True)



df1=pd.read_csv('calendar.txt',sep=',')
tipo_dia=['entre semana','Domingo','entre semana','entre semana','entre semana','Sabado']
df1['tipo_dia']=pd.Series(tipo_dia)
#df1.to_sql(name='gtfs_bogota_calendar', con=engine, if_exists='replace',index=True)



df2=pd.read_csv("calendar_dates.txt",sep=',')
#df2.to_sql(name='gtfs_bogota_calendar_dates', con=engine, if_exists='replace',index=True)


df3=pd.read_csv("routes.txt",sep=',',dtype={'route_short_name':object})
df3['agency_id']=df3['agency_id'].astype(str)
df3['route_type']=df3['route_type'].astype(str)
df3['route_short_name']=df3['route_short_name'].astype(object)

#df3.to_sql(name='gtfs_bogota_routes', con=engine, if_exists='replace',index=True)
#%%
df4=pd.read_csv("shapes.txt",sep=',')

#df4.to_sql(name='gtfs_bogota_shapes', con=engine, if_exists='replace',index=True)
#%%
df6=pd.read_csv("stops.txt",sep=',')
df6.head()
#df6.to_sql(name='gtfs_bogota_stops', con=engine, if_exists='replace',index=True)

#%%
df6['stop_lat'] = df6['stop_lat'].astype(str)
df6['stop_lon'] = df6['stop_lon'].astype(str)

df6['stop_lat'] = df6['stop_lat'].str.replace('.','')
df6['stop_lat'] = (df6['stop_lat'].str[:1] + '.' + df6['stop_lat'].str[1:]).astype(float)

df6['stop_lon'] = df6['stop_lon'].str.replace('.','')
df6['stop_lon'] = (df6['stop_lon'].str[:3] + '.' + df6['stop_lon'].str[3:]).astype(float)

print(df6['stop_lat'].head())
print(df6['stop_lon'].head())
#%%
df6.to_excel("stops.xls",sheet_name='Stops')

df6['geometry'] = df6.apply(lambda x: Point(float(x.stop_lon), float(x.stop_lat)), axis=1)
print(df6['geometry'])
crs={'init': 'epsg:4326'}
df6_geo = gpd.GeoDataFrame(df6,crs =crs, geometry = df6.geometry)
print(df6_geo.crs)
print(type(df6_geo))
print(df6_geo['geometry'])
df6_geo.to_file("stops_from_stops_table.shp")
#%%

df7=pd.read_csv("trips.txt",sep=',')
df7=pd.merge(df7,df3[['route_id','route_short_name']],left_on=['route_id'], right_on = ['route_id'], how = 'left')
df7=pd.merge(df7,df1[['service_id','tipo_dia']],left_on=['service_id'], right_on = ['service_id'], how = 'left')

print(df7.head())
#%%
shapes_attributes=df7.groupby(['shape_id','route_short_name'])['trip_headsign'].unique().reset_index()
shapes_attributes=pd.DataFrame(shapes_attributes)
shapes_attributes.to_excel("shapes_attributes.xls",sheet_name='shapes_attributes')
print(shapes_attributes)

#df7.to_sql(name='gtfs_bogota_trips', con=engine, if_exists='replace',index=True)

#%%
df5=pd.read_csv("stop_times.txt",sep=',')
df5['arrival_time']=pd.to_timedelta(df5['arrival_time'])#, unit='s'
df5['departure_time']=pd.to_timedelta(df5['departure_time']) #, unit='s'
df5=pd.merge(df5,df7[['trip_id','route_short_name','service_id','tipo_dia','shape_id','trip_headsign']],left_on=['trip_id'], right_on = ['trip_id'], how = 'left')
df5=pd.merge(df5,df6[['stop_id',' stop_name','stop_lon','stop_lat']],left_on=['stop_id'], right_on = ['stop_id'], how = 'left')

print(df5.head())


conditions = [
            (df5['tipo_dia'] == 'entre semana') & (df5['arrival_time'] >= df0.loc[0,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[0,'Hora_final']),
            (df5['tipo_dia'] == 'entre semana') & (df5['arrival_time'] >= df0.loc[1,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[1,'Hora_final']),
            (df5['tipo_dia'] == 'entre semana') & (df5['arrival_time'] >= df0.loc[2,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[2,'Hora_final']),
            (df5['tipo_dia'] == 'entre semana') & (df5['arrival_time'] >= df0.loc[3,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[3,'Hora_final']),
            (df5['tipo_dia'] == 'entre semana') & (df5['arrival_time'] >= df0.loc[4,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[4,'Hora_final']),
            (df5['tipo_dia'] == 'entre semana') & (df5['arrival_time'] >= df0.loc[5,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[5,'Hora_final']),
            (df5['tipo_dia'] == 'entre semana') & (df5['arrival_time'] >= df0.loc[6,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[6,'Hora_final']),
            (df5['tipo_dia'] == 'Sabado') & (df5['arrival_time'] >= df0.loc[7,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[7,'Hora_final']),
            (df5['tipo_dia'] == 'Sabado') & (df5['arrival_time'] >= df0.loc[8,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[8,'Hora_final']),
            (df5['tipo_dia'] == 'Sabado') & (df5['arrival_time'] >= df0.loc[9,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[9,'Hora_final']),
            (df5['tipo_dia'] == 'Domingo') & (df5['arrival_time'] >= df0.loc[10,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[10,'Hora_final']),
            (df5['tipo_dia'] == 'Domingo') & (df5['arrival_time'] >= df0.loc[11,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[11,'Hora_final']),
            (df5['tipo_dia'] == 'Domingo') & (df5['arrival_time'] >= df0.loc[12,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[12,'Hora_final']),
            (df5['tipo_dia'] == 'Domingo') & (df5['arrival_time'] >= df0.loc[13,'Hora_inicio']) & (df5['arrival_time'] <= df0.loc[13,'Hora_final']),
            
            ]   
choices = [df0.loc[0,'Periodo'],df0.loc[1,'Periodo'],df0.loc[2,'Periodo'],df0.loc[3,'Periodo'],df0.loc[4,'Periodo'],df0.loc[5,'Periodo'],df0.loc[6,'Periodo'],df0.loc[7,'Periodo'],df0.loc[8,'Periodo'],df0.loc[9,'Periodo'],
           df0.loc[10,'Periodo'],df0.loc[11,'Periodo'],df0.loc[12,'Periodo'],df0.loc[13,'Periodo']]
df5['Periodo'] = np.select(conditions, choices)
print(df5.head(100))

time_format = '%H:%M:%S'
df_freq=df5.copy()


#df_freq['arrival_time'] = df_freq['arrival_time'].astype('datetime64[ns]')

#1 munito
df_freq=df_freq.set_index(['arrival_time']).resample('1T')
df_freq.size().plot()


xlab = 'Horas'
ylab = 'Número de viajes'
title = 'Viajes por minuto'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.savefig('Viajes_frecuencia.jpg',dpi=450, bbox_inches='tight')
plt.show()


#%%

frequencies_rutas=df5.groupby(['route_short_name'])['trip_id'].nunique().to_frame().reset_index()
print(frequencies_rutas.head())
frequencies_rutas.to_excel("frequencies_rutas.xls",sheet_name='frequencies')
#df5.to_sql(name='gtfs_bogota_stop_times', con=engine, if_exists='replace',index=True)
#%%
#por la cantidad de registros debe ser xlsx y no xls
#df5.to_excel("stop_squence_pivot.xlsx",sheet_name='stop_sequence')

freq=df5.groupby(['route_short_name','tipo_dia']).agg({'arrival_time':'min', 'departure_time':'max'})[['arrival_time','departure_time']].reset_index()
print(freq.head())

freq.to_excel("frequencies.xls",sheet_name='freq')
#%%
rutas_shape=pd.pivot_table(df5,columns=['route_short_name','shape_id','trip_headsign','stop_id','stop_sequence',' stop_name','stop_lon','stop_lat']).to_frame()
rutas_shape.to_csv("rutas_shape.csv")
rutas_shape=pd.read_csv("rutas_shape.csv")
rutas_shape.to_excel("rutas_shape.xls",sheet_name='rutas_shape')
rutas_shape=pd.read_excel("rutas_shape.xls")
print(rutas_shape.head(50))

rutas_shape['geometry'] = rutas_shape.apply(lambda x: Point(float(x.stop_lon), float(x.stop_lat)), axis=1)
print(rutas_shape['geometry'])
crs={'init': 'epsg:4326'}
rutas_shape_geo = gpd.GeoDataFrame(rutas_shape,crs =crs, geometry = rutas_shape.geometry)
print(rutas_shape_geo.crs)
print(type(rutas_shape_geo))
print(rutas_shape_geo['geometry'])
rutas_shape_geo.to_file("rutas_shape.shp")