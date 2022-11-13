class cuenta:
    def __init__(self):
        self.numero=0
        self.valor=0

    def set_numero(self, numero):
        self.numero = numero
    
    def get_numero(self):
        return self.numero

    def carga(self,numero):
        self.valor = self.valor + numero

class cuentaAhorro(cuenta):
    def __init__(self):
        super().__init__()