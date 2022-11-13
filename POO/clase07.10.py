class Zapateria:
    def __init__(self,codArt,descripcionArt,percioArt,cantidadArt,descuentoArt):
        #self.nombre= nom
        self.codArt = codArt
        self.descripcionArt = descripcionArt
        self.percioArt = percioArt
        self.cantidadArt = cantidadArt
        self.descuentoArt = descuentoArt
    
    #def set_nom(self,nom):
     #   self.nom=nom
    def set_codArt(self,codArt):
        self.codArt=codArt 
    def set_descripcionArt(self,descripcionArt):
        self.descripcionArt=descripcionArt
    def set_percioArt(self,percioArt):
        self.percioArt=percioArt  
    def set_cantidadArt(self,cantidadArt):
        self.cantidadArt=cantidadArt
    def set_descuentoArt(self,descuentoArt):
        self.descuentoArt=descuentoArt  
    
    #def get_nom(self):
    #    return self.nom
    def get_codArt(self):
        return self.codArt
    def get_descripcionArt(self):
        return self.descripcionArt
    def get_percioArt(self):
        return self.percioArt    
    def get_cantidadArt(self):
        return self.cantidadArt
    def get_descuentoArt(self):
        return self.descuentoArt

    def __str__(self):
        txt= "El aticulo  tiene el codigo {} - descripcion {} - precio {} - cantidad {} - descuento {}"
        return txt.format(self.get_codArt(), self.get_descripcionArt(), self.get_percioArt(), self.get_cantidadArt(), self.get_descuentoArt(),type(self).__name__)


    def precio(self):
        while self.get_precioArt() <  7000:
            if self.get_precioArt() <  7000:
                print("Error!, el precio debe ser mayor a $7000")
            else:
                return self.get_percioArt(), "Es el precio del producto"

    def cantidad(self):
        while self.get_cantidadArt() <= 0:
            if self.get_cantidadArt() <= 0:
                print("Erro!!, La cantidad de articulos no puede ser 0")
            else:
                return self.get_cantidadArt(), "es la cantidad de Articulos"
        
    def codigoArt(self):
        while self.get_codigoArt() > 999 and self.codigoArt < 7999:
            if self.get_codigoArt() > 999 and self.codigoArt < 7999:
                print("Error!!... El codigo debe ser numerico entre 999 y 7999")
            else:
                return self.get_codArt(), "Es el codigo del producto"

    def descuentosArt(self):
        if self.get_descuentoArt() != False:
            x= self.get_percioArt()
            y= (x*0.20)
            return "El precio del articulo con descuento es {}".format(x-y)
        else:
            return "Que lastima, no hay descuentos disponible"


    

class Vendedor(Zapateria):
    def __init__(self,codArt,descripcionArt,percioArt,cantidadArt,descuentoArt,nombreVendedor):
        super().__init__(codArt,descripcionArt,percioArt,cantidadArt,descuentoArt)
        self.nombreVendedor=nombreVendedor

    def set_nombreVendedor(self,nombreVendedor):
        self.nombreVendedor=nombreVendedor  
    
    def get_nombreVendedor(self):
        return self.nombreVendedor

    def ventas(self):
        pass

zap= Zapateria(11,"rojos",34,1,False)
print(zap)

#print(zap.descuentoArt())
print(zap.cantidadArt())