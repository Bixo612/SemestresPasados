class auto:
    def __init__(self):
        self.patente="------"
        self.velocidad=0
        
        self.choque=False
    
    def set_patente(self,pat):
        #La patente ingresada debe tener 6 caracteres para ser registrada
        if len(pat)==6:
            self.patente=pat
            print("Patente registrada")
        else:
            print("Largo de patente invalida")

    def get_patente(self):
        return self.patente

    def get_velocidad(self):
        return self.velocidad

    def acelerar(self):
        self.velocidad=self.velocidad+1
        print ("El auto ",self.patente,"va a ",self.velocidad,"Km/H")
    
    def desacelerar(self):
        self.velocidad=self.velocidad-1
        print ("El auto ",self.patente,"va a ",self.velocidad,"Km/H")



# string = "pa"
# x=3

# if len(string)<x:
#     print("Es menor a ",x)
# elif len(string)==x:
#     print("Es igual a ",x)
# else:
#     print("Es mayor a ",x)
