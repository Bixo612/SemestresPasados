var rut = "12.45678-9"

if (rut.length < 9 || rut.length > 10) {
    console.log("El largo del rut debe ser entre 9 y 10 caracteres")
}
if(rut.indexOf(".")>-1 ){
    console.log("El rut no debe contener puntos")
}
if(rut.lastIndexOf("-")<0){
    console.log("El rut debe llevar guion")
}




var numero = "91-23"

if (isNaN(numero)){
    console.log("Solo se permiten caracteres numericos")
}
if (numero.indexOf("+")>-1){
    console.log("Solo se permiten caracteres numericos")
}
if (numero.indexOf("9")!=0){
    console.log("El numero debe comenzar con 9")
}