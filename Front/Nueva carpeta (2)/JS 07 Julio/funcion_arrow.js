//Ejemplo de arrow Function

mi_funcion = () => 30

una_funcion =() => {

    valor = 50
    console.log("En una funcion arrow valor es:"+valor)
}

otra_funcion = () =>{
    //crea literalmente un objeto
    objeto = {}
    objeto.nombre = "juana"
    objeto.edad = 23
    return objeto
}


dato = otra_funcion()
console.log(dato)
console.log(mi_funcion())
una_funcion()