//La constante no puede ser modificada
const arr = ["Papa","Lechuga","Tomate"]
//let declara una variable solo permite ciertos tipos de datos y pude explicar los errores
//var recibe cualquier dato pero no te notifica el erro
let arreglo = []
for (i=0;i<15;i++){
    arreglo.push(parseInt(Math.random() * 100))
}

for (i=0;i<arreglo.length;i++){
    console.log((i+1)+". "+arreglo[i])
}

/*
llenar arreglo con 15 valores random
mostrar los datos
mostrar el primero y el utlimo
arrohas la sumatoria de los numeros 
agregar 3 valores mas
volver a mostrar el contenido
*/