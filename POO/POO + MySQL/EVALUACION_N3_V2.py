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



#Creando procesos pelicula
class blockbuster():  

    def crearPelicula():
        
        consultandoID = "SELECT MAX(idPelicula) FROM pelicula"
        mycursor.execute(consultandoID)
        idM = mycursor.fetchone()
        idR = idM[0]
        # print("Primer ID: ", idR)
        idP = idR +1

        titulo = input("Ingrese el titulo de la pelicula: ")
        if len(titulo) > 101:
            print ("Cantidad invalida de caracteres, recuerde que son 100 letras")
            titulo = input("Ingrese el titulo de la pelicula: ")
        else:
            print("Titulo ", titulo , "registrado correctamente")
        año_estreno = int(input("Ingrese el año de estreno de la pelicula: "))
        duracion = int(input("Ingrese el duracion en minutos de la pelicula: "))
        censura = int(input("Ingrese la cencura de la pelicula: "))
        tipoPelicula= input("Ingrese el tipo de pelicula: ")
        if len(tipoPelicula) > 5:
            print ("Cantidad invalida de caracteres, recuerde que son 5 letras")
            tipoPelicula= input("Ingrese el tipo de pelicula: ")
        else:
            print(tipoPelicula) 

        estudio= input("Ingrese el estudio que produjo la pelicula: ")
        if len(estudio) > 5:
            print ("Cantidad invalida de caracteres, recuerde que son 5 letras")
            estudio= input("Ingrese el estudio que produjo la pelicula: ")

        else:
            print(estudio) 

        print("-"*50)
        print("¡Pelicula agregada con exito!".center(40, "*"))
        print("-"*50)


        peli = Pelicula(idP,titulo,año_estreno,duracion,censura,tipoPelicula,estudio)
        return peli

    def agregarPelicula(pelicula):

        sql= "INSERT INTO pelicula VALUES (%s,%s,%s,%s,%s,%s,%s)"
        valor= (pelicula.get_idPelicula(),pelicula.get_titulo(), pelicula.get_año_estreno(), pelicula.get_duracion(), pelicula.get_censura(),pelicula.get_estudio(),pelicula.get_TipoPelicula(),)        
        mycursor.execute(sql,valor)

    def eliminarPelicula(id):
        sql = "Delete from pelicula where pelicula.idPelicula = %s"
        var = (id,)
        mycursor.execute(sql,var)

        con.commit()
        print(mycursor.rowcount, "Se ha borrado la pelicula con exito")

    def actualizarElTituloDeUnaPelicula(nuevo,idPelicula):
            sql = "Update pelicula set titulo = %s where pelicula.idPelicula = %s;"
            var = (nuevo,idPelicula,)
            mycursor.execute(sql,var)

    def imprimirUnaPelicula(idPelicula):
        sql = "Select * from pelicula where idPelicula = %s"
        var = (idPelicula,)
        mycursor.execute(sql,var)
        resultado = mycursor.fetchone()
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
    print ("1. Agregar una Pelicula".center(40, "*"))
    print ("2. Eliminar Pelicula ".center(40, "*"))
    print ("3. Actualizar el nombre de una película".center(48, "*"))
    print ("4. Imprimir una película".center(40, "*"))
    print ("5. Imprimir todas las película".center(50, "*"))
    print ("6. Salir".center(40, "*"))
    print()     
    print ("Elige una opcion: ")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        x = blockbuster.crearPelicula()
        blockbuster.agregarPelicula(x)
    elif opcion == 2:
        id = pedirNumeroEntero()
        blockbuster.eliminarPelicula(id)
    elif opcion == 3:
        id = pedirNumeroEntero()
        nuevo = input("Ingrese el nuevo nombre para la pelicula: ")
        blockbuster.actualizarElTituloDeUnaPelicula(nuevo,id)
    elif opcion == 4:
        id = pedirNumeroEntero()
        blockbuster.imprimirUnaPelicula(id)
    elif opcion == 5:
        blockbuster.imprimirTodasLasPeliculas()
    elif opcion == 6:
        salir = True
    else:
        print ("Ingreso una opción errónea. Intente nuevamente")
        
print("*"*50)
print ("¡Fin!.center(40, "*")")
print("*"*50)


#Negid Inati Matheus, Rut: 27.101.260-8