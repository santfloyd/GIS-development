import anydbm

f = open("states.txt", 'r')
#crear el archivo con el nombre pasado como primer parametro con el modo "c"
stateDB = anydbm.open('states.dbm', 'c')
states=f.readlines()
#loop para crear lista leyendo por cada linea y asignar valor a variables que luego se comportarán como dict
for line in states: 
    listValues=line.split(",")
    statename=listValues[0]
    print statename
    stateAbbrev=listValues[1]
    print stateAbbrev
    #añade valores de la lista al archivo .dbm creado antes en forma de dict
    stateDB[statename]=stateAbbrev

f.close()
stateDB.close()

for key in stateDB.keys():
    print (stateDB[key])