import random

vehiculos = (["Chevrolet", "Orlando"], ["Chevrolet", "Captiva"], ["Hyundai", "Tucson"], ["Hyundai", "Santa Fe"],
             ["Chevrolet", "Colorado"], ["Chevrolet", "Spin"], ["Suzuki", "S-Presso"], ["Suzuki", "Vitara"], ["Suzuki", "Gran Nomade"])


def generarPatenteNueva():
    pat = chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + str(random.randint(0, 9))
    pat = pat + str(random.randint(0, 9))
    return pat


def generarVehiculo():
    max = len(vehiculos)
    max = max - 1
    ran = random.randint(0, max)
    var = vehiculos[ran]
    vehi = '{"patente" : "' + generarPatenteNueva() + '", "marca":"' + \
        var[0] + '", "modelo":"' + var[1] + '"}'
    return vehi


inspectores = ([1, "12-06-1996", "13520500-K", "Felipe Andres Soto Diaz",
        "Masculino", "fasd@gamil.com", "14-10-1985", 97854053],
    [2, "12-06-1996", "13456963-1", "Sofia Andrea Roman Valdez",
        "Femenino", "sarv@gamil.com", "14-03-1986", 945289561],
    [3, "12-06-1996", "13520630-2", "Marcos Antonio Fernandez Ilabaca",
        "Masculino", "mafi@gamil.com", "20-02-1986", 952624540],
    [4, "12-06-1996", "13025753-3", "Valentina Macarena Valdez Zuniga",
        "Femenino", "vmvz@gamil.com", "03-12-1990", 945786301],
    [5, "12-06-1996", "13525554-4", "Roberto Carlos Carrera Lopez",
        "Masculino", "rccl@gamil.com", "20-01-1989", 902047755])


def generar_inspector():
    max = len(inspectores)
    max = max - 1
    ran = random.randint(0, max)
    var = inspectores[ran]
    funci = '{"id_inspector": ' + str(var[0]) + ', "fecha_ingreso" : "' + var[1] + '" , "funcionario_municipal" : { "rut" : "' + var[2] + '" , "nombre" : "' + \
        var[3] + '" , "sexo" : "' + var[4] + '" , "correo" : "' + var[5] + \
        '" , "fecha_nacimiento" : "' + \
        var[6] + '" , "telefono" : ' + str(var[7]) + '}}'
    return funci
