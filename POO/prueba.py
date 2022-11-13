import random

def printMenu():
    print("""
    MENU COMBAT FIGHTER
    1-Ingresar combatiente
    2-Combate
    4-Salir""")

class Luchador():

    def __init__(self):
        self.nombre = ""
        self.hp = 100

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_hp(self,hp):
        self.hp = hp
    
    def get_nombre(self):
        return self.nombre

    def get_hp(self):
        return self.hp
    
    def restar_hp(self, dano):
        self.hp = self.hp - dano

class Combate():
    pass

ext = True
menu = None
nombre = None
apuesta = None

j1 = Luchador()
j2 = Luchador()
mortalF= Combate(j1,j2)
while ext:
    printMenu()
    menu = input("Ingrese opcion")
    if menu == 1:
        nombre = input("ingrese el nombre del primer combatiente")
        j1.set_nombre(nombre)
        nombre = input("ingrese el nombre del segundo combatiente")
        j2.set_nombre(nombre)
    elif menu == 2:

        while apuesta not in range (1,3):
            print("A que personaje deseas aporstar")
            print("1-",j1.get_nombre())
            print("2-",j2.get_nombre())
            apuesta = input
            mortalF.combate()
            
    elif menu == 4:
        ext = False
    else:
        print ("Opcion Invalida :(")