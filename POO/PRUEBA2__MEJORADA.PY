import random

class combatiente():
    def __init__ (self,nombre):
        self.nombre = nombre
        self.vida = 100
    
    def restar_Vidas(self,daño):
        self.vida = self.vida - daño
        print("el peleador",self.nombre,"recibio un daño de: ",daño,)
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
       
    def set_contador(self,count):
        self.contador = count

    def get_contador(self):
        return self.contador
    
    def daño_Pelea(self):
        
            ataque = random.randrange(0,100)
            defensa = random.randrange(0,100)
            daño = 0
            
            if ataque in range(0,11):
                print("ATACANTE HA FALLADO")
                print()      
            elif  ataque in range(11,61):
                daño = daño - 10
                print("ATACANTE HA DADO GOLPE NORMAL")
                print()     
            elif ataque in range(61-81):
                daño = daño - 15
                print("ATACANTE HA DADO PATADA")
                print()    
            elif ataque in range(81,86):
                daño = daño - 30
                print("ATACANTE HA DADO GOLPE LETAL")
                print()     
            elif ataque in range(86,100):
                daño = daño - 99
                print("ATACANTE HA DADO GOLPE MORTAL")
                print() 
            if defensa in range(0,20):
                daño = daño - (daño * 0.7)
                print("DEFENSOR LOGRA DEFENDERSE Y EVITA ALGO DE DAÑO")
                print()
        
            print ("El atacante inflinge: ",daño,"puntos de vida")
                                            
            if self.contador % 2:
                self.peleador2.restar_Vidas(daño)
            else:
                self.peleador1.restar_Vidas(daño)
            self.contador = self.contador + 1
    
    
    def contador_peleas(self):

        self.contadorpeleas =  self.contadorpeleas + 1                   
        

