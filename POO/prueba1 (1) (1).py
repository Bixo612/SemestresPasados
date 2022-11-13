import random

class Combatiente():
    
    def __init__(self, n="",v=100):
        self.nombre=n
        self.vida=v

    def set_nombre(self,n):
        self.nombre = n
    def get_nombre(self):
        return self.nombre

    def set_vida(self, v):
        self.vida = v
    def get_vida(self):
        return self.vida

 
class Batalla():

    def __init__(self):
        self.eleccion1 = ""
        self.eleccion2 = ""
        self.registro = []
        self.golpe=0


    def set_golpe(self,g):
        self.golpe = g
    def get_golpe(self):
        return self.golpe

    def set_eleccion1(self,e1):
        self.eleccion1 = e1
    def set_eleccion2(self,e2):
        self.eleccion2 = e2

    def get_eleccion1(self):
        return self.eleccion1
    def get_eleccion2(self):
        return self.eleccion2

    def registrar(self,ganador):
        self.registro.append({"combatiente1":self.eleccion1,"combatiente2":self.eleccion2, "Ganador":ganador})

    def get_registro(self):
        return self.registro

    def tiradorCombatiente1(self):
        opcionTiradaMaq= random.randrange(0,99)
        eleccionMaq=0
        
        print("ESCOGIENDO PORCENTAJE DE POSIBILIDADES....!!!".center(40))
        if opcionTiradaMaq >= 0 and opcionTiradaMaq<=10:
            eleccionMaq= "Fallar"
        elif opcionTiradaMaq >= 11 and opcionTiradaMaq<=60:
            eleccionMaq= "Golpe Normal"  
        elif opcionTiradaMaq >= 61 and opcionTiradaMaq<=80:
            eleccionMaq ="Patada"  
        elif opcionTiradaMaq >= 81 and opcionTiradaMaq<=85:
            eleccionMaq ="Golpe Letal"  
        else: 
            eleccionMaq="Golpe Mortal"   
        print("*"*80)
        return "La posibilidad de falla es de: "+ str(opcionTiradaMaq) + "% " +"Lo que corresponde a:" + str(eleccionMaq) 
  
    def tiradorCombatiente2(self):
        opcionTiradaMaq2= random.randrange(0,20)
        print("ESCOGIENDO PORCENTAJE....!!!".center(40))
        print("*"*80)
        return "Estimado combatiente n° 2, usted califica con: "+ str(opcionTiradaMaq2) + "% " +"para bloquear el 70"+ "% " +" del daño del golpe recibido por el combatiente n° 1" 




    def pleito(self):
        opcionTiradaGolpes= random.randrange(0,3)
        eleccionGolpe=""
        glp=0
        if opcionTiradaGolpes == 0:
            eleccionGolpe= "Ha recibido un daño normal, se que no es nada para ti....pero lamentablemente se disminura tu vida - 10 puntos"            
            glp=10
        elif opcionTiradaGolpes == 1:
            eleccionGolpe= "Rayos, recibio una patada... a su vida se descontaran - 15 puntos"            
            glp=15
        elif opcionTiradaGolpes== 2:
            eleccionGolpe ="Eso si que fue un golpe letal... a su vida se descontaran - 30 puntos"            
            glp=30
        else:
            eleccionGolpe ="Wow!!! Que gran Golpe Mortal... a su vida se descontaran - 99 puntos"        
            glp=99
        print("*"*80)
        return eleccionGolpe

    def combatir(self):
        ganador = None
        cont = 1
        
        while self.eleccion1.get_vida() >0 and self.eleccion2.get_vida() > 0
            if cont % 2 = 0:

            else:
                



            cont = cont + 1
        self.registrar(ganador)
        return

lucha = Batalla()



#mostrando menu
def mostrarMenu():
    
    print("*"*50)
    print("Menu Mortal Fighter**".center(40, "*"))
    print("1- Apostar a combatiente")
    print("2- Salir\n")
    print("*"*50)

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
            print("Error!! Debe escoger 1 o 2")
    return opcion

f = False
apostado=""
while not f:
    mostrarMenu()
    opcion = leerOpcion()
    if opcion == 1:
        print("*"*100)
        print("\nBienvenido al juego Mortal Fighter, antes que nada...Ingrese los nombres de los combatientes por favor!!!\n")    
        print("*"*100)
        nombre_combatiente1 = input("Ingrese el nombre del combatiente numero 1: ")
        nombre_combatiente2 = input("Ingrese el nombre del combatiente numero 2: ")
        print("*"*100)
        combatiente1 = Combatiente(nombre_combatiente1)
        combatiente2 = Combatiente(nombre_combatiente2)
        print ("\nComenzando.... !!!¿¿¿Estas listo???!!! \n")
        print("*"*100)
        print ("a)Combatiente numero 1:", combatiente1.get_nombre())
        print ("b)Combatiente numero 2:", combatiente2.get_nombre())
        lucha.set_eleccion1(combatiente1)
        lucha.set_eleccion2(combatiente2)
        #print ("\n")
        while apostado != "a" and apostado!= "b":
            apostado=input("Ahora que ya sabes cuales son los jugadores, debes seleccionar uno de ellos!!(a/b): ")
            if apostado != "a" and apostado != "b":
                print("Ohhh, recuerde que debe ingresar solo a o b")
        print("El combatiente escogido es el", apostado, "¡Buena suerte!")
        print("Registro de vidas: ")
        while combatiente1.get_vida() > 0 and combatiente2.get_vida() > 0:
            lucha.combatir()

            print(combatiente1.get_nombre(), "***", combatiente2.get_nombre())
            print(combatiente1.get_vida(), "***", combatiente2.get_vida())  

        break
    else:
        salir = True    
        break
#imprimiendo objetos de prueba
# 

# if combatiente1.get_vida() > combatiente2.get_vida():
#     print("El ganador de esta dura batalla es: ", combatiente1.get_nombre())
# else:
#     print("El ganador a esta dura batalla es: ", combatiente2.get_nombre())