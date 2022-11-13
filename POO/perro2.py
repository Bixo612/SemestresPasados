class perro:

    def __init__(self):
        self.nombre="-"
        self.ladra=False
        self.edad=0
        

    def asignar_nombre(self, nombre):
        self.nombre=nombre

    def get_nombre(self):
        return self.nombre
    
    def set_ladra(self, ladra):
        self.ladra=ladra

    def ladrar(self):
        if self.ladra != True:
            return ("...")
        else:   
            return ("{}: GRRRR GUUAAU GUUUAAAUU".format(self.get_nombre()))

print ("creamos los objetos")

perroA = perro()
perroB = perro()

print ("Les preguntamos los nombres a nuestros Perros")

print(perroA.get_nombre())
print(perroB.get_nombre())

print("aun no tienen nombre po")
print("ahora les pondremos nombre ")

perroA.asignar_nombre("Blackie")
perroB.asignar_nombre("Lana")

print(perroA.get_nombre())
print(perroB.get_nombre())

print(perroA.ladrar())
print(perroB.ladrar())

perroB.set_ladra(True)

print(perroA.ladrar())
print(perroB.ladrar())