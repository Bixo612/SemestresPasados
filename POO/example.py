class Persona():

    def __init__(self,rut,nombre,edad):
        self.__rut      = rut
        self.__nombre   = nombre
        self.__edad     = edad
    
    def get_nombre(self):
        return self.__nombre

    def get_rut(self):
        return self.__rut
    
    def get_edad(self):
        return self.__edad

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_rut(self,rut):
        self.__rut = rut

    def set_edad(self,edad):
        self.__edad = edad
        
    def __str__(self):
        return "Nombre {}, {} rut, edad {} Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), type(self).__name__)

    def __str__(self):
        return "{}".format(type(self))

