class Persona
{
    //constructor con parametros
    constructor(nombre,genero,edad)
    {
        this.nombre = nombre
        this.genero = genero
        this.edad = edad
    }


    mostrar_informacion(){
        console.log("Nombre es:"+this.nombre)
        console.log("Genero:"+this.genero)
        console.log("Edad:"+this.edad)
    }
}

objeto = new Persona("Pedro","M",44)
objeto.mostrar_informacion()