'''
Clase con parametros para inicializar la conexion
'''



#Clase que contiene como atributos los valores que por defecto usará el constructor

class Settings:
    USER='postgres'
    PASSWORD='postgres'
    HOST='localhost'
    PORT='5432'
    DATABASE='PROJDSIG'
    #crear el constructor de la clase y admite un parametro database
    #para solo indicar la base de datos cuando se intente la conexion
    def __init__(self, database=None):
        self.user=Settings.USER
        self.password=Settings.PASSWORD
        self.host=Settings.HOST
        self.port=Settings.PORT
        if database == None:
            self.database=Settings.DATABASE
        else:
            self.database=database
    
    
        
