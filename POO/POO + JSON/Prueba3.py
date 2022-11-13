import json
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="argonautas"
    )

cursor = con.cursor()



class Agronauta():

    def __init__(self,rut,nombre,cargo,edad):
        self.rut = rut
        self.nombre = nombre
        self.cargo = cargo
        self.edad = edad
    
    def getRut(self):
        return self.rut

    def getNombre(self):
        return self.nombre

    def getCargo(self):
        return self.cargo
    
    def getEdad(self):
        return self.edad

    def editRut(self,rut):
        self.rut = rut

    def editNombre(self,nombre):
        self.nombre = nombre

    def editCargo(self,cargo):
        self.cargo = cargo

    def editEdad(self,edad):
        self.edad = edad

    def estaRegistrado(self):
        sql = "Select rut from argonauta where rut = %s"
        var = (self.rut,)
        cursor.execute(sql,var)
        res = cursor.fetchone()
        if res == self.rut:
            return True
        else:
            return False

    def registrarBd(self):
        sql = "Insert into argonauta values (%s,%s,%s,%s)"
        var = (self.rut,self.nombre,self.cargo,self.edad,)
        cursor.execute(sql,var)

    # def guardarRegistro(self):
    #     if estaRegistrado():

    #     pass

    def buscarBd(self,rut):
        sql = "Select * from argonauta where rut = %s"
        val = (rut,)
        cursor.execute(sql,val)
        resultado = cursor.fetchone()
        self.rut = resultado[0]
        self.nombre = resultado[1]
        self.cargo = resultado[2]
        self.edad = resultado[3]

    def __str__(self) -> str:
        return "Rut {} | Nombre {} | Cargo {} | Edad {}".format(self.getRut(),self.getNombre(),self.getCargo(),self.getEdad())
    
    def returnJson(self):
        jsonResult = json.dumps(self.__dict__)
        return jsonResult

x = Agronauta("17","Tarma","Grumete",25)
x.guardarRegistro()







