import mysql.connector

con = mysql.connector.connect(host="localhost", user="root",password="", database="zapateria")

cursorx = con.cursor()

class Zapato():
    def __init__(self, codigo, descripcion, precio, cantidad, descuento):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio =    precio
        self.cantidad = cantidad
        self.descuento = descuento
       
    def get_codigo(self):
        return self.codigo

    def get_descripcion(self):
        return self.descripcion
    
    def get_precio(self):
        return self.precio

    def get_cantidad(self):
        return self.cantidad

    def get_descuento(self):
        return self.descuento

    def set_codigo(self, codigo):
        self.codigo = codigo
    
    def set_descricion(self, descripcion):
        self.descripcion = descripcion

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return "Codigo: {} | Descripcion: {} | Precio: ${} | Cantidad: {} | Descuento: {} |".format(self.get_codigo(),self.get_descripcion(),self.get_precio(),self.get_cantidad(),self.get_descuento())

class Zapateria():

    def __init__(self, nombreZap, dia):
        self.nombreZap = nombreZap
        self.dia = dia
        self.numeroventas = 0
        self.ventas = 0
        self.listaZapatos = []

    
    def get_nombreZap(self):
        return self.nombreZap
    
    def get_dia(self):
        return self.dia
    
    def set_nombreZap(self, nombreZap):
        self.nombreZap = nombreZap

    def set_dia(self, dia):
        self.dia = dia

    def get_ventas(self):
        return self.ventas

    def get_numeroventas(self):
        return self.numeroventas

    def set_numeroventas(self, ventasdia):
        self.numeroventas = ventasdia
        

    def vender_zapato(self, zapato):
        self.listaZapatos.append(zapato)
        print("*****VENTA DE ZAPATO********")
        valor = zapato.get_precio() * zapato.get_cantidad()
        
        if (zapato.get_descuento()):
            valor *= 0.8
        
        self.ventas += valor
        self.numeroventas += 1
        
        print("Venta numero {}".format(self.get_numeroventas()))
        print("unidades de Zapatilla  {}, Valor Unitario {}".format(zapato.get_cantidad(), zapato.get_precio()))
        print("Total a Pagar  {}".format(valor))

        return self

    def MuestraZapatosVendidos(self):
        print("mostrando zapatos vendidos")
        for i in range(len(self.listaZapatos)):
            x = self.listaZapatos[i]
            print(x)
    ## Nueva clase
    def MuestraZapatosBD(self):
        print ("Mostrando Zapatos de la BD")
        sql = """select *  from zapato """        
        cursorx.execute(sql)

        resultado = cursorx.fetchall()

        for x in resultado:
            print (x)
        
        print ("Fin de Consulta")

    def ConsultarID(self):
        id = int(input("Hola bienvenido Ingrese codigo a buscar"))
        val = (id,)
        sql = "select * from zapato where id_zapato = %s"

        cursorx.execute(sql,val)
        resultado = cursorx.fetchone()
        
        print (resultado)

class Vendedor():
    
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.sexo = ""
        self.zapatoVendido = None 

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad
    
    def get_edad(self):
        return self.edad
 
    def get_sexo(self):
        return self.sexo
 
    def set_sexo(self, sexo):
        self.sexo = sexo


    def vender(self, tienda):
        tienda.vender_zapato(self.zapatoVendido)

    def configuravendedor(self):
        nom = ""
        edad = 0
        sexo = ""

        nom = input("Ingrese el nombre del vendedor ")
        edad = input("ingresa la edad del vendedor  ")
        sexo = input("ingrese el sexo del vendedor  ")

        self.set_nombre(nom)
        self.set_edad(edad)
        self.set_sexo(sexo)

        print("usuario Configurado aca los datos:  ")
       

    
    def __str__(self):
        return "Nombre del Vendedor: {} | Edad: {} | Sexo: {} ".format(self.get_nombre(),self.get_edad(),self.get_sexo())



    def CrearZapato(self):
        cod= 0
        desc=None
        pre=0
        cant=0
        desct= False
        print("Generador de Zapatos")
 
        while cod < 999 or cod > 7999:
            cod = int(input("Ingrese un codigo entre 999 a 7999: "))
            if cod < 999 or cod > 7999:
                print ("Codigo invalido intentelo nuevamente")
            else:
                print ("Codigo ",cod," registrado correctamente ")
    
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
        print (z.get_codigo())
       
        sql = "INSERT INTO zapato (id_zapato, nombre, precio, cantidad) values (%s,%s,%s,%s)"
        val = (z.get_codigo(), z.get_descripcion(), z.get_precio(), z.get_cantidad())  
        cursorx.execute(sql,val)

        con.commit()

        print(cursorx.rowcount, "zapato guardado en la BD")

        self.zapatoVendido = z
        print ("**Zapato Ok**")

    

tienda = Zapateria("MegaZapatos","Martes 23")
menu = True
memo = Vendedor()
## memo.configuravendedor()

print(memo)
ctrl = "invalido"


print( "Bienvenidos a la tienda v2 :  {}  , Ahora con BD " .format(tienda.get_nombreZap()))


while menu:
    ctrl =" "
    while ctrl != "y" or ctrl != "n" or ctrl !="l":
        ctrl = input("""
        MENU ZAPATERIA
        Ingrese un valor:
        (y) para vender
        (l) listar zapatos en BD
        (c) Consultar por ID de Zapato

USTED ALUMNO DEBERA DESARROLLAR LOS SIGUIENTES METODOS:

adicional debera modificar el metodo Crear zapato, para que este obtenga el ultimo id de la bd y lo pueda utilizar

        (p) Informar precio Promedio Zapatos
        (k) Mostrar zapato mas caro
        (j) Mostrar Zapato con mas unidades (cantidad)
        (r) Listar zapatos ordenados por precio de mayor a menor
        (n) salir del sistema 
                """)
        if ctrl == "y":
            print ("Ingrese Producto")
            memo.CrearZapato()
            memo.vender(tienda)
        elif ctrl == "n":
            print ("Cierre del dia:")
            print("total Ventas de dia {}  -Numero de ventas realizadas {} -  TOTAL  :   {}".format(tienda.get_dia(), tienda.get_numeroventas( ), tienda.get_ventas()))
            break
        elif ctrl == "l":
             tienda.MuestraZapatosBD()
        elif ctrl == "c":
            print ("Ingresando al modulo de consultas")
            tienda.ConsultarID()
        else:
            print ("Ingrese una opcion valida (y/n)") 
    
    menu = False

print("adios")