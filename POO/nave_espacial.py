class nave:
    def __init__(self):
        self.nombre = ""
        self.cargaMaxima = 100
        self.carga = 0
        self.volando = False
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre
    def set_despega(self, despega):
        self.despega = despega
    def get_despega(self):
        return self.despega
    def set_aterriza(self, aterriza):
        self.aterriza = aterriza
    def get_aterriza(self):
        return self.aterriza
    def set_carga(self, carga):
        self.carga = carga
    def get_carga(self):
        return self.carga
    def set_descarga(self, descarga):
        self.descarga = descarga
    def get_descarga(self):
        return self.descarga

naveA = nave()
naveB = nave()

naveA.set_nombre("starfox")
naveB.set_nombre("Milano")

def despegar(self):
    if self.volando == True:
        print("la nave se encuentra en vuelo")
    if self.carga > self.cargaMaxima:
        print("la nave no puede despegar debido a que ha superado el limite de carga")
    else:
        print("despegando...")
        print("la nave ha despegado exitosamente")

def aterrizar(self):
    if self.volando == False:
        if self.carga > self.cargaMaxima:    
            print("La nave lleva demasiado peso, peligro!, afirmate Juan!!")
            print("la nave ah explotado")
    else:
        print("la nave ha aterrizado exitosamente")
    
def cargar(self):
    if self.volando == True:
        print("necesita estar en tierra para cargar")
    else:
        print("cargando...")
    
def descargar(self):
    if self.volando == True:
        print("necesita estar en tierra para descargar")
    else:
        print("descargando")

