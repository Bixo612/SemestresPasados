class nave:
    def __init__(self):
        self.nombre =""
        self.max    =100
        self.carga  =0
        self.fly    =False
    
    def set_nombre(self,nom):
        self.nombre=nom
        print ("--Nombre registrado (",nom,")--",sep="")

    def despegar(self):
        if self.fly:
            print ("--La nave",self.nombre,"ya esta volando")
        else:
            self.fly=True
            print ("--La nave",self.nombre,"despego")

    def aterrizar(self):
        if self.fly:
            if self.carga > self.max:
                print ("--La nave",self.nombre,"exploto")
                print ("--por que la carga superaba el maximo permitido")
                self.nombre =""
                self.max    =100
                self.carga  =0
                self.fly    =False
                print ("--Se han borrado los registros de la nave")
            else:
                self.fly=False
        else:
            print ("--La nave",self.nombre,"aun no despega")

    def cargar(self,Y):
        self.carga=self.carga+Y
        print("--Se actualizo la carga",self.carga)

# Instanciar Naves
nave1 = nave()
nave2 = nave()

# nombre =input("Ingrese el nombre de la nave 1: ")
# nave1.set_nombre(nombre)
# nombre =input("Ingrese el nombre de la nave 2: ")
# nave2.set_nombre(nombre)

nave1.set_nombre("X-Wing")
nave2.set_nombre("Razor Crest")

# Cargar Naves
nave1.cargar(150)
nave2.cargar(120)

# Descargar Naves
nave1.cargar(-60)

# Aterrizar Naves
nave1.aterrizar()
nave2.aterrizar()

# Despegar Naves
nave1.despegar()
nave2.despegar()

# Aterrizar Naves
nave1.aterrizar()
nave2.aterrizar()
