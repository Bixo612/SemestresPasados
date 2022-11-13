import random

id_mun = 1
id_juz = 101
id_mult = 1001

municipalidades = ( "Puente Alto", "Pudahuel", "La Reina")

direcciones = [ "Av Daigonal", "Av Transversal", "Av Longitudinal", "Bernardo O'Higgins", "Arturo Prat", "Gabriela Mistral", "Pablo Neruda", "Vicente Huidobro",
                "Jose Miguel Carrera", "José Manuel Balmaceda", "Manuel Blanco Encalada", "Manuel Bulnes", "Joaquín Prieto", "Manuel Bulnes", "Luis Barros Borgoño",
                "Pedro Aguirre Cerda","Algarrobo","Chañar","Pacama","Queñoa","Tamarugo","Patahua","Pelu","Petra","Boldo","Bollen","Corontillo","Frangel","Maiten",
                "Molle","Petrillo"]

infraciones = [ "Conducir a exceso de velocidad","Conduccion con restricion vehicular","Infringir normas sobre viraje","No respetar señal pare","Detener o estacionar un vehículo en doble fila"
                "Sobrepasar a otro vehiculo por la berma","Conducir vehiculo sin placa patente","No respetar signos o señales de transito","No hacer las señales debidas antes de virar"
                "Conducir vehiculo en contra el sentido del transito","Conducir vehiculo sin permiso de circulacion","Conducir vehiculo sin certificado de seguro obligatorio vigente"]

vehiculos = (   ["Chevrolet", "Orlando"], ["Chevrolet", "Captiva"], ["Hyundai", "Tucson"], ["Hyundai", "Santa Fe"], ["Chevrolet", "Colorado"], ["Chevrolet", "Spin"],
                ["Suzuki", "S-Presso"], ["Suzuki", "Vitara"], ["Suzuki", "Gran Nomade"],["Ford", "F-150"],["Ford", "Bronco"],["Volkswagen", "Tiguan"],["Kia","Frontier"],
                ["Citroën","Berlingo"],["Peugeot","Partner"],["Jeep", "Wrangler"],["Jeep", "Grand Cherokee"],["Jeep", "Compass"],["Dodge", "Durango"],["Suzuki", "Samurai"],
                ["Dodge","Ram"])

inspectores = ([1, "12-06-1996", "13520500-K", "Felipe Andres Soto Diaz", "Masculino", "fasd@gamil.com", "14-10-1985", 97854053],
               [2, "12-06-1996", "13456963-1", "Sofia Andrea Roman Valdez","Femenino", "sarv@gamil.com", "14-03-1986", 945289561],
               [3, "12-06-1996", "13520630-2", "Marcos Antonio Fernandez Ilabaca","Masculino", "mafi@gamil.com", "20-02-1986", 952624540],
               [4, "12-06-1996", "13025753-3", "Valentina Macarena Valdez Zuniga","Femenino", "vmvz@gamil.com", "03-12-1990", 945786301],
               [5, "12-06-1996", "13525554-4", "Roberto Carlos Carrera Lopez", "Masculino", "rccl@gamil.com", "20-01-1989", 902047755],
               [6, "12-06-1996", "13520639-5", "Camila Antonio Valdez Zuniga", "Femenino", "cavz@gamil.com", "15-03-1987", 902048560],
               [7, "12-06-1996", "13753869-6", "Fernanda Sofia Oney Mendez", "Femenino", "fsom@gamil.com", "12-03-1988", 951963050])


def gen_direccion():
    max = len(direcciones)
    max = max-1
    ran = random.randint(0, max)
    calle = direcciones[ran]
    numero = str(random.randint(100, 9999))
    direccion = calle + " # " + numero
    return direccion


def gen_infracion():
    max = len(infraciones)
    max = max-1
    ran = random.randint(0, max)
    return infraciones[ran]


def gen_fecha():
    dia = str(random.randint(1, 31))
    mes = str(random.randint(1, 12))
    anio = str(random.randint(2020, 2022))
    return dia + "-" + mes + "-" + anio

def generarPatenteNueva():
    pat = chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + str(random.randint(0, 9))
    pat = pat + str(random.randint(0, 9))
    return pat

def gen_vehiculo():
    max = len(vehiculos)
    max = max - 1
    ran = random.randint(0, max)
    var = vehiculos[ran]
    vehi = '{"patente" : "' + generarPatenteNueva() + '", "marca":"' + \
        var[0] + '", "modelo":"' + var[1] + '"}'
    return vehi

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


print('[')
for i in municipalidades:
    print('    {')
    print('        "id_municipalidad" : ', id_mun, ',')
    print('        "comuna" : "', i, '",', sep="")
    print('        "juzgados": [')
    print('            {')
    print('                "id_juzgado" : ', id_juz, ',')
    id_juz = id_juz + 1
    print('                "nombre_juzgado" : "Primer juzgado de ', i, '",', sep="")
    print('                "multas" : [')
    print('                    {')
    print('                        "nro_multa" : ', id_mult, ',')
    print('                        "direccion" : "',gen_direccion(), '",', sep="")
    print('                        "fecha" : "', gen_fecha(), '",', sep="")
    print('                        "infracion" : "',gen_infracion(), '",', sep="")
    print('                        "vehiculo" : ', gen_vehiculo(), ',')
    print('                        "insepctor" : ', generar_inspector())
    id_mult = id_mult + 1
    print('                    },')
    print('                    {')
    print('                        "nro_multa" : ', id_mult, ',')
    print('                        "direccion" : "',gen_direccion(), '",', sep="")
    print('                        "fecha" : "', gen_fecha(), '",', sep="")
    print('                        "infracion" : "',gen_infracion(), '",', sep="")
    print('                        "vehiculo" : ', gen_vehiculo(), ',')
    print('                        "insepctor" : ', generar_inspector())
    id_mult = id_mult + 1
    print('                    }')
    print('                ]')
    print('            },')
    print('            {')
    print('                "id_juzgado" : ', id_juz, ',')
    id_juz = id_juz + 1
    print('                "nombre_juzgado" : "Segundo juzgado de ', i, '",', sep="")
    print('                "multas" : [')
    print('                    {')
    print('                        "nro_multa" : ', id_mult, ',')
    print('                        "direccion" : "',gen_direccion(), '",', sep="")
    print('                        "fecha" : "', gen_fecha(), '",', sep="")
    print('                        "infracion" : "',gen_infracion(), '",', sep="")
    print('                        "vehiculo" : ', gen_vehiculo(), ',')
    print('                        "insepctor" : ', generar_inspector())
    id_mult = id_mult + 1
    print('                    },')
    print('                    {')
    print('                        "nro_multa" : ', id_mult, ',')
    print('                        "direccion" : "',gen_direccion(), '",', sep="")
    print('                        "fecha" : "', gen_fecha(), '",', sep="")
    print('                        "infracion" : "',gen_infracion(), '",', sep="")
    print('                        "vehiculo" : ', gen_vehiculo(), ',')
    print('                        "insepctor" : ', generar_inspector())
    id_mult = id_mult + 1
    print('                    }')
    print('                ]')
    print('            }')
    print('        ]')
    id_mun = id_mun+1
    print('    },')
print(']')

input(" ")