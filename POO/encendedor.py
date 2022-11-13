class encendedor:

    def __init__(self):
        self.nombre=""
        self.encendido=True

    def on_off(self):
        if self.encendido==True:
            self.encendido = False
            #print ("Encendedor ",self.nombre," Apagado")
        else:
            self.encendido = True
            #print ("Encendedor ",self.nombre," Encendido")

    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

print ("Crear Objetos")

encendedor1 = encendedor()
encendedor2 = encendedor()

encendedor2.set_nombre("Palta")
encendedor1.set_nombre("Melon")

encendedor2.on_off()
encendedor1.on_off()
encendedor1.on_off()



    