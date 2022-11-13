lista1 = ["Rojo", "Amarillo", "Verde", "Azul"]
lista2 = ["Rojo", "Blanco", "Negro", "Azul"]

for (i = 0; i < lista1.length; i++) {
    for (j = 0; j < lista2.length; j++) {
        //console.log(lista1[i] + lista2[j])
        if (lista1[i] == lista2[j]) {
            console.log(lista1[i] + lista2[j])
        }
    }
}

//tambien se puede usar la función forEach()

console.log(":)")
