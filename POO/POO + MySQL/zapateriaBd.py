import mysql.connector

def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zapateria"
    )

cursor = con.cursor()

def insertIntoZapatos(idZapato,nombre,precio,cantidad):
    sql = "Insert into zapato (id_zapato,nombre,precio,cantidad) Values (%s,%s,%s,%s)"
    val = (idZapato,nombre,precio,cantidad)
    cursor.execute(sql,val)

def selectAllZapatos():
    cursor.execute("Select * from zapato")
    resultado = cursor.fetchall()
    for x in resultado:
        print (x)

def selectZapatoId(id):
    sql = "Select * from zapato where id_zapato = %s"
    val = (id,)
    cursor.execute(sql,val)
    resultado = cursor.fetchone()
    print(resultado)


def printMenu():
    print ("""
MENU ZAPATERIA

(1) Vender zapato
(2) Listar zapatos 
(3) Buscar zpato por id
(4) Precio promedio de zapatos
(5) Zapato mas caro
(6) Zapato con mas unidades
(7) Lista de zapatos ordenados por precio
(0) salir del sistema 
""")

### Clases

class Validaciones():
    pass

class Zapato():
    def __init__(self, idZapato, descripcion, precio, cantidad):
        self.idZapato = idZapato
        self.descripcion = descripcion
        self.precio =    precio
        self.cantidad = cantidad
       
    def get_idZapato(self):
        return self.idZapato

    def get_descripcion(self):
        return self.descripcion
    
    def get_precio(self):
        return self.precio

    def get_cantidad(self):
        return self.cantidad

    # def get_descuento(self):
    #     return self.descuento

    def set_idZapato(self, idZapato):
        self.idZapato = idZapato
    
    def set_descricion(self, descripcion):
        self.descripcion = descripcion

    def set_precio(self, precio):
        self.precio = precio

    def set_cantidad(self, cantidad):
        self.cantidad

    def __str__(self):
        return "idZapato: {} | Descripcion: {} | Precio: ${} | Cantidad: {} |".format(self.get_idZapato(),self.get_descripcion(),self.get_precio(),self.get_cantidad())

class Vendedor():
    
    def __init__(self,nombre,edad,rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.zapato = None 

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad
    
    def get_edad(self):
        return self.edad
 
    def set_rut(self, rut):
        self.rut = rut
    
    def get_rut(self):
        return self.rut
    
    def __str__(self):
        return "Nombre del Vendedor: {} | Edad: {} | Rut: {} ".format(self.get_nombre(),self.get_edad(),self.get_rut())

    def CrearZapato(self):
        cod = 0
        pre = 0
        cant = 0

        print("Generador de Zapatos")
 
        while cod < 999 or cod > 7999:
            cod = int(input("Ingrese un idZapato entre 999 a 7999: "))
            if cod < 999 or cod > 7999:
                print ("idZapato invalido intentelo nuevamente")
            else:
                print ("idZapato ",cod," registrado correctamente ")
    
        desc = str(input("ingrese Nombre  "))
     
        while pre < 7000 :
            pre = int(input("Ingrese un precio desde $7.000: "))
            if pre < 7000:
                print ("Precio invalido intentelo nuevamente")
            else:
                print ("Precio ",pre," registrado correctamente")
   
           
        while cant <= 0 :
            cant = int(input("Ingrese un cantidad: "))
            if cant <= 0:
                print ("Cantidad invalido intentelo nuevamente")
            else:
                print ("Cantidad  " ,cant,"  registrado correctamente")
    
        respuesta = ""
        while respuesta != "y" or respuesta != "n":
             respuesta = input("Tiene descuento? (y/n): ") 
             if respuesta == "y":
                print("El producto tiene descuento")
                desct = True
                respuesta = ""
                break
             elif respuesta == "n":
                print("El producto NO tiene descuento")
                desct = False
                respuesta = ""
                break
             else:
                print("Ingrese una opcion valida (y/n)")
    
        z = Zapato(cod, desc, pre, cant, desct)
        print (z.get_idZapato())
       
        sql = "INSERT INTO zapato (id_zapato, nombre, precio, cantidad) values (%s,%s,%s,%s)"
        val = (z.get_idZapato(), z.get_descripcion(), z.get_precio(), z.get_cantidad())  
        cursorx.execute(sql,val)

        con.commit()

        print(cursorx.rowcount, "zapato guardado en la BD")

        self.zapato = z
        print ("**Zapato Ok**")

### idZapato

menu = True

while menu:
    ctrl = None
    printMenu()
    ctrl = leerEntero("Selccione una opcion (0 a 7)\n0")
    if ctrl == 0:
        menu = False
        print ("Hasta luego :D")
    elif ctrl == 1:
        print ("Vender Zapato")
    elif
        