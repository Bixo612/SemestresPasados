class persona():

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
        return "Nombre {}, {} rut, edad {} Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), type(self).__name__)


class empleado(persona):
    
    def __init__(self, rut, nombre, edad, cdodepto, dpto, valorhora, horas):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        self.cdodepto = cdodepto
        self.dpto = dpto
        self.valorhora = valorhora
        self.horas = horas
        
    def set_cdodepto(self, cdodepto):
        self.cdodepto = cdodepto

    def set_dpto(self, dpto):
        self.dpto = dpto

    def set_valorhora(self, valorhora):
        self.valorhora = valorhora

    def set_horas(self, horas):
        self.horas = horas

    def get_cdodepto(self):
        return self.cdodepto
    def get_dpto(self):
        return self.dpto
    def get_valorhora(self):
        return self.valorhora        
    def get_horas(self):
        return self.horas

    def __str__(self):
        return "Nombre {}, {} rut, edad {}, Departamento: {}  Valor horas: {}, Puesto Trabajo: {}".format(self.get_nombre(), self.get_rut(), self.get_edad(), self.get_dpto(), self.get_valorhora(), type(self).__name__)


class propietario(empleado):
    def __init__(self, rut, nombre, edad, codDepto, depto, valorHora, horas, nacionalidad):
        super().rut=rut
        super().nombre= nombre
        super().edad=edad
        super().codDepto=codDepto
        super().depto=depto
        super().valorHora=valorHora
        super().horas=horas
        self.nacionalidad=nacionalidad

        def set_nacionalidad(self, nacionalidad):
            self.nacionalidad=nacionalidad  
    
        def get_nacionalidad(self):
            return self.nacionalidad

class ingeniero(empleado):

    def __init__(self, rut, nombre, edad, cdodepto, depto, valorhora, horas,  bonoproduccion):

        super().rut = rut
        super().nombre = nombre
        super().edad = edad
        super().cdodepto = cdodepto
        super().depto = depto
        super().valorhora = valorhora
        super().hora = horas
        self.bonoproduccion = bonoproduccion

        def set_bonoproduccion(self, bonoproduccion):
            self.bonoproduccion=bonoproduccion
        def get_bonoproduccion(self):
            return self.bonoproduccion


class administrativo(empleado):

    def _init_(self, rut, nombre, edad, codDepto, depto, valorHora, horas, horasExtras):
        super().rut=rut
        super().nombre= nombre
        super().edad=edad
        super().codDepto=codDepto
        super().depto=depto
        super().valorHora=valorHora
        super().horas=horas
        self.horasExtras=horasExtras

        def set_horasExtras(self,horasExtras):
            self.horasExtras=horasExtras

        def get_horasExtras(self):
         return self.horasExtras


prueba = persona(16127552, "richard", 35)
print(prueba)

pruebaempleado = empleado(17390088, "julio", 31, 34, "Ventas", 4000, 60)
print(pruebaempleado)