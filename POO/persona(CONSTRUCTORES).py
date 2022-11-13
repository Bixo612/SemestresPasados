class persona:
    def __init__(self):
        self.nombre = ""

    def set_nombre(self, nombre):
        self.nombre=nombre
    
    def get_nombre(self):
        return self.nombre


class estudiante:


    def __init__(self, nombre, apellido, carrera):
        self.nombre=nombre
        self.apellido=apellido
        self.carrera=carrera

    def __str__(self):
      return "Nombre es:" + self.nombre + " " + self.apellido



alumno = estudiante("Fabian","Morales","ing Informatica")



print(alumno)

personaA = persona()
persona.set_nombre = "test"
print(personaA)
personaB = persona()
persona.set_nombre = "test"
print(personaB)

