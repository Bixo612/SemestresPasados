# Zapateria

# Caso a Resolver:
# Una tienda de calzado requiere registrar las ventas diarias,
# para ello usted desarrollará un prototipo considerando atributos
# de cada articulo: código, descripción, precio, cantidad, descuento (si será true, no será false).
# Reglas de Negocio:
# Precio debe ser mayor o igual a 7000.
# Cantidad debe ser mayor a cero.
# Código debe ser numérico entre 999 y 7999
# Un método arrojará el total de la compra
# Aquellos que tengan descuento se descontará un 20%
# Generar una Clase Vendedor el cual pueda interactuar con la Clase Zapatería y
# pueda realizar ventas, entregando los parámetros de cada producto.
# Programe ambas clases y los métodos necesarios para hacer el proceso de ventas.
# Además se requiere un método que entregue el total de las ventas realizadas en el día.

class Funciones():

    def crear_codigo(self):
        codigo = -1
        while codigo <= 999 or codigo >= 7999:
            codigo = int(input("Ingrese un codigo entre 999 a 7999: "))
            if codigo <= 999 or codigo >= 7999:
                print("Codigo invalido intentelo nuevamente")
            else:
                print("Codigo", codigo, "registrado correctamente")
        return codigo


    def crear_descripcion(self):
        descripcion = input("Ingrese una descripcion: ")
        return descripcion


    def crear_precio(self):
        precio = -1
        while precio < 7000:
            precio = int(input("Ingrese un precio desde $7.000: "))
            if precio < 7000:
                print("Precio invalido intentelo nuevamente")
            else:
                print("Precio", precio, "registrado correctamente")
        return precio


    def crear_cantidad(self):
        cantidad = -1
        while cantidad <= 0:
            cantidad = int(input("Ingrese un cantidad: "))
            if cantidad <= 0:
                print("Cantidad invalido intentelo nuevamente")
            else:
                print("Cantidad", cantidad, "registrado correctamente")
        return cantidad


    def crear_descuento(self):
        respuesta = ""
        while respuesta != "y" or respuesta != "n":
            respuesta = input("¿Tiene descuento? (y/n): ")
            if respuesta == "y":
                print("El producto tiene descuento")
                return True
            elif respuesta == "n":
                print("El producto NO tiene descuento")
                return False
            else:
                print("Ingrese una opcion valida (y/n)")

class Zapateria ():

    def __init__(self, nombreZap, dia):
        ventas = []
        self.nombreZap = nombreZap
        self.dia = dia
        self.ventas = ventas

    def get_nombreZap(self):
        return self.nombreZap

    def get_dia(self):
        return self.dia

    def set_nombreZap(self, nombreZap):
        self.nombreZap = nombreZap

    def set_dia(self, dia):
        self.dia = dia

    def agregarVenta(self, nuevaVenta):
        self.ventas.append(nuevaVenta)

    def calcular_ventas(self):
        ventas = self.ventas
        suma = 0
        for x in ventas:
            if x.get_descuento:
                suma = suma + ((x.get_precio()*0.8) * x.get_cantidad())
            else:
                suma = suma + (x.get_precio() * x.get_cantidad())
        return suma

class Vendedor():
    def __init__(self, nombre):
        self.nombre = nombre
        self.zapatoVendido = None

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def crearZapato(self):
        self.zapatoVendido = Zapato()
        print("**Zapato Ok**")

    def venderZapato(self, zapateria):
        zapateria.agregarVenta(self.zapatoVendido)
        print("**Zapato agregado a las ventas**")
        return zapateria

class Zapato(Funciones):

    def __init__(self):
        self.codigo = super().crear_codigo()
        self.descripcion = super().crear_descripcion()
        self.precio = super().crear_precio()
        self.cantidad = super().crear_cantidad()
        self.descuento = super().crear_descuento()

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

    def set_codigo(self):
        self.codigo = super().crear_codigo()

    def set_descricion(self):
        self.descripcion = super().crear_descripcion()

    def set_precio(self):
        self.precio = super().crear_precio()

    def set_cantidad(self):
        self.cantidad = super().crear_cantidad()

    def set_precio(self):
        self.descuento = super().crear_descuento()

    def __str__(self):
        return "Codigo {} / Descripcion {} / Precio {} / Cantidad {} / Descuento {} ".format(
            self.get_codigo(), self.get_descripcion(), self.get_precio(), self.get_cantidad(), self.get_descuento())

memo = Vendedor("Memo")

print(memo.nombre)

memo.crearZapato()

print(memo.zapatoVendido)

beba = Zapateria("Calzados Beba", "12/10/2021")

beba = memo.venderZapato(beba)

print("Las ventas total del dia son: ", beba.calcular_ventas())

zap = Zapato()

print("Fin :D")
