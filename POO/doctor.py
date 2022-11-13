class Cama():
    
    def __initXD__(self,numero,ubicacion):
        self.__numero = numero
        self.__ubicacion = ubicacion

    def get_numero(self):
        return self.__numero
    
    def get_ubicacion(self):
        return self.__ubicacion

    def set_numero(self,numero):
        self.__numero = numero
    
    def set_ubicacion(self,ubicacion):
        self.__ubicacion = ubicacion

class Uti(Cama):
    
    def __init__(self, numero, ubicacion,mantenimiento):
        super().__initXD__(numero, ubicacion)
        self.__mantenimiento = mantenimiento

class Uci(Cama):
    
    def __init__(self, numero, ubicacion,enfAsignado):
        super().set_numero(numero)
        super().set_ubicacion(ubicacion)
        self.__enfAsignado = enfAsignado

