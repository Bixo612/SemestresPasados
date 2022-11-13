atacar = ""
evadir = ""

class nave:
    def __init__(self):
        self.nombre = ""
        self.cargaMaxima = 100
        self.carga = 0
        self.vuela = False
        self.bajoAtaque = True
    
    def set_nombre(self,nombre):
        self.nombre = nombre
        print("--Nombre ingresado (",nombre,")")
    
    def despegar(self):
        if self.vuela:
            print("la nave se encuentra en vuelo")
        else:
            print("despegando...")
            print("la nave", self.nombre, "ha despegado exitosamente")
            self.vuela = True   
            self.estado = "bajo ataque"

        while self.bajoAtaque == True:
            print("trazando ruta a planeta mas cercano")
            print("despues de un tiempo de vuelo")
            self.vuela == True
            eleccion = input("se acercan naves enemigas, capitán sus ordenes! atacar o evadir: ")
            if eleccion == "atacar":
                print("preparense para atacar!")
                print ("fire, fire, pium pium, mueran cucarachas espaciales!")
                print("despues de una ardua batalla, hemos salido victoriosos")
                print("casi llegando a nuestro destino")
                self.bajoAtaque = False
            if eleccion == "evadir":
                print("realizando maniobras evasivas!")
                print ("hemos logrado escapar de nuestros enemigos")
                print("casi llegando a nuestro destino")
                self.bajoAtaque = False                 
            else:
                self.bajoAtaque == False
                
    def aterrizar(self):
        if self.bajoAtaque == False:
            print(self.nombre, "preparandose para aterrizar")
            print("descenciendo")
            
            if self.carga > self.cargaMaxima:
                print("peligro, la nave lleva demasiado peso, alerta! explosion inminente, afirmate Juan")
                print("gokuuuuu", "(boooom)")
                print("la nave ha explotado")
            else:
                print("la nave", self.nombre, "ha aterrizado exitosamente")        
        
        else:
            self.vuela = False
            print("la nave se encuentra en tierra")

    def cargar(self, bulto):
        self.carga=self.carga+bulto
        print("--La carga actual de", self.nombre, "es de", self.carga)

    def descargar(self, bulto):
        self.carga=self.carga-bulto
        print("--La carga actual de", self.nombre, "es de", self.carga)
   
naveA = nave()
naveB = nave()

naveA.set_nombre("starfox")
naveB.set_nombre("Milano")    

naveA.cargar(+100)
naveB.cargar(+120)

naveA.descargar(50)

naveA.despegar()
naveB.despegar()

naveA.aterrizar()
naveB.aterrizar()