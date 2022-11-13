class persona():
    def __init__(self):
        self.nombre=""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

class estudiante():
    def __init__(self,nombre,apellido,carrera):
        self.nombre=nombre
        self.apellido=apellido
        self.carrera=carrera

    def __str__(self):
        return "Nombre es: " + self.nombre + " " + self.apellido + " / "+ self.carrera

alumno1 = estudiante("Alan","Brito","Veterinaria")

persona1 = persona()
persona1.set_nombre("Juanito")
persona2 = persona()
persona2.set_nombre("Juanito")

print (alumno1)
print (persona1)
print (persona2)


