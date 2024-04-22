# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:05:03 2018

@author: ASUS
"""

import shelve

lstCityPops=[["Vancouver",224008, 642843],["Surrey", 589632, 548965]]
#crea el .dat
db=shelve.open('bc_population.dat','n')
try:
    for lstCityValues in lstCityPops:
        city=lstCityValues[0]
        pop1996=lstCityValues[1]
        pop2010=lstCityValues[2]
        #crea el diccionario para  iterrar los valores en la lista lscitypops e ir insertando 
        dictpop={"1996":pop1996, "2010":pop2010}
        db[city]=dictpop
finally:
    print "population data writen"
    db.close()

