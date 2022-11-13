
import random

class Luchador():

    def __init__(self,nombre):
        self.nombre = nombre
        self.hp = 100
        self.vivo = True

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_vivo(self):
        return self.vivo

    def get_hp(self):
        return self.hp

    def set_hp(self,hp):
        self.hp = hp
        if self.hp <= 0:
            self.vivo = False
        elif self.hp > 0:
            self.vivo = True

    def rest_hp(self,dano):
        self.hp = self.hp - dano
        print(self.get_nombre(),"Tiene",self.get_hp(),"Pts de vida")
        if self.hp <= 0:
            self.vivo = False
            print(self.get_nombre(), "Ha sido derrotado")

class Funciones():

    def def_ataque(self,atacante):
        dano = 0
        ataque = random.randrange(0,99)
        if ataque in range(0,11):
            dano = 0
            print(atacante,"Ha fallado el ataque")
        elif ataque in range(11,61):
            dano = 10
            print(atacante,"Ha acertado un ataque normal")
        elif ataque in range(61,81):
            dano =  15
            print(atacante,"Ha acertado una patada")
        elif ataque in range(81,86):
            dano =  30
            print(atacante,"Ha acertado un golpe letal")
        elif ataque in range(86,99):
            dano =  99
            print(atacante,"Ha acertado un golpe mortal")
        return dano

    def def_dano_bloqueado(self,dano):
        dano_bloqueado = 0
        bloqueo = random.randrange(0,99)
        if bloqueo in range (0,20):
            dano_bloqueado = dano * 0.7
            print("Ha bloquado",dano_bloqueado,"Ptos de daño")
        return dano_bloqueado

class Combate(Funciones):
    def __init__(self, j1, j2,apuesta):
        self.j1 = j1
        self.j2 = j2
        self.contador = 1
        self.apuesta = apuesta

    def set_j1(self,j1):
        self.j1 = j1

    def set_j1(self,j1):
        self.j1 = j1

    def luchar(self):

        self.j1.set_hp(100)
        self.j2.set_hp(100)
        
        while self.j1.get_vivo() and self.j2.get_vivo():
            if self.contador % 2 == 0:
                dano = super().def_ataque(self.j2.get_nombre())
                dano_bloqueado = super().def_dano_bloqueado(dano)
                dano = dano - dano_bloqueado
                self.j1.rest_hp(dano)
                print()
            else:
                dano = super().def_ataque(self.j1.get_nombre())
                dano_bloqueado = super().def_dano_bloqueado(dano)
                dano = dano - dano_bloqueado 
                self.j2.rest_hp(dano)
                print()
            self.contador = self.contador + 1
        
        if self.j1.get_vivo():
            print(self.j1.get_nombre(), "Ha ganado")
        elif self.j1.get_vivo():
            print(self.j1.get_nombre(), "Ha ganado")

def printMenu():
    print("""    MENU COMBAT FIGHTER
    1-Combate
    2-salir""")
    
ext = True

while ext:
    printMenu()
    op = int(input("**Seleccione una opcion: "))
    if op == 1:
        nombre = input("**Ingrese el nombre del primer combatiente")
        j1 = Luchador(nombre)
        nombre = input("**Ingrese el nombre del segundo combatiente")
        j2 = Luchador(nombre)
        print ("Prximo Combate",j1.get_nombre(),"V/S",j2.get_nombre())
        op = -1
        while op not in range (1,3):
            print ("1- ",j1.get_nombre())
            print ("2- ",j2.get_nombre())
            op = int(input("**Seleccione apuesta"))
        combate = Combate(j1,j2,op)
        print()
        rep = "y"
        while rep == "y" or rep == "Y":
            combate.luchar()
            rep = input ("**Desea reptir combate y apuesta (y)")

    elif op == 2:
        ext = False
        print("Gracias por jugar :D")
    else:
        print("Ingrese una opcion valida D:")


