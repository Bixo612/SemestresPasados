# Juego cachipun con algunos pasos
# jugador vs jugador
# jugador vs CPU (importar un Random)
# con clases
# 5 opciones = piedra,papel,tijera,lagarto,Spock


import random

class persona():

    def __init__ (self,nombre):
        self.nombre = nombre

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre


class jugadores():
     
    def __init__(self):

        self.contador1 = 0
        self.contador2 = 0
        self.opcion1 = ""
        self.opcion2 = ""

    def set_contador(self,co1):
        self.contador1 = co1

    def get_contador(self):
        return self.contador1

    def set_contador2(self,co2):
        self.contador2 = co2

    def get_contador2(self):
        return self.contador2

    def set_opcion1(self,op1):
        self.opcion1 = op1

    def set_opcion2(self,op2):
        self.opcion2 = op2

    def get_opcion1(self):
        return self.opcion1

    def get_op2(self):
        return self.opcion2

    def opcion_Jugador1(self):
    

        self.opcion1 = None
        while self.opcion1 == None or self.opcion1 not in range(1,6):
                    
            self.opcion1 = leerNumeroEntero("""Selecione una tirada:   
    1- papel
    2- piedra
    3- tijera
    4- spock
    5- lagarto
                                                        
    Tu tirada es = """)

            if self.opcion1 == None or self.opcion1 not in range(1,6):
                        print("Escoger solo opcion de 1 a 5 son las opciones disponibles.")
            
        return self.opcion1

    def opcion_jugador2(self):
        
        self.opcion2 = None
        while self.opcion2 == None or self.opcion2 not in range(1,6):
                    
            self.opcion2 = leerNumeroEntero("""Selecione una tirada:   
    1- papel
    2- piedra
    3- tijera
    4- spock
    5- lagarto
                                                        
    Tu tirada es = """)

            if self.opcion2 == None or self.opcion2 not in range(1,6):
                        print("Escoger solo opcion de 1 a 5 son las opciones disponibles.")
        
        return self.opcion2

    def crear_Duelo(self,jugador1,jugador2):

          
        if self.opcion1 == 1 and self.opcion2 == 2:
                print("El ganador es",jugador1)
                self.contador1 = self.contador1 + 1 
 
        elif self.opcion1 == 3 and self.opcion2 == 2:
                print("El ganador es",jugador2)
                self.contador2 = self.contador2 + 1

        elif self.opcion2 == 1 and self.opcion1 == 2:
                print("El ganador es",jugador2)
                self.contador2 = self.contador2 + 1

        elif self.opcion2 == 3 and self.opcion1 == 2:
                print("El ganador es",jugador1)
                self.contador1 = self.contador1 + 1

        elif self.opcion2 == 3 and self.opcion1 == 1:
                print("El ganador es",jugador2)
                self.contador2 = self.contador2 + 1

        elif self.opcion1 == 3 and self.opcion2 == 1:
                print("El ganador es",jugador1)
                self.contador1 = self.contador1 + 1            
        else:
                print ("EMPATE!!!!")
        

class MAQUINA():
    pass



   



def mostrarMenu():
    print("Menu".center(30, "-"))
    print("1- Jugador VS PC")
    print("2- Jugador VS Jugador")
    print("3- Salir")

def leerNumeroEntero(texto):
    try:
        return int(input(texto))
    except:
        return None

def leerOpcion():
     
    opcion = None    
    while opcion == None or opcion not in range(1,4):
        opcion = leerNumeroEntero("Ingrese opcion: ")
        if opcion == None or opcion not in range(1,4):
            print("Escoger solo opcion de 1 a 3 son las opciones disponibles.")
    return opcion


salir = False
while not salir:
    mostrarMenu()
    opcion = leerOpcion()
    if opcion == 2:
        print("Empieza el jogo")
        Player1 = input("Nombre Jugador 1: ")
        Player2 = input("Nombre jugador 2: ")
        jugador1 = persona(Player1)
        jugador2 = persona(Player2)

        print( jugador1.get_nombre() ," VS ", jugador2.get_nombre())
        print("VAMOS A JUGAR..")
        
        juego_jugador_vs_jugador = jugadores()
        
        round = 0
        while juego_jugador_vs_jugador.get_contador() != 3 and  juego_jugador_vs_jugador.get_contador2() != 3:
            round = 1 + round
            print("ROUND: ",round)
            juego_jugador_vs_jugador.opcion_Jugador1()
            juego_jugador_vs_jugador.opcion_jugador2()
            juego_jugador_vs_jugador.crear_Duelo(Player1,Player2)
            print(Player1,"ha ganado: ",juego_jugador_vs_jugador.get_contador()," batalla/s")
            print(Player2,"ha ganado: ",juego_jugador_vs_jugador.get_contador2()," batalla/s")

            if juego_jugador_vs_jugador.get_contador() != 3 and  juego_jugador_vs_jugador.get_contador2() != 3:
                pass
        print("......................................")
        if juego_jugador_vs_jugador.get_contador() == 3:
            print("el indiscutible ganador es: ",Player1)
        else:
            print("el indiscutible ganador es: ",Player2)
        print("......................................")
    elif opcion == 1:
        pass
    else:
        salir = True    

