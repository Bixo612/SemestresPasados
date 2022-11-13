# Fabian Morales Molina 18665542-7
# Vicente Vasquez Vasquez 19360397-1

import random

#Se definen el nombre del combatiente
class combatientes():
    def __init__ (self,nombre):
        self.nombre = nombre
        self.vida = 100
    
    def restar_Vidas(self,dano):
        self.vida = self.vida - dano
        print("la vida del peleador = ",self.vida)

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_vida(self,vida):
        self.vida = vida

    def get_vida(self):
        return self.vida


class batalla():

    def __init__(self,peleador1,peleador2):
        
        self.contador = 1
        self.peleador1 = peleador1
        self.peleador2 = peleador2


    def set_peleador1(self,peleador1):
        self.peleador1 = peleador1

    def get_peleador1(self):
        return self.peleador1

    def set_peleador2(self,peleador2):
        self.peleador2 = peleador2

    def get_peleador2(self):
        return self.peleador2

    def set_contador(self,count):
        self.contador = count

    def get_contador(self):
        return self.contador
    
    def dano_Pelea(self):
        

            ataque = random.randrange(0,100)
            defensa = random.randrange(0,100)
            dano = 0
            bloqueo = 0

        
            if ataque in range(0,11):
                dano = 0
                print("ATACANTE HA FALLADO")
                print()
                
            elif  ataque in range(11,61):
                dano = 10
                print("ATACANTE HA DADO GOLPE NORMAL")
                print()

            elif ataque in range(61,81):
                dano =  15
                print("ATACANTE HA DADO PATADA")
                print()

            elif ataque in range(81,86):
                dano =  30
                print("ATACANTE HA DADO GOLPE LETAL")
                print()

            elif ataque in range(86,100):
                dano =  99
                print("ATACANTE HA DADO GOLPE MORTAL")
                print()

            if defensa in range(0,20):
                bloqueo =  dano * 0.7
                dano = dano - bloqueo
                print("el pelador bloqueo =",bloqueo )
                                            
            if self.contador % 2:
                print("el peleador",self.peleador1.get_nombre(),"le hizo",dano,"puntos de daño a ",self.peleador2.get_nombre())
                self.peleador2.restar_Vidas(dano)
            else: 
                print("el peleador",self.peleador2.get_nombre(),"le hizo",dano,"puntos de daño a ",self.peleador1.get_nombre())
                self.peleador1.restar_Vidas(dano)
            self.contador = self.contador + 1
    



def eleccion_jugador():

    eleccion = 0
    while eleccion != 1 and eleccion != 2:
        eleccion = int(input("Elige al combatiente que ganara: "))
        if eleccion != 1 and eleccion != 2:
            print("Debe elegir entre 1 o 2 ya que son solo 2 combatientes")         
    return eleccion  


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
            print("Escoger solo opcion de 1 a 2 son las opciones disponibles.")
    return opcion
            
j1 = combatientes(None)
j2 = combatientes(None)
pelea = batalla(j1,j2)

salir = False
while not salir:
    mostrarMenu()
    opcion = leerOpcion()
    if opcion == 1:
        nombre = input("Ingrese nombre del combatiente 1 = ")
        j1.set_nombre(nombre)
        nombre = input("Ingrese nombre del combatiente 2 = ")
        j2.set_nombre(nombre)
        print()
        print("La Batalla sera entre los siguientes combatientes:")
        print( j1.get_nombre()  ," V/S ", j2.get_nombre() )
        print(" 1.-",j1.get_nombre() )
        print(" 2.-",j2.get_nombre() )
        eleccion = eleccion_jugador()
        contador_aciertos = 0
        retry = False
        contador_combates = 0
        while not retry:     
            while j1.get_vida() >= 0 and j2.get_vida() >= 0:
                print("Ataque numero: ",pelea.get_contador())
                pelea.dano_Pelea()
                input()

            if j1.get_vida() >= 0:
                print ("**",j1.get_nombre(),"WINS **")
            elif j2.get_vida() >= 0:
                print ("**",j2.get_nombre(),"WINS **")

            contador_combates = contador_combates + 1
            if eleccion == 1 and j1.get_vida() > 0:
                contador_aciertos = contador_aciertos + 1
                print ("Acertaste tu apuesta, llevas ",contador_aciertos,"acierto(s) de ", contador_combates , " batalla(s)" )
            elif eleccion == 2 and j2.get_vida() > 0:
                contador_aciertos = contador_aciertos + 1
                print ("Acertaste tu apuesta, llevas ",contador_aciertos,"acierto(s) de ", contador_combates , " batalla(s)" )
            else:
                print ("Fallaste tu apuesta, llevas ",contador_aciertos,"acierto(s) de ", contador_combates , " batalla(s)" )
            option = input("¿quires repetir combate y apuesta? (y): ")
            j1.set_vida(100)
            j2.set_vida(100)
            if option == "y" or option == "Y":
                retry = False
            else:
                retry = True
    else:
        salir = True
        print ("Gracias por jugar")
        
        
        

