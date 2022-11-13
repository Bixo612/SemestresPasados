class zapateria():
    def __init__(self, Nombre, dia):
        self._Nombre = Nombre
        self._dia = dia
        self.ventas = 0
    def set_dia(self, dia):
        self._dia = dia
    def set_nombre(self, Nombre):
        self._Nombre = Nombre
    def get_dia(self):
        return self.__dia
    def get_ventas(self):
        return self.__ventas

class Vendedor():
    def __init__(self, Nombre):
        self._Nombre = Nombre
        zapatoVendido = 0
    def set_Nombre(self, Nombre):
       self._Nombre = Nombre
    def get_Nombre(self, Nombre):
        return self._Nombre
    def CreaZapato(self):
        zapatoVendido = Zapato()
        return ("Zapato OK")

class Zapato():
    def __init__(self):
       self._codigo = self.set_codigo()
       self._descripcion = self.set_descripcion
       self._precio = self.set_precio    
       self._cantidad = self.set_cantidad
       self._descuento = self.set_descuento
    
    def set_codigo(self):
        codigo = 0
        while codigo >= 999 and codigo <=7999:
            codigo = input ("ingrese codigo entre 999 y 7999")
            if codigo >= 999 and codigo <= 7999:
                self._codigo = codigo
            else:
             print("Codigo invalido, ingreselo nuevamente")
        return ("codigo ok {}", self.get_codigo())
        
    def set_descripcion(self):
        descripcion = input("Ingrese un Nombre de zapato")
        self._descripcion = descripcion
        return ("Nombre ok {}", self.get_descripcion())
    
    def set_precio(self):
        precio = 0
        while precio >= 7000:
            precio = input ("ingrese precio mayor a 7000")
            if precio >= 7000:
                self._precio = precio
            else:
             print("Precio invalido, ingreselo nuevamente")
        return ("Precio ok {}", self.get_Precio())
    def set_cantidad(self):
        cantidad = 0
        while cantidad >= 1:
            cantidad = input ("ingrese Cantidad a Vender")
            if cantidad >= 1:
                self._cantidad = cantidad
            else:
             print("Cantidad invalida, ingreselo nuevamente")
        return ("Cantidad ok {}", self.get_cantidad())    
    def set_descuento(self):
        descuento = False
        descuento = input("Si tiene descuento escriba True")
        self._descuento = descuento
    
    def get_codigo(self):
        return self._codigo
    def get_descripcion(self):
        return self._descripcion
    def get_precio(self):
        return self._precio
    def get_cantidad(self):
        return self._cantidad
    def get_descuento(self):
        return self._descuento

vendedor = Vendedor("pedro")
vendedor.CreaZapato()