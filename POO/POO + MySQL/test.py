def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

class Validaciones():

    def crearIdZapato(self):
        id = None
        while id == None:
            id = leerEntero("Ingrese un Id de zapato entre 999 a 7999")
            if id != None:
                if id <999 or id >7999:
                    print("Id no valido")
                    id = None
        return id




# def crearIdZapato():
#     cod = None
#     while cod < 999 or cod > 7999:
#         cod = leerEntero("Ingrese un id zapato entre 999 a 7999: ")
#         if cod < 999 or cod > 7999:
#             print ("id zapato invalido intentelo nuevamente")
#         else:
#             print ("id zapato ",cod," registrado correctamente ")
#     return cod
    
        # desc = str(input("ingrese Nombre  "))
     
        # while pre < 7000 :
        #     pre = int(input("Ingrese un precio desde $7.000: "))
        #     if pre < 7000:
        #         print ("Precio invalido intentelo nuevamente")
        #     else:
        #         print ("Precio ",pre," registrado correctamente")
   
           
        # while cant <= 0 :
        #     cant = int(input("Ingrese un cantidad: "))
        #     if cant <= 0:
        #         print ("Cantidad invalido intentelo nuevamente")
        #     else:
        #         print ("Cantidad  " ,cant,"  registrado correctamente")

def crearIdZapato():        
    id = None
    while id == None:
        id = leerEntero("Ingrese un Id de zapato entre 999 a 7999:\n")
        if id != None:
            if id <999 or id >7999:
                print("Id no valido")
                id = None
    return id

print (crearIdZapato())