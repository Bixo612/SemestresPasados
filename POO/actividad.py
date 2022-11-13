def menuPrincipal():
    print ("*"*35)
    print ("Menú Principal")
    print ("1- Agregar alumno")
    print ("2- Quitar alumno")
    print ("3- Seleccionar alumno")
    print ("4- Listar Alumnos")
    print ("5- Salir")

def menuAlumno():
    print ("*"*35)
    print ("Menú Alumno")
    print ("1- Agregar nota")
    print ("2- Eliminar nota")
    print ("3- Mostrar notas")
    print ("4- Mostrar promedio de notas")
    print ("5- Volver")

def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

def agregarAlumno():
    nombre = input("Ingrese el Nombre del alumno: ")
    rut = input("Ingrse el rut:")
    return [nombre, rut] 

def eliminarAlumno():
    pass

def mostrarAlumnos(alumnos):
    print ("Nombre".center(23), "Rut".center(20),sep="")
    i=1
    for alumno in alumnos:
        nombre = alumno [0]
        rut = alumno [1]
        print (str(i).center(3), end="")
        i = i + 1
        print (f"{nombre:20s}", end="")
        print (f"{rut:20s}",)

# Codigo

salir = True
volver = True
menuP = None
listaAlumnos = []

while salir:
    menuPrincipal()
    menuP = leerEntero("Seleccione una opcion: ")
    if menuP == 1:
        alumno = agregarAlumno()
        listaAlumnos.append(alumno)
        menuP == None
    elif menuP == 2:
        eliminar = eliminarAlumno()
        menuP = None
    elif menuP == 3:
        #Seleccionar Alumno
        menuP == None
    elif menuP == 4:
        mostrarAlumnos(listaAlumnos)
        menuP == None
    elif menuP == 5:
        salir = False
    else:
        print("Debe ingresar una opcion valida")
