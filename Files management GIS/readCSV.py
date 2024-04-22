# -*- coding: utf-8 -*-
"""
Created on Thu May 03 12:51:17 2018

@author: ASUS
"""

import csv
f=open('bc_pop1996.csv','r')
#bloque try con un objeto iterador y la loop
try:
    csvReader=csv.reader(f)
    for row in csvReader:
        print row
finally:
    f.close()
#para omitir los encabezados
f=open('bc_pop1996.csv','r')
#bloque try con un objeto iterador y la loop
try:
    csvReader=csv.reader(f)
    for row in csvReader:
        if row[2] != 'name':
            print "texto" + row[2] + row[2] + "texto" + str(row[2])
finally:
    f.close()
#para escribir un csv

#lista con listas de valores a insertar
lstCityPops = [ [1,"Vancouver",642849], [2,"Surrey",462905], [3,"Burnaby",227389], [4,"Richmond",196858], [5,"North Vancouver",139095], [6,"Abbotsford",138179],[7,"Langley",130555],[8,"Coquitlam",126594],[9,"Keowna",121306],[10,"Saanich",114140]]
f=open('bc_pop1996.csv','a')
try:
    writer=csv.writer(f)
    writer.writerow(('id','city','population'))
    for valor in lstCityPops:
        valor1=lstCityPops[0]
        valor2=lstCityPops[1]
        valor3=lstCityPops[2]
        writer.writerow((valor1,valor2,valor3))
finally:
    print "csv wroten"
    f.close()
        

