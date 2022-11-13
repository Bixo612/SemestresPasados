import mysql.connector

con = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="")


#https://www.w3schools.com/python/python_mysql_getstarted.asp


class Vendedor():

    def __init__(self,nombre,edad,sexo,rut):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.rut = rut

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_edad(self,edad):
        self.edad = edad

    def set_sexo(self,sexo):
        self.edad = sexo
    
    def set_rut(self,rut):
        self.rut = rut

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_sexo(self):
        return self.sexo

    def get_rut(self):
        return self.rut

    def __str__(self) -> str:
        pass

class zapato():
    
    def __init__(self,codigo,descripcion,precio,cantidad):
        self.codigo = codigo
        self.descripcio =  descripcion
        self.precio = precio
        self.cantidad = cantidad
    


