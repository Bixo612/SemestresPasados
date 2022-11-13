class Zapato():
    def __init__(self, codigo, descripcion, precio, cantidad, descuento):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
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
        self.ventas = 0
    
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

    def vender_zapato(self, zapato):
        valor = zapato.get_precio() * zapato.get_cantidad()

        if (zapato.get_descuento()):
            valor *= 0.8
        
        self.ventas += valor
        return self


class Vendedor():
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.zapatoVendido = None
 
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def vender(self, tienda):
        tienda.vender_zapato(self.zapatoVendido)

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
        self.zapatoVendido = z
        print ("**Zapato Ok**")

    

tienda = Zapateria("Batta","Martes 19")
menu = True
memo = Vendedor("Laura")
ctrl = "invalido"
print( "Bienvenidos a la tienda:  {}   " .format(tienda.get_nombreZap()))


while menu:
    ctrl =" "
    while ctrl != "y" or ctrl != "n":
        ctrl = input("Desea Vender? (y/n) ")
        if ctrl == "y":
            print ("Ingrese Producto")
            memo.CrearZapato()
            memo.vender(tienda)
        elif ctrl == "n":
            print ("Cierre del dia:")
            print("total Ventas de dia {}   -  TOTAL  :   {}".format(tienda.get_dia(), tienda.get_ventas()))
            break
        else:
            print ("Ingrese una opcion valida (y/n)") 
    
    menu = False

print("adios")