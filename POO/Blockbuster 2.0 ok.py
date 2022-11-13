import mysql.connector

# Agregar una película
# Eliminar una película--
# Actualizar el nombre de una película. --ok
# Imprimir una película -- ok
# Imprimir todas las películas -- ok
# Salir

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="blockbuster"
    )

cursor = con.cursor()

def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

def printMenu():
    print ("Menu Blockbuster")
    print ("0 - Salir")
    print ("1 - Agregar Pelicula")
    print ("2 - Cambiar nombre de pelicula")
    print ("3 - Buscar pelicula por Id")
    print ("4 - Listar todas las peliculas")
    print ("5 - Eliminar pelicula por Id")
    print ("")

class FxSql():

    def mostrarPeliculas():
        cursor.execute("Select * from pelicula order by 1")
        resultado = cursor.fetchall()
        print ("Id Pelicula | Titulo                  | Año de estreno | Duracion | Censura | Estudio | Tipo de pelicula",sep= "" )
        for x in resultado:
             print("  {:<10}| {:<24}| {:<15}| {:<9}| {:<8}| {:<8}| {:<7}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

    def buscarPelicula(id):
        sql = "Select * from pelicula where idPelicula = %s"
        var = (id,)
        cursor.execute(sql,var)
        resultado = cursor.fetchall()
        print (resultado)

    def cambiarNombre(id,nuevo):
        sql = "Update pelicula set titulo = %s where pelicula.idPelicula = %s;"
        var = (nuevo,id,)
        cursor.execute(sql,var)

    def eliminarPelicula(id):
        sql = "Delete from pelicula where pelicula.idPelicula = %s"
        var = (id,)
        cursor.execute(sql,var)

    def obtenerUltimoId():
        cursor.execute("Select max(idPelicula) from pelicula")
        id_A = cursor.fetchone()
        # print ("Este es ultimo id de pelicula registrado")
        # print (id_A)
        # print ("Pero se encuentra dentro de una tupla")
        # print (type(id_A))
        id_B = id_A[0]
        # print ("Ahora lo sacamos de la tupla")
        # print (id_B)
        # print ("Ahora es un entero y es manipulable ")
        # print (type(id_B))
        # print (id_B + 1)
        return id_B

    def existeId(id):
        cursor.execute("Select idPelicula from pelicula")
        resultado = cursor.fetchall()
        for x in resultado:
            y = x[0]
            if id == y:
                print ("")
                return True

    def agregarPelicula(id,titulo,año,duracion,censura,estudio,tipo):
        sql = "Insert into pelicula values (%s,%s,%s,%s,%s,%s,%s)"
        var = (id,titulo,año,duracion,censura,estudio,tipo,)
        cursor.execute(sql,var)

class Pelicula():

    def __init__(self,titulo,año_estreno,duracion,censura,estudio,TipoPelicula):
        self.idPelicula     = FxSql.obtenerUltimoId() + 1
        self.titulo         = titulo
        self.año_estreno    = año_estreno
        self.duracion       = duracion
        self.cenusra        = censura
        self.estudio        = estudio
        self.TipoPelicula   = TipoPelicula

    def set_idPelicula(self,idPelicula):
        self.idPelicula = idPelicula

    def set_titulo(self,titulo):
        self.titulo = titulo

    def set_año_estreno(self,año_estreno):
        self.año_estreno = año_estreno

    def set_duracion(self,duracion):
        self.duracion = duracion

    def set_censura(self,censura):
        self.cenusra = censura

    def set_estudio(self,estudio):
        self.estudio = estudio

    def set_TipoPelicula(self,TipoPelicula):
        self.TipoPelicula = TipoPelicula

    def get_idPelicula(self):
        return self.idPelicula

    def get_titulo(self):
        return self.titulo 

    def get_año_estreno(self):
        return self.año_estreno 

    def get_duracion(self):
        return self.duracion

    def get_censura(self):
        return self.cenusra

    def get_estudio(self):
        return self.estudio 

    def get_TipoPelicula(self):
        return self.TipoPelicula

    def __str__(self) -> str:
        return "Id Pelicula {} | Titulo {} | Año de estreno {} | Duracion {} | Cenusura {} | Estudio {} | Tipo de pelicula {} |".format(
            self.get_idPelicula(),self.get_titulo(),self.get_año_estreno(),self.get_duracion(),self.get_censura(),self.get_estudio(),self.get_TipoPelicula())

class Valid():

    def crearTitulo():
        titulo = ""
        while len(titulo) == 0 or len(titulo)>100:
            titulo = input ("Ingrese el titulo de la pelicula: ")
            if len(titulo)>100:
                print ("El titulo de la pelicula debe contener maximo 100 caracteres")
        return titulo

    def crearEstudio():    
        estudio = ""
        while len(estudio) == 0 or len(estudio)>5:
            estudio = input ("Ingrese el estudio de la pelicula: ")
            if len(estudio)>5:
                print ("El estudio de la pelicula debe contener maximo 5 caracteres")
        return estudio

    def crearTipo():    
        tipo = ""
        while len(tipo) == 0 or len(tipo)>5:
            tipo = input ("Ingrese el tipo de la pelicula: ")
            if len(tipo)>5:
                print ("El tipo de la pelicula debe contener maximo 5 caracteres")
        return tipo

    def crearUnEntero(txt):
        entero = None
        while entero == None:
            entero = leerEntero(txt)
            if entero == None:
                print("Ingrese un numero valido")
        return entero

class Blockbuster():

    def crearPelicula():
        titulo = Valid.crearTitulo()
        año = Valid.crearUnEntero("Ingrese año de estreno: ")
        duracion = Valid.crearUnEntero("Ingrese la duracion de la pelicula: ")
        censrua = Valid.crearUnEntero("Ingrese la censura de la pelicula: ")
        estudio = Valid.crearEstudio()
        tipo = Valid.crearTipo()
        peli = Pelicula(titulo,año,duracion,censrua,estudio,tipo)
        return peli

    def agregarPeli(pelicula):
        FxSql.agregarPelicula(pelicula.get_idPelicula(),pelicula.get_titulo(),
        pelicula.get_año_estreno(),pelicula.get_duracion(),pelicula.get_censura(),pelicula.get_estudio(),
        pelicula.get_TipoPelicula())

def menu():

    salir = True
    op = None
    while salir:
        printMenu()
        op = leerEntero("Ingrese una opcion: ")
        print ("")
        if op == 0:
            salir = False
            print ("Hasta pronto :D")
        elif op == 1:
            #Agregar una pelicula
            pelicula = Blockbuster.crearPelicula()
            Blockbuster.agregarPeli(pelicula)
            print ("Pelicula Registrada")
            FxSql.buscarPelicula(FxSql.obtenerUltimoId())
            print("")            
        elif op == 2:
            #Cambiar nombre de pelicula
            id = leerEntero("Ingrese el codigo de la pelicula que dese modificar: ")
            if FxSql.existeId(id):
                nombre = Valid.crearTitulo()
                FxSql.cambiarNombre(id,nombre)
                print ("Datos actualizados")
                FxSql.buscarPelicula(id)
                print ("")
            else:
                print ("No existe una pelicula registrada con el codigo ",id)
            print ("") 
        elif op == 3:
            #Buscar pelicula por Id
            id = leerEntero("Ingrese el codigo que desea buscar: ")
            if FxSql.existeId(id):
                FxSql.buscarPelicula(id)
            else:
                print ("No existe una pelicula registrada con el codigo ",id)
            print ("")
        elif op == 4:
            #Listar todas las pelicuas
            FxSql.mostrarPeliculas()
            print ("")
        elif op == 5:
            #Eliminar pelicula por id
            id = leerEntero("Ingrese el codigo de la pelicula que desea eliminar: ")
            if FxSql.existeId(id):
                FxSql.eliminarPelicula(id)
                print ("Pelicula con id ",id, "eliminada")
            else:
                print ("No existe una pelicula registrada con el codigo ",id)
            print ("")
        else:
            print ("Ingrese una opcion valida entre 0 y 4")

menu()




