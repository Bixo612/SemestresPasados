class Validaciones():

    def asignar_eleccion():
        eleccion = None

        while eleccion!= 1 or eleccion!= 2 or eleccion!= 3 or eleccion!= 4 or eleccion !=5:
            pass

class Jugador(Validaciones):

    def __init__(self,nombre):
        self.nombre = nombre
        self.eleccion = None

class Persona(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)


class bot(Jugador):
    pass

ext = True

while ext:
    print ("1.- Jugador V/S Jugador")
    print ("2.- Jugador V/S Cpu")
    print ("3.- Salir")
    op = input("Ingrese opcion")
    if op == 1:
        print ("Jugador V/S Jugador")
    elif op == 2:
        print ("Jugador V/S Cpu")
    ext = False




