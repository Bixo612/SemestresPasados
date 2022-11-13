class Vehiculo():

    def __init__(self,patente,codMotor):
        self.__patente = patente
        self.__codMotor = codMotor

    def set_patente(self,patente):
        self.__patente = patente

    def set_patente(self,patente):
        self.__patente = patente


class Auto(Vehiculo):

    def __init__(self, patente, codMotor,asientos,puertas):
        super().__init__(patente, codMotor)
        self.__patente = patente
        self.__codMotor = codMotor

    