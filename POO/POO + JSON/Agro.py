import json
#abrimos el archivo json con permisos de lectura

f = open('D:\VCS Codes\Json\Argonautas.json')

data = json.loads(f.read())

for x in data["argonautas"]:
    print (x)

with open("argo2.json","w") as file:
    json.dump(data, file , indent=5)

f.close()