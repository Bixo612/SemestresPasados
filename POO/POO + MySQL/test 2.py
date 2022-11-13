def printMenu():
    print ("Menu Blockbuster")
    print ("0 - Salir")
    print ("1 - Agregar Pelicula")
    print ("2 - Cambiar nombre de pelicula")
    print ("3 - Buscar pelicula por codigo")
    print ("4 - Listar todas las peliculas")

salir = True
while salir:
    printMenu()
    op = input("Ingrese una opcion: ")
    if op == 0:
        salir = False
    elif op == 1:
        #Agregar una pelicula
        pass
    elif op == 2:
        #Cambiar nombre de pelicula
        pass
    elif op == 3:
        #Buscar Pelicula por codigo
        pass
    elif op == 4:
        #Listar todas las pelicuas
        print ("asdas4")
        # mostrarPeliculas()
    else:
        print ("Ingrese una opcion valida entre 0 y 4")