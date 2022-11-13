class Persona():

    def __init__(self,rut,nombre,edad):
        self.__rut      = rut
        self.__nombre   = nombre
        self.__edad     = edad
    
    def get_nombre(self):
        return self.__nombre

    def get_rut(self):
        return self.__rut
    
    def get_edad(self):
        return self.__edad

    def set_nombre(self,nombre):
        self.__nombre = nombre
        print ("Nombre Actualizado")

    def set_rut(self,rut):
        self.__rut = rut

    def set_edad(self,edad):
        self.__edad = edad
    
    def __str__(self):
        return "Per Rut {} / Nombre {} / Edad {} ".format(self.get_rut(),self.get_nombre(),self.get_edad())

    def __st__(self):
        return "{}/{}".format(self.get_rut(),self.get_nombre())

class Empleado(Persona):

    def __init__(self, rut, nombre, edad, codDpto,dpto,valorHora,horas):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        self.__codDpto      = codDpto
        self.__dpto         = dpto  
        self.__valorHora    = valorHora
        self.__horas        = horas

    def get_codDpto(self):
        return self.__codDpto

    def get_dpto(self):
        return self.__dpto
    
    def get_valorHora(self):
        return self.__valorHora

    def get_horas(self):
        return self.__horas

    def set_codDpto(self, codDpto):
        self.__codDpto = codDpto

    def set_dpto(self, dpto):
        self.__dpto = dpto
    
    def set_valorHora(self, valorHora):
        self.__valorHora = valorHora

    def set_horas(self, horas):
        self.__horas = horas

    def sueldo(self):
        A = self.get_horas()
        B = self.get_valorHora()
        return "El valor a pagar de {} es ${}".format(self.get_nombre(),A*B)

    def correo(self):
        return "{}@{}.explotamos.com".format(self.get_nombre(),self.get_dpto())

    def correoActulizado(self,apellido):
        #correo = str(self.get_nombre(),apellido,"@",self.set_dpto(),"-",self.get_codDpto(),".explotamos.com")
        return "{}{}@{}-{}.explotamos.com".format(self.get_nombre(),apellido,self.get_dpto(),self.get_codDpto())


    def __str__(self):
        return "Emp Rut {} / Nombre {} / Edad {} / Cod Dpto {} / Dpto {} / Valor Hora ${} / Horas {}".format(self.get_rut(),self.get_nombre(),
        self.get_edad(),self.get_codDpto(),self.get_dpto(),self.get_valorHora(),self.get_horas())

class Propietario(Empleado):

    def __init__(self, rut, nombre, edad, codDpto, dpto, valorHora, horas, nacionalidad):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        super().set_codDpto(codDpto)
        super().set_dpto(dpto)
        super().set_valorHora(valorHora)
        super().set_horas(horas)
        self.__nacionalidad = nacionalidad

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self,nacionalidad):
        self.__nacionalidad = nacionalidad

    def __str__(self):
        return "Prp Rut{} / Nombre {} / Edad {} / Cod Dpto {} / Dpto {} / Valor Hora {} /Horas {} / Nacionalidad {}".format(self.get_rut(),self.get_nombre(),
        self.get_edad(),self.get_codDpto(),self.get_dpto(),self.get_valorHora(),self.get_horas(),self.get_nacionalidad())

class Ingeniero(Empleado):

    def __init__(self, rut, nombre, edad, codDpto, dpto, valorHora, horas, bonoProduccion):
        super().set_rut(rut)
        super().set_nombre(nombre)
        super().set_edad(edad)
        super().set_codDpto(codDpto)
        super().set_dpto(dpto)
        super().set_valorHora(valorHora)
        super().set_horas(horas)
        self.__bonoProduccion = bonoProduccion

    def get_bonoProduccion(self):
        return self.__bonoProduccion

    def set_bonoProduccion(self, bonoProduccion):
        self.__bonoProduccion = bonoProduccion

    def sueldo(self):
        A = self.get_horas()
        B = self.get_valorHora()
        C = self.get_bonoProduccion()
        return "El valor a pagar de {} es ${}".format(self.get_nombre(),(A*B)+C)

    def __str__(self): 
        return "Ing Rut{} / Nombre {} / Edad {} / Cod Dpto {} / Dpto {} / Valor Hora {} /Horas {} / Bono produccion ${}".format(self.get_rut(),self.get_nombre(),
        self.get_edad(),self.get_codDpto(),self.get_dpto(),self.get_valorHora(),self.get_horas(),self.get_bonoProduccion())

class Administrativo(Empleado):

    def __init__(self, rut, nombre, edad, codDpto, dpto, valorHora, horas, horasExt):
        super().__init__(rut, nombre, edad, codDpto, dpto, valorHora, horas)
        self.__horasExt = horasExt

    def get_horasExt(self):
        return self.__horasExt

    def set_horasExt(self, horasExt):
        self.__horasExt = horasExt

    def sueldo(self):
        A = self.get_horas()
        B = self.get_valorHora()
        C = self.get_horasExt()
        D = (A*B)+(C*(B*1.5))
        return "El valor a pagar de {} es ${}".format(self.get_nombre(),D)

    def __str__(self): 
        return "Adm Rut{} / Nombre {} / Edad {} / Cod Dpto {} / Dpto {} / Valor Hora {} /Horas {} / Horas Extras {}".format(self.get_rut(),self.get_nombre(),
        self.get_edad(),self.get_codDpto(),self.get_dpto(),self.get_valorHora(),self.get_horas(),self.get_horasExt())


esp = "======="

print(esp)
Per = Persona(19360397,"Vicente",25)
print(Per)
print(esp)
Emp = Empleado(20123456,"Alan",20,102,"Ventas",1500,60)
print(Emp)
print(esp)
Pro = Propietario(18456753,"Marco",30,101,"Gerencia",2000,50,"Chino")
print(Pro)
print(esp)
Ing = Ingeniero(17654321,"Joaquin",30,103,"Contabiliad",1500,60,20000)
print(Ing)
print(esp)
Adm = Administrativo(15974365,"Sofia",35,102,"Ventas",1500,60,5)
print(Adm)
print(esp)

print(Emp.sueldo())
print(Pro.sueldo())
print(Ing.sueldo())
print(Adm.sueldo())

#print(Emp.correo())
print(Pro.correo())
print(Ing.correo())
print(Adm.correo())

print(esp)
print(esp)
print(esp)

print(Per.__st__())
print(Per.__str__())

print(esp)
print(esp)
print(esp)

print (Ing.correoActulizado("Lopez"))

