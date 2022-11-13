import json

auto = '''{
    "marca": "Ford",
    "modelo": "Mustang",
    "anio": 1968,
    "colores": ["Rojo","Blanco","Azul","Negro"] 
}'''


argo = '''{
    "nombre": "Alan Brito",
    "edad": 25,
    "cargo": "Navegante",
    "habilidades": ["Cocinar","Luchar","Tocar ukulele"]
}'''



## Comando load carga el objeto como un diccionaroo

x = json.loads(auto)
print(x)
print(x["colores"])
print(x["anio"])

## comando dump pasa un dicionario a un archivo jason


class Argonauta:
    def __init__(self, nombre, cargo, edad):
        self.nombre = nombre
        self.cargo = cargo
        self.edad = edad

    def __str__(self):
        pass

pers = Argonauta("Marco","Capitan",20)

json_result = json.dumps(pers.__dict__)

x = json.loads(json_result)
print (x)

print (type(x))
