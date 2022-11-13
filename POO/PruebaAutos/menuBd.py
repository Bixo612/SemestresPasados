from ast import Delete
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="concesionario"
    )

cursor = con.cursor()

def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

class Vehiculo():
    def __init__(self,patente,marca,modelo,anio) -> None:
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    def get_patente(self):
        return self.__patente

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__anio

    def set_patente(self,patente):
        self.__patente = patente

    def set_marca(self,marca):
        self.__marca = marca

    def set_modelo(self,modelo):
        self.__modelo = modelo

    def set_anio(self,anio):
        self.__anio = anio
    
    def __str__(self) -> str:
        return "{} - {} {} - {}".format(self.get_patente(),self.get_marca(),self.get_modelo(),self.get_anio())

class FxSql():

    def registrar_vehiculos(auto):
        sql = "Insert into vehiculos values(%s,%s,%s,%s)"
        var = (auto.get_patente(),auto.get_marca(),auto.get_modelo(),auto.get_anio(),)
        cursor.execute(sql,var)
    
    def listar_vehiculos():
        cursor.execute("Select * from vehiculos order by 1")
        resultado = cursor.fetchall()
        for x in resultado:
            print (x)

    def borrar_vehiculo(patente):
        sql = "Delete from vehiculos where vehiculos.patente = %s"
        var = (patente,)
        cursor.execute(sql,var)

    def buscar_vehiculo(patente):
        #Esta funcion busca un vehiculo por patente y crea un objeto con los datos
        sql = "Select * from vehiculos where patente = %s"
        var = (patente,)
        cursor.execute(sql,var)
        resultado = cursor.fetchall()
        #el resultado es una tupla dentro de una lista y con la siguente linea lo extremos
        tupla = resultado[0]
        #de esta manera podermos asiganar los elementos de la tupla a un objeto
        auto = Vehiculo(tupla[0],tupla[1],tupla[2],tupla[3])
        return auto
# Menu

def printMenu():
    print("Menu")
    print("0 - Salir")
    print("1 - Listar vehiculos")
    print("2 - Agregar vehiculo")
    print("3 - Editar vehiculo")
    print("4 - Borrar vehiculo")
    print("->")


def menu():

    exit = True
    while exit:
        op = None
        printMenu()
        op = leerEntero("Ingrese una opcion:")
        if op == 0:
            exit = False
            print("Hasta pronto")
            input("")
        elif op == 1:
            print("FUNCION DE LISTAR")
        elif op == 2:
            print("FUNCION DE AGREGAR")
        elif op == 3:
            print("FUNCION DE EDITAR")
        elif op == 4:
            print("FUNCION DE BORRAR")
        else:
            print("Funcion invalida :/")

# print("**----------------------------------**")
# x = FxSql.buscar_vehiculo("SDGT69")
# print(x.__str__())
# print("**----------------------------------**")

# x = input("->")