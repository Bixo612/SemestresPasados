
import mysql.connector
con = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "blockbuster")
mycursor = con.cursor()


#Creando clase pelicula 
class Pelicula():

    def __init__(self, idPelicula, titulo,año_estreno,duracion,censura,estudio,TipoPelicula):
        self.idPelicula= idPelicula
        self.titulo= titulo
        self.año_estreno= año_estreno
        self.duracion= duracion
        self.censura= censura
        self.estudio= estudio
        self.TipoPelicula= TipoPelicula
        self.listaPelicula =[]

    def get_idPelicula(self):
        return self.idPelicula
    def set_idPelicula(self, idPelicula):
        self.idPelicula = idPelicula

    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_año_estreno(self):
        return self.año_estreno
    def set_año_estreno(self, año_estreno):
        self.año_estreno = año_estreno

    def get_duracion(self):
        return self.duracion
    def set_duracion(self, duracion):
        self.duracion = duracion

    def get_censura(self):
        return self.censura
    def set_censura(self, censura):
        self.censura = censura

    def get_estudio(self):
        return self.estudio
    def set_estudio(self, estudio):
        self.estudio = estudio

    def get_TipoPelicula(self):
        return self.TipoPelicula
    def set_TipoPelicula(self, TipoPelicula):
        self.TipoPelicula = TipoPelicula

class blockbuster():    
    def agregarPelicula(self,idPelicula,titulo,año_estreno, duracion,censura,estudio, tipoPelicula):
        idPelicula = ""
        titulo = " "
        año_estreno = 0
        duracion = 0
        censura = 0
        estudio = " "
        tipoPelicula= " "
        
        consultandoID = "SELECT MAX(idPelicula) FROM pelicula"
        mycursor.excute(consultandoID)
        idM = mycursor.fetchone()
        idR = idM[0]
        print("Primer ID: ", idR)

        idP = idR +1


        idPelicula = idP
        titulo = input("Ingrese el titulo de la pelicula: ")
        año_estreno = int(input("Ingrese el año de estreno de la pelicula: "))
        duracion = int(input("Ingrese el duracion en minutos de la pelicula: "))
        censura = int(input("Ingrese la cencura de la pelicula: "))
        tipoPelicula = input("Ingrese el tipo de pelicula: ")
        estudio= input("Ingrese el estudio que produjo la pelicula: ")


        self.set_idPelicula(idPelicula)
        self.set_titulo(titulo)
        self.set_año_estreno(año_estreno)
        self.set_duracion(duracion)
        self.set_censura(censura)
        self.set_estudio(estudio)
        self.set_TipoPelicula(tipoPelicula)

        sql= "INSERT INTO `pelicula` (`idPelicula`, `titulo`, `año_estreno`, `duracion`, `censura`, `estudio`,`tipoPelicula`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        valor= (self.get_idPelicula(),self.get_titulo(), self.get_año_estreno(), self.get_duracion(), self.get_censura(),self.get_estudio(),self.get_TipoPelicula())
        
        mycursor.execute(sql,valor)
        con.commit()

 

        

    def eliminarPelicula(self):
        sql = "Delete from pelicula where pelicula.idPelicula = %s"
        var = (id,)
        mycursor.execute(sql,var)

        con.commit()
        print(mycursor.rowcount, "record(s) deleted")

    def actualizarElTituloDeUnaPelicula(self,idPelicula):
            sql = "Update pelicula set titulo = %s where pelicula.idPelicula = %s;"
            var = (idPelicula,)
            mycursor.execute(sql,var)

    def imprimirUnaPelicula(self,idPelicula):
        sql = "Select * from pelicula where idPelicula = %s"
        var = (idPelicula,)
        mycursor.execute(sql,var)
        resultado = mycursor.fetchall()
        print (resultado)

    def imprimirTodasLasPeliculas():
        mycursor.execute("SELECT * FROM pelicula")
        resultado = mycursor.fetchall()
        for z in resultado:
            print (z)

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
salir = False
opcion = 0
 
while not salir:
    
    print("*"*50)
    print ("¡¡¡¡UN MANTENEDOR MAS!!!!".center(40, "*"))
    print ("1. Agregar una Pelicula")
    print ("2. Eliminar Pelicula ")
    print ("3. Actualizar el nombre de una película")
    print ("4. Imprimir una película")
    print ("5. Imprimir todas las película")
    print ("6. Salir\n")
    print("*"*50)
     
    print ("Elige una opcion: ")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        Pelicula.agregarPelicula()
    elif opcion == 2:
        Pelicula.eliminarPelicula()
    elif opcion == 3:
        Pelicula.actualizarElTituloDeUnaPelicula()
    elif opcion == 4:
        Pelicula.imprimirUnaPelicula()
    elif opcion == 5:
        Pelicula.imprimirTodasLasPeliculas()
    elif opcion == 6:
        salir = True
    else:
        print ("Ingreso una opción errónea. Intente nuevamente")
 
print ("Fin")


