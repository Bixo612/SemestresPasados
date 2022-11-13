# REALIZAR APUESTTAS A BATALLAS
#COMBATIENETE1  0 - 10 = FALLA    11 - 60 = GOLPE NORMAL    61 - 80 = PATADA  81 - 85 = GOLPE LETAL  86 - 99 = GOLPE MORTAL
#COMBATIENTE2  0 - 20 = BLOQUEAR EL 70 PORCIENTO
# NORMAL = 10 PTOS ---  PATADA = 15 PTOS ------ LETAL = 30 PTOS ------- MORTAL = 99 PTOS   
# LOS JUGADORES ATACCAN Y BLOQUEAN POR TURNOS, PARTE ATACANDO EL JUGADOR 1
# INFORMAR CUANTAS BATALLAS SE ACERTO LA APUESTA
#

import random

class combatientes():
    def __init__ (self,nombre,nombre1):
        self.nombre = nombre
        self.nombre1 = nombre1

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_nombre1(self,nombre1):
        self.nombre1 = nombre1

    def get_nombre1(self):
        return self.nombre1

class apuesta():
    def __init__(self):  

        self.opcionCombatiente = 0

    def set_opcionCombatiente(self,op1):
        self.opcionCombatiente = op1

    def get_opcionCombatiente(self):
        return self.opcionCombatiente

    def eleccion_jugador(self):

        self.opcionCombatiente = 0
        while self.opcionCombatiente != 1 and self.opcionCombatiente != 2:
            self.opcionCombatiente = int(input("Elige al combatiente que ganara: "))
            if self.opcionCombatiente != 1 and self.opcionCombatiente != 2:
                print("Debe elegir entre 1 o 2 ya que son solo 2 combatientes") 
        return self.opcionCombatiente


class batalla():
    
    def __init__(self,j1,j2):
        
        self.combatiente1 = 1
        self.combatiente2 = 2
        self.vidacombatiente1 = 100
        self.vidacombatiente2 = 100
        self.contador = 1
        self.contadorPelea = 0

    def set_contador(self,count):
        self.contador = count

    def get_contador(self):
        return self.contador
    
    def set_combatiente1(self,cm1):
        self.combatiente1 = cm1

    def get_combatiente1(self):
        return self.combatiente1

    def set_combatiente2(self,cm2):
        self.combatiente2 = cm2

    def get_combatiente2(self):
        return self.combatiente2
    
    def set_vidacombatiente1(self,vc1):
        self.vidacombatiente1 = vc1

    def get_vidacombatiente1(self):
        return self.vidacombatiente1

    def set_vidacombatiente2(self,vc2):
        self.vidacombatiente2 = vc2

    def get_vidacombatiente2(self):
        return self.vidacombatiente2

    def pelea(self):
        
            ataque = random.randrange(0,100)
            defensa = random.randrange(0,100)
            self.vidacombatientes = 0
            
        
            if ataque in range(0,11):
                print("ATACANTE HA FALLADO")
                print()
                
            elif  ataque in range(11,61):
                self.vidacombatientes = self.vidacombatientes - 10
                print("ATACANTE HA DADO GOLPE NORMAL")
                print()
                if defensa in range(0,20):
                    self.vidacombatientes = self.vidacombatientes + 7
                    print("DEFENSOR LOGRA DEFENDERSE Y EVITA ALGO DE DAÑO")
            elif ataque in range(61,81):
                self.vidacombatientes = self.vidacombatientes - 15
                print("ATACANTE HA DADO PATADA")
                print()
                if defensa in range(0,20):
                    self.vidacombatientes = self.vidacombatientes + (15 * 0.7)
                    print("DEFENSOR LOGRA DEFENDERSE Y EVITA ALGO DE DAÑO")
                    print()
            elif ataque in range(81,86):
                self.vidacombatientes = self.vidacombatientes - 30
                print("ATACANTE HA DADO GOLPE LETAL")
                print()
                if defensa in range(0,20):
                    self.vidacombatientes = self.vidacombatientes + (30 * 0.7)
                    print("DEFENSOR LOGRA DEFENDERSE Y EVITA ALGO DE DAÑO")
                    print()
            elif ataque in range(86,100):
                self.vidacombatientes = self.vidacombatientes - 99
                print("ATACANTE HA DADO GOLPE MORTAL")
                print()
                if defensa in range(0,20):
                    self.vidacombatientes = self.vidacombatientes + (99 * 0.7)
                    print("DEFENSOR LOGRA DEFENDERSE Y EVITA ALGO DE DAÑO")
                    print()
        

            print ("El atacante inflinge: ",self.vidacombatientes,"puntos de vida")
                                            
            if self.contador % 2:
                self.vidacombatiente2 = self.vidacombatiente2 + self.vidacombatientes
                print("El combatiente 2 quedo con ",self.vidacombatiente2,"puntos de vida")
            else:
                self.vidacombatiente1 = self.vidacombatiente1 + self.vidacombatientes
                print("El combatiente 1 quedo con ",self.vidacombatiente1,"puntos de vida")
            self.contador = self.contador + 1
    
    
    def contador_peleas(self):

        self.contadorpeleas =  self.contadorpeleas + 1                   
        

def mostrarMenu():
    

    print("*"*80)
    print("MENU COMBATE FIGHTER".center(60))
    print("*"*80)
    print("1- Combate Mortal")
    print("2- Salir")

def leerNumeroEntero(texto):
    try:
        return int(input(texto))
    except:
        return None

def leerOpcion():
     
    opcion = None    
    while opcion == None or opcion not in range(1,3):
        opcion = leerNumeroEntero("Ingrese opcion: ")
        if opcion == None or opcion not in range(1,3):
            print("Escoger solo opcion de 1 a 3 son las opciones disponibles.")
    return opcion

contadorbatallas = 0
contadorGanadas = 0
salir = False
while not salir:
    mostrarMenu()
    opcion = leerOpcion()
    if opcion == 1:

        peleador1 = input("Ingrese nombre combatiente 1: ")
        peleador2 = input("Ingrese nombre combatiente 2: ")
        peleadores = combatientes(peleador1,peleador2)
        print( peleadores.get_nombre()  ," V/S ", peleadores.get_nombre1() )

        apostador = apuesta()
        apostador.eleccion_jugador()
        print(" Apostaste al COMBATIENTE: ",apostador.get_opcionCombatiente())
        print("-----------------------------------")
        print("VAMOS A LA BATALLA")
        print("-----------------------------------")
        combate_Mortal = batalla()
        while combate_Mortal.get_vidacombatiente1() >= 1 and combate_Mortal.get_vidacombatiente2() >= 1:
            print(combate_Mortal.get_contador())
            combate_Mortal.pelea()
            ver = (input())
            if combate_Mortal.get_vidacombatiente1() >= 1 and combate_Mortal.get_vidacombatiente2() >= 1:

                pass
        contadorbatallas =+ 1 
        if combate_Mortal.get_vidacombatiente1() >= 1:
            print("EL GANADOR ES EL COMBATIENTE 1 : ",peleadores.get_nombre() )

        else:
            print("EL GANADOR ES EL COMBATIENTE 2 : ",peleadores.get_nombre1())

        if apostador.get_opcionCombatiente() == 1 and combate_Mortal.get_vidacombatiente1() >= 0:
            print("HAS GANADO LA APUESTA")
            contadorGanadas =+ 1 
        elif apostador.get_opcionCombatiente() == 1 and combate_Mortal.get_vidacombatiente1() <= 0:
            print("SERA PARA LA PROXIMA, PERDISTE LA APUESTA")
        if apostador.get_opcionCombatiente() == 2 and combate_Mortal.get_vidacombatiente2() >= 0:
            print("HAS GANADO LA APUESTA")
            contadorGanadas =+ 1 
        elif apostador.get_opcionCombatiente() == 2 and combate_Mortal.get_vidacombatiente2() <= 0:
            print("SERA PARA LA PROXIMA, PERDISTE LA APUESTA")
        
        
        print("*" * 50)
        print("has ganado ",contadorGanadas," APUESTA/S De un total de ",contadorbatallas," BATALLA/s" )
        print("*" * 50)
    salir = True



