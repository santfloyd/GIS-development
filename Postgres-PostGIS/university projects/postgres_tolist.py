# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:41:14 2022

@author: Usuario
"""

import psycopg2
t_host = "localhost"
t_port = "5433"
t_dbname = "proyecto"
t_user = "postgres"
t_pw = "postgres"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()

query = "select distinct(oneway) from saoh2.tramo_vial"
db_cursor.execute(query)
list_users = db_cursor.fetchall()


cleaned=[str(i[0]) for i in list_users]

    
print(cleaned)
