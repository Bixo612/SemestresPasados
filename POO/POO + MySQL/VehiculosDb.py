import mysql.connector
import random
import hashlib

def generarPatenteAntigua():
    pat = chr(random.randint(65,90))
    pat = pat + chr(random.randint(65,90))
    pat = pat + str(random.randint(0,9))
    pat = pat + str(random.randint(0,9))
    pat = pat + str(random.randint(0,9))
    pat = pat + str(random.randint(0,9))   
    return pat

def generarPatenteNueva():
    pat = chr(random.randint(65,90))
    pat = pat + chr(random.randint(65,90))
    pat = pat + chr(random.randint(65,90))
    pat = pat + chr(random.randint(65,90))
    pat = pat + str(random.randint(0,9))
    pat = pat + str(random.randint(0,9))   
    return pat

# https://www.w3schools.com/python/python_mysql_create_db.asp

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="concesionario"
    )

cursor = mydb.cursor()

def insertIntoVehiculos(pat,ano,marca,modelo):

    sql = "Insert into vehiculos (patente,ano,marca,modelo) Values (%s,%s,%s,%s)"
    val = (pat,ano,marca,modelo)
    cursor.execute(sql,val)

def buscarPorPatente(patente):
    sql = "Select * from vehiculos where patente = %s"
    pat = (patente,)
    cursor.execute (sql,pat)
    resultado = cursor.fetchall()
    for x in resultado:
        print (x)

def selectAllVehiculos():
    cursor.execute("Select * from vehiculos order by patente")
    resultado = cursor.fetchall()
    for x in resultado:
        print (x)

# def buscarPorPatente(patente):
#     sql = "Select * from vehiculos where patente like %Rt"
#     pat = (patente,)
#     cursor.execute (sql)
#     resultado = cursor.fetchone()
#     print(resultado)
    


# selectAllVehiculos()
# print ("------")
# buscarPorPatente("HCDK86")


# print (generarPatenteNueva())