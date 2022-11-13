class Zapateria():

    def __init__(self, codigo, descripcion, precio, cantidad, descuento):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio
        self.__cantidad = cantidad
        self.__descuento = descuento

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_precio(self, precio):
        self.__precio = precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

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


class Vendedor():

    def __init__(self, nombre, rut, ventas =[]):
        self.__nombre = nombre
        self.__rut = rut
        self.__ventas = ventas

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_rut(self, rut):
        self.__rut = rut

    def set_ventas(self, ventas):
        self.__ventas = ventas

    def get_nombre(self):
        return self.__nombre

    def get_rut(self):
        return self.__rut
    
    def get_ventas(self):
        return self.__ventas

 