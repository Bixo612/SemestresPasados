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
        self.vida=100
        self.golpe=None

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

    def set_vida(self,v):
        self.vida = v
    def get_vida(self):
        return self.vida

#metodo registrar para poder agg a la list el registro de la batalla
    def registrar(self):
        self.registro.append({"combatiente1":self.eleccion1,"combatiente":self.eleccion2})

    def get_registro(self):
        return self.registro

#0 a 10 % posibilidad de Fallar
#11 a 60% de dar un golpe Normal 
# 61 a 80% de dar una patada  
#  81 a un 85 % de dar un golpe Letal
#  86 al 99% de probabilidad de acertar un golpe Mortal
#metodo tirador para poder obtener porcentaje al azar del combatiente 1(aproxi)

    def tiradorCombatiente1(self):
        import random
        opcionTiradaMaq= random.randrange(0,99)
        eleccionMaq=0
        print("ESCOGIENDO PORCENTAJE....!!!".center(40))
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
#metodo para combatiente 2   
    def tiradorCombatiente2(self):
        import random
        opcionTiradaMaq2= random.randrange(0,20)
        print("ESCOGIENDO PORCENTAJE....!!!".center(40))
        print("*"*80)
        return "Estimado combatiente n° 2, usted califica con: "+ str(opcionTiradaMaq2) + "% " +"para bloquear el 70"+ "% " +" del daño del golpe recibido por el combatiente n° 1" 

#metodo para los golpes
    def golpes(self):
        import random
        opcionTiradaGolpes= random.randrange(0,3)
        eleccionGolpe=""
        if opcionTiradaGolpes == 0:
            eleccionGolpe= "Ha recibido un daño normal, se que no es nada para ti....pero lamentablemente se disminura tu vida - 10 puntos"
            
        elif opcionTiradaGolpes == 1:
            eleccionGolpe= "Rayos, recibio una patada... a su vida se descontaran - 15 puntos"
            
        elif opcionTiradaGolpes== 2:
            eleccionGolpe ="Eso si que fue un golpe letal... a su vida se descontaran - 30 puntos"
            
        else:
            eleccionGolpe ="Wow!!! Que gran Golpe Mortal... a su vida se descontaran - 99 puntos"
            
        print("*"*80)
        return eleccionGolpe

#Entrada al juego junta a la pedida de nombres y creando objts comb1 y comb2
print("*"*100)
print("\nBienvenido al juego Mortal Fighter, antes que nada...Ingrese los nombres de los combatientes por favor!!!\n")    
print("*"*100)
nombre_combatiente1 = input("Ingrese el nombre del combatiente numero 1: ")
nombre_combatiente2 = input("Ingrese el nombre del combatiente numero 2: ")
print("*"*100)

combatiente1 = Combatiente(nombre_combatiente1)
combatiente2 = Combatiente(nombre_combatiente2)

print ("\nComenzando.... !!!¿¿¿Estas listo???!!! \n")
print ("Combatiente numero 1:", combatiente1.get_nombre())
print ("Combatiente numero 2:", combatiente2.get_nombre())
print ("\n")

lucha = Batalla()



    


#mostrando menu
def mostrarMenu():
    
    print("Menu** Mortal Fighter**".center(40, "*"))
    print("1- Apostar a combatiente")
    print("2- Salir\n")

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
while not f:
    mostrarMenu()
    opcion = leerOpcion()
    if opcion == 1:
        pass
        break
    else:
        salir = True    
        break
#imprimiendo objetos de prueba
enfrentamiento=Batalla()
print (enfrentamiento.tiradorCombatiente1())

enfrentamiento=Batalla()
print (enfrentamiento.tiradorCombatiente2())

enfrentamiento=Batalla()
print (enfrentamiento.golpes())

