##Laura Sofia Henao Quintero 24426138-8
##Fabian Andree Morales Molina 18665542-7


import mysql.connector

con = mysql.connector.connect(host="localhost", user="root",password="", database="blockbuster")

cursorx = con.cursor()

class pelicula():

    def __init__(self, idPelicula, titulo, año_estreno, duracion, censura, estudio, TipoPelicula):
        self.idPelicula = idPelicula
        self.titulo = titulo
        self.año_estreno = año_estreno
        self.duracion = duracion
        self.censura = censura
        self.estudio = estudio
        self.TipoPelicula = TipoPelicula
        self.eliminada = 0
        self.id = 0


    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id


    def get_eliminada(self):
        return self.eliminada

    def get_idPelicula(self):
        return self.idPelicula

    def get_titulo(self):
        return self.titulo
    
    def get_año_estreno(self):
        return self.año_estreno

    def get_duracion(self):
        return self.duracion

    def get_censura(self):
        return self.censura

    def get_estudio(self):
        return self.estudio
    
    def get_TipoPelicula(self):
        return self.TipoPelicula      


    def set_eliminada(self, eliminada):
        self.eliminada = eliminada

    def set_idPelicula(self, idPelicula):
        self.idPelicula = idPelicula
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_año_estreno(self, año_estreno):
        self.año_estreno = año_estreno
    
    def set_censura(self, censura):
        self.censura = censura

    def set_duracion(self, duracion):
        self.duracion = duracion
    
    def set_estudio(self, estudio):
        self.estudio = estudio

    def set_TipoPelicula(self, TipoPelicula):
        self.TipoPelicula = TipoPelicula


    def crearId(self):
        
        sql = """SELECT max(idPelicula) from pelicula"""

        cursorx.execute(sql)
        resultado = cursorx.fetchone()
        self.id = (int(resultado[0])) + 1



    def agregar_pelicula(self):

              
        idPelicula = self.id
        titulo = input("ingrese titulo pelicula: " )
        año_estreno = int(input("ingrese Año de estreno: " ))
        duracion = int(input("ingrese duración pelicula: " ))
        censura = int(input("ingrese edad minima pelicula: " ))
        estudio = input("ingrese estudio de pelicula: " )
        TipoPelicula = input("ingrese tipo de pelicula: " )


        self.set_idPelicula(idPelicula)
        self.set_titulo(titulo)
        self.set_año_estreno(año_estreno)
        self.set_duracion(duracion)
        self.set_censura(censura)
        self.set_estudio(estudio)
        self.set_TipoPelicula(TipoPelicula)
       
        
        sql = "INSERT INTO `pelicula`(`idPelicula`, `titulo`, `año_estreno`, `duracion`, `censura`, `estudio`, `TipoPelicula`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (self.get_idPelicula(), self.get_titulo(), self.get_año_estreno(), self.get_duracion(), self.get_censura(), self.get_estudio(), self.get_TipoPelicula())  
        
        cursorx.execute(sql,val)
        con.commit()

        print(cursorx.rowcount, "Pelicula guardada en la BD")
        print("EL ID DE LA PELICULA REGISTRADA ES: ", idPelicula)
    
    def imprimirPeliculas(self):

        sql = """SELECT * FROM pelicula"""
        cursorx.execute(sql)
        resultado = cursorx.fetchall()

        for x in resultado:
     
            print("ID PELICULA: {:<10}   | TITULO : {:<20}  |  AÑO ESTRENO: {} |  DURACION: {} |  CENSURA: {:<8} |  ESTUDIO:  {:<7} |  TIPO DE PELIICULA:  {:<7}|".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        
        print ("Fin de Consulta")
    
    
    
    def eliminarPelicula(self):

        id = int(input("ingrese ID de pelicula a eliminar: "))

        sql = "delete FROM pelicula WHERE idPelicula = %s"
        val = (id,)
        
        cursorx.execute(sql,val)
        con.commit()
        print(cursorx.rowcount, "Pelicula ELIMINADA en la BD")

    def modificarNombre(self):

        id = int(input("ingrese ID de pelicula : "))
        nuevoTitulo = input("Ingrese nuevo titulo de pelicula: ")

        sql = "UPDATE pelicula SET titulo = %s where idPelicula = %s"
        val = (nuevoTitulo,id)
        
        cursorx.execute(sql,val)
        con.commit()
        print(cursorx.rowcount, "Pelicula Modificada en la BD")

    def buscarPelicula(self):
   
        formaBusqueda = int(input("Desea buscar por ID o TITULO (1 = ID , 2 = titulo):  "))
        if formaBusqueda == 1:
            id = int(input("ingrese ID de pelicula que quiere buscar: "))
            sql = """SELECT * FROM pelicula where idPelicula = %s"""
        elif formaBusqueda == 2:
            id = input("ingrese titulo de pelicula que quiere buscar: ")
            sql = """SELECT * FROM pelicula where titulo like %s"""
        else:
            return print("debe ser 1 o 2 la opcion valida")
        val = (id,)
        cursorx.execute(sql,val)
        resultado = cursorx.fetchall()

        
        movie = (resultado[0])
        print('*'*80,'')
        print("ID PELICULA: {}".format(movie[0]))
        print("TITULO:  {}".format(movie[1]))
        print("AÑO ESTRENO:  {}".format(movie[2]))
        print("DURACION: {}".format(movie[3]))
        print("CENSURA:  {}".format(movie[4]))
        print("ESTUDIO:  {}".format(movie[5]))
        print("TIPO DE PELIICULA:  {}".format(movie[6]))


def mostrarMenu():
    
        print("*"*80)
        print("MENU BLOCKBUSTER".center(80))
        print("*"*80)
        print("1- Agregar Pelicula")
        print("2- Eliminar Pelicula")
        print("3- Actualizar Nombre De La Pelicula")
        print("4- Imprimir una pelicula")
        print("5- Imprimir todas las peliculas")
        print("6- Salir")

def leerNumeroEntero(texto):
        try:
            return int(input(texto))
        except:
            return None

def leerOpcion():
        
        opcion = None    
        while opcion == None or opcion not in range(1,7):
            opcion = leerNumeroEntero("Ingrese opcion: ")
            if opcion == None or opcion not in range(1,7):
                print("Escoger solo opcion de 1 a 6 son las opciones disponibles.")
        return opcion



repositorioPelicula = pelicula(0,'',0,0,0,'','')

salir = False
while not salir:
    mostrarMenu()
    opcion = leerOpcion()
    if opcion == 1:
        print("*"*80)
        repositorioPelicula.crearId()
        repositorioPelicula.agregar_pelicula()
    if opcion == 2:
        repositorioPelicula.eliminarPelicula()
    elif opcion == 3:
        repositorioPelicula.modificarNombre()
    elif opcion == 4:
        repositorioPelicula.buscarPelicula()
    elif opcion == 5:
        print("*"*80)
        repositorioPelicula.imprimirPeliculas()
    elif opcion == 6:
        salir = True
       
