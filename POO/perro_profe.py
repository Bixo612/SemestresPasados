class perro:

    def __init__(self):
        self.nombre=""
        self.ladra=False

    def set_nombre(self, nombre):
        self.nombre=nombre

    def get_nombre(self):
        return self.nombre

    def set_ladra(self, ladra):
        self.ladra=ladra

    def ladrar(self):
        if self.ladra == True:
            return ("    ")
        else:   
            return ("GRRRR GUUAAU GUUUAAAUU")

print ("creamos los objetos")

perroA = perro()
perroB = perro()

print ("Les preguntamos los nombres a nuestros Perros")

print(perroA.get_nombre())
print(perroB.get_nombre())

print("aun no tienen nombre po")
print("ahora les pondremos nombre ")

perroA.set_nombre("Blackie")
perroB.set_nombre("Lana")

print ("Les preguntamos los nombres a nuestros Perros otra vez")

print(perroA.get_nombre())
print(perroB.get_nombre())

print("Lana es una perra buena para ladrar")

perroB.set_ladra(True)

print("pasa un gato!!! quien ladra?")

print(perroA.ladrar())
print(perroB.ladrar())
