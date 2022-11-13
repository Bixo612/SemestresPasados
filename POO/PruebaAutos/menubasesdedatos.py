import mysql.connector

conector1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    )

cursor1 = conector1.cursor()

def ListarBasesDeDatos():
    cursor1.execute("SHOW DATABASES")
    print("listado de bases de datos")
    for x in cursor1:
        print(x)

def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

def printMenu():
    print("Menu")
    print("0 - Salir")
    print("1 - Listar bases de datos")
    print("2 - Mostrar conector")
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
            print("Listando bases de datos")
            ListarBasesDeDatos()
        else:
            print("Funcion invalida :/")

menu()
