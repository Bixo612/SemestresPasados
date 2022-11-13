import mysql.connector

conector = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    )
print("hi")
print(conector)
print("conector ok")

input("crer database?")
cursor = conector.cursor()
cursor.execute("CREATE DATABASE concesionario2")
print("database creada")

input("mostrar databases?")
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)

input("conectar a concesionario")

conectordb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="concesionario2"
    )

cursordb = conectordb.cursor()

print (conectordb)
input("crear tabla vehiculos")
cursordb.execute("CREATE TABLE vehiculos (patente VARCHAR(8), anio INT, marca VARCHAR(20),marca VARCHAR(20))")