class Vehiculo():

    def set_color(self, color):
        self.__color = color

    def set_ruedas(self, ruedas):
        self.__ruedas = ruedas

    def get_color(self):
        return "morado"

    def get_ruedas(self):
        return 3

    def __str__(self):
        return "Color {}, {} ruedas, tipo: {}".format(self.get_color(), self.get_ruedas(), type(self).__name__)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().set_color(color)
        super().set_ruedas(ruedas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc, tipo: {}".format(super().get_color(), self.__velocidad, super().get_ruedas(), self.__cilindrada, type(self).__name__)

class Moto(Vehiculo):
    
    pass


coche = Coche("azul", 150, 4, 1200)
print(coche)

moto = Moto()
moto.set_color("rojo")
moto.set_ruedas(2)
print(moto)

vehiculo = Vehiculo()
print(vehiculo)