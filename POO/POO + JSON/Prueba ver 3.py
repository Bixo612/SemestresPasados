import json
import mysql.connector

#Vicente Vasquez Galvez 19360397-1

# Fila que se debe agregar a la bd necesaria para el funcionamiento de este programa

#ALTER TABLE `argonauta` ADD `rut` VARCHAR(10) NOT NULL FIRST, ADD PRIMARY KEY (`rut`); 

def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="argonautas"
    )

cursor = con.cursor()

class FxSql():

    def registrarBd(rut,nombre,cargo,edad):
        sql = "Insert into argonauta values (%s,%s,%s,%s)"
        var = (rut,nombre,cargo,edad,)
        cursor.execute(sql,var)

    def existeRut(rut): 
        sql = "Select rut from argonauta where rut = %s"
        var = (rut,)
        cursor.execute(sql,var)
        res = cursor.fetchone()
        if res == None:
            return False
        else:
            res = res[0]
            if res == rut:
                return True
            else:
                return False

    def selectArgonauta(rut):
        sql = "Select * from argonauta where rut = %s"
        val = (rut,)
        cursor.execute(sql,val)
        resultado = cursor.fetchone()
        return resultado

    def eliminarArgonauta(rut):
        sql = "Delete from argonauta where rut = %s"
        var = (rut,)
        cursor.execute(sql,var)

    def totalRegistros():
        sql = "Select count(*) from argonauta"
        cursor.execute(sql)
        res = cursor.fetchone()
        return res[0]

    def selectAll():
        sql = "Select * from argonauta"
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

class Validaciones():

    def crearRut():
        rut = ""
        while len(rut) == 0 or len(rut) > 10:
            rut = input ("Ingrese el rut del argonauta: ")
            if len(rut) == 0 or len(rut) > 10:
                print ("Rut invalido")
        return rut

    def leerStringConLimite(txt,limit):
        string = ""
        while len(string) == 0 or len(string)>=limit:
            string = input (txt)
            if len(string) == 0 or len(string)>=limit:
                print ("dato no valido")
        return string  

    def asignarEdad():
        edad = None
        while edad == None:
            edad = leerEntero("Ingrese la edad: ") 
            if edad == None:
                print("Formato Invalido intentelo nuevamente")
        return edad

class Argonauta():

    def __init__(self,Vjason):
        argo = json.loads(Vjason)
        self.rut = argo["rut"]
        self.nombre = argo["nombre"]
        self.cargo = argo["cargo"]
        self.edad = argo["edad"]
    
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

    def guardarRegistro(self):
        if FxSql.existeRut(self.rut):
            print ("No se pudo registrar, rut existente en Bd")
        else:
            FxSql.registrarBd(self.rut,self.nombre,self.cargo,self.edad)
            print ("Argonauta registrado satisfactoriamente")

    def __str__(self) -> str:
        return "Rut {} | Nombre {} | Cargo {} | Edad {}".format(self.getRut(),self.getNombre(),self.getCargo(),self.getEdad())
    
    def buscarBdgenerateJson(self,rut):
        if FxSql.existeRut(rut):
            print("Existe rut")
            tup = FxSql.selectArgonauta(rut)
            self.rut = tup[0]
            self.nombre = tup[1]
            self.cargo = tup[2]
            self.edad = tup[3]
            jsonResult = json.dumps(self.__dict__)
            res = json.loads(jsonResult)
            print (res)
        else:
            print("No existe el rut")

    def returnJson(self):
        jsonResult = json.dumps(self.__dict__)
        return jsonResult
    
def printMenu():
    print("MENU ARGONAUTAS")
    print("0 - Salir")
    print("1 - Registrar Argonauta")
    print("2 - Buscar Argonauta")
    print("3 - Eliminar Argonauta")

def menu():
    dicc = {
        "rut":"-",
        "nombre":"-",
        "cargo":"-",
        "edad":0
    }
    VJson =  json.dumps (dicc)
    argonauta = Argonauta(VJson)
    salir = True
    op = None
    while salir:
        printMenu()
        op = leerEntero("Ingrese una opcion: ")  
        if op == 0:
            salir = False
            print ("Hasta pronto") 
        if op == 1:
            #Registrar Argonauta
            rut = Validaciones.crearRut()
            nombre = Validaciones.leerStringConLimite("Ingrese el nombre del argonauta (max 100 caracteres): ",100)
            cargo = Validaciones.leerStringConLimite("Ingrese el cargo del argonauta (max 100 caracteres): ",100)
            edad = Validaciones.asignarEdad() 
            diccionario = {
                "rut":rut,
                "nombre":nombre,
                "cargo":cargo,
                "edad":edad
            }
            VJson = json.dumps (diccionario)
            argonauta = Argonauta(VJson)
            argonauta.guardarRegistro()
        if op == 2:
            #Obtener Argonauta
            rt = Validaciones.crearRut()
            argonauta.buscarBdgenerateJson(rt)
        if op == 3:
            #Eliminar astronauta
            rut = Validaciones.crearRut()
            if FxSql.existeRut(rut):
                FxSql.eliminarArgonauta(rut)
                print("Rut",rut,"Eliminado")
            else:
                print("Rut",rut,"No existe en los registros")
        
menu()    

