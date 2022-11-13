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

def validarCodigo(codigo):
    if codigo >= 999 and codigo <= 7999:
        return codigo
    else:
        print("Codigo invalido, ingreselo nuevamente")
        return None

def validarPrecio(precio):
    if precio >= 7000:
        return precio
    else:
        print("Precio invalido, ingreselo nuevamente")
        return None

def validarCantidad(cantidad):
    if cantidad > 0:
        return cantidad
    else:
        print("Cantidad invalido, ingreselo nuevamente")
        return None

class Vendedor():

    def __init__(self, codigo, descripcion, precio, cantidad, descuento):
        self.__codigo = validarCodigo(codigo)
        self.__descripcion = descripcion
        self.__precio = validarPrecio(precio)
        self.__cantidad = cantidad
        self.__descuento = descuento

    def set_codigo(self, codigo):
        self.__codigo = validarCodigo(codigo)

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_precio(self, precio):
        self.__precio = validarPrecio(precio)

    def set_cantidad(self, cantidad):
        self.__cantidad = validarCantidad(cantidad)

    def set_descuento(self, descuento):
        self.__descuento = descuento

    def get_codcodigo(self):
        return self.__codigo

    def get_descripcion(self):
        return self.__descripcion

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    def get_descuento(self):
        return self.__descuento

    def __str__(self):
        return "Cod:{} / Descripcion:{} / Precio:{} / Cantidad:{} / Descuento:{}\n".format(
            self.get_codcodigo(), self.get_descripcion(), self.get_precio(), self.get_cantidad(), self.get_descuento()
        )
    
class Zapateria():

    def __init__(self, dia):
        ventas = []
        self.__dia = dia
        self.__ventas = ventas
    
    def set_dia(self, dia):
        self.__dia = dia

    def set_ventas(self, ventas):
        self.__ventas = ventas

    def get_dia(self):
        return self.__dia

    def get_ventas(self):
        return self.__ventas
    
    def agregar_venta(self, ventaNueva):
        ventas = self.__ventas
        ventas.append(ventaNueva)
        self.__ventas = ventas

    def calcular_ventas(self):
        ventas = self.__ventas
        suma = 0
        for x in ventas:
            if x.get_descuento:
                suma = suma + ((x.get_precio()*0.8) * x.get_cantidad())
            else:
                suma = suma + (x.get_precio() * x.get_cantidad())
        return suma
        

    
ven1 = Vendedor(1001,"Converse Roja",47000,2,False)
ven2 = Vendedor(1002,"Converse Azul",45000,3,False)
ven3 = Vendedor(1003,"Addidas Blancas",50000,4,True)

zap = Zapateria("11/10/21")

zap.agregar_venta(ven1)
zap.agregar_venta(ven2)
zap.agregar_venta(ven3)

print(zap.calcular_ventas())