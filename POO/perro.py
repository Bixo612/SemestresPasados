class perro:
    #Todos los perros van al cielo
    def __init__(self):
        self.nombre=""
        self.ladra=0

    def set_nombre(self, nombre):
        self.nombre=nombre

    def get_nombre(self):
        return self.nombre

    def set_ladra(self, ladra):
        self.ladra=ladra
    
    def ladrar(self):
        pass

perroA = perro()
perroB = perro()

perroA.set_nombre("Palta")
perroB.set_nombre("Tuna")

print(perroB.get_nombre())
print(perroA.get_nombre())


