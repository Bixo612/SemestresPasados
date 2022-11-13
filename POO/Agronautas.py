import json
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="argonautas"
    )

cursor = con.cursor()
print(con)


def agregarArgonauta(nombre,cargo,edad):
    sql = "Insert into argonauta values (%s,%s,%s)"
    var = (nombre,cargo,edad,)
    cursor.execute(sql,var)

agregarArgonauta("Felipe","Grumete",22)

def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

def leerStringConLimite(txt,limit):
    string = ""
    while len(string) == 0 or len(string)>=limit:
        string = input (txt)
        if len(string) == 0 or len(string)>=limit:
            print ("dato no valido")
    return string        





def printMenu():
    print("MENU AGRONAUTAS")
    print("0 - Salir")
    print("1 - Registrar Agronauta")

def menu():
    salir = True
    op = None
    while salir:
        printMenu()
        op = leerEntero("Ingrese una opcion")  
        if op == 0:
            salir = False
            print ("Hasta pronto") 
        if op == 1:
            #Registrar Agronauta
            nombre = leerStringConLimite("Ingrese el nombre del agronauta (max 100 caracteres)",100)
            cargo = leerStringConLimite("Ingrese el cargo del agronauta (max 100 caracteres)",100)
            print (nombre, cargo)                 
###

#menu()
