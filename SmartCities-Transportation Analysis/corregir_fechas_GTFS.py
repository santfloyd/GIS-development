# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:19:12 2019

@author: ASUS
"""

import pandas as pd

df=pd.read_csv('gtfs_bogota_calendar_dates.csv')
df['date']=df['date'].apply(lambda x: x.replace(',',''))
#df['date'] =  pd.to_datetime(df['date'])
print(df)

df.to_csv('gtfs_bogota_calendar_dates_corregido')