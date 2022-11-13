class persona:

    def __init__(self, rut, nombre, edad):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad

    def set_rut(self, rut):
        self.rut = rut
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_edad(self, edad):
        self.edad = edad

    def get_rut(self):
        return self.rut
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad

    def __str__(self):
        return "Nombre: {},rut: {}, edad: {} Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), type(self).__name__)

class empleado(persona):
    def __init__(self, rut, nombre, edad, cdodepto, depto, valorhora, horas):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        self.cdodepto = cdodepto
        self.depto = depto
        self.valorhora = valorhora
        self.horas = horas

    def set_cdodepto(self, cdodepto):
        self.cdodepto=cdodepto
    def set_depto(self, depto):
        self.depto=depto
    def set_valorhora(self, valorhora):
        self.valorhora=valorhora
    def set_horas(self, horas):
        self.horas=horas
    
    def get_cdodepto(self):
        return self.cdodepto
    def get_depto(self):
        return self.depto
    def get_valorhora(self):
        return self.valorhora
    def get_horas(self):
        return self.horas
    
    def __str__(self):
        return "Nombre: {} | rut {} | edad: {} | Departamento: {} | Horas : {} | Valor horas: {} | Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), self.get_depto(), self.get_horas(), self.get_valorhora(), type(self).__name__)

    def sueldo(self):
        A = self.get_horas()
        B = self.get_valorhora()
        return "El sueldo liquido a pagar a {} es ${} pesos".format(self.get_nombre(),A*B)

    def correo(self):
        return "Email : {}@{}.explotamos.com".format(self.get_nombre(),self.get_depto())

class propietario(empleado):
    def __init__(self, rut, nombre, edad, cdodepto, depto, valorhora, horas, nacionalidad):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        super().set_cdodepto(cdodepto)
        super().set_depto(depto)
        super().set_valorhora(valorhora)
        super().set_horas(horas)
        self.nacionalidad = nacionalidad
    
    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def get_nacionalidad(self):
        return self.nacionalidad

    def __str__(self):
        return "Nombre: {} | rut: {} | edad: {} | Departamento: {} | Horas : {} | Valor horas: {} | Nacionalidad: {} | Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), self.get_depto(), self.get_horas(), self.get_valorhora(), self.get_nacionalidad(), type(self).__name__)

class ingeniero(empleado):
    def __init__(self, rut, nombre, edad, cdodepto, depto, valorhora, horas, bonoproduccion):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        super().set_cdodepto(cdodepto)
        super().set_depto(depto)
        super().set_valorhora(valorhora)
        super().set_horas(horas)
        self.bonoproduccion = bonoproduccion
    
    def set_bonoproduccion(self, bonoproduccion):
        self.bonoproduccion = bonoproduccion
    def get_bonoproduccion(self):
        return self.bonoproduccion

    def sueldo(self):
        A = self.get_horas()
        B = self.get_valorhora()
        C = self.get_bonoproduccion()
        return "El sueldo liquido a pagar a {} es de ${} pesos".format(self.get_nombre(),(A*B)+C)

    def __str__(self):
        return "Nombre: {} | rut: {} | edad: {} | Departamento: {} | Horas : {} | Valor horas: {} |bono produccion: {}| Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), self.get_depto(), self.get_horas(), self.get_valorhora(),self.get_bonoproduccion(), type(self).__name__)

class administrativo(empleado):
    def __init__(self, rut, nombre, edad, cdodepto, depto, valorhora, horas, horasextras):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        super().set_cdodepto(cdodepto)
        super().set_depto(depto)
        super().set_valorhora(valorhora)
        super().set_horas(horas)
        self.horasextras = horasextras

    def set_horasExtras(self,horasextras):
        self.horasextras=horasextras
    def get_horasextras(self):
        return self.horasextras

    def sueldo(self):
        A = self.get_horas()
        B = self.get_valorhora()
        C = self.get_horasextras()
        return "El sueldo liquido a pagar a {} es de ${} pesos".format(self.get_nombre(),(A*B)+(A*1.5))

    def __str__(self):
        return "Nombre: {} | rut: {} | edad: {} | Departamento: {} | cantidad horas : {} | Valor horas: {} | valor horaextras: {} | Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), self.get_depto(),self.get_horas(), self.get_valorhora(),self.get_horasextras(), type(self).__name__)

espacio = ("________")
print(espacio)

prueba = persona(16127552, "richard", 35)
print(prueba)
print(espacio)
pruebaempleado = empleado(17390088, "julio", 31, 34, "Ventas", 4000, 60)
print(pruebaempleado)
print(espacio)
pruebaPropietario = propietario(27101260, "negid", 99, 34, "gerencia", 7000, 30, "Venezolano")
print(pruebaPropietario)
print(pruebaPropietario.sueldo())
print(pruebaPropietario.correo())
print(espacio)
pruebaIngeniero = ingeniero(1475145, "ricardo", 80, 233 ,"ejecutivo", 8000, 30, 1000)
print(pruebaIngeniero)
print(pruebaIngeniero.sueldo())  
print(pruebaIngeniero.correo())
print(espacio)
pruebaAdministrativo = administrativo(1475145, "juan", 30, 36 ,"administracion", 9000, 30, 2000)
print(pruebaAdministrativo)
print(pruebaAdministrativo.sueldo())
print(pruebaAdministrativo.correo())