class Persona {
    constructor(nombre, edad) {
        this.setNombre(nombre)
        this.setEdad(edad)
    }

    setNombre(nombre) {
        if (nombre.length > 0) {
            this.nombre = nombre
        }
        else {
            console.log('Debe ingresar un nombre')
        }
    }

    setEdad(edad) {
        if (edad >= 0 && edad <= 65) {
            this.edad = edad
        }
        else {
            console.log('Edad debe ser entre 0 y 65')
        }
    }

    printPersona() {
        console.log('Nombre: ' + this.nombre)
        console.log('Edad: ' + this.edad)

    }

}

objecto1 = new Persona("Juana",44)
objecto1.printPersona()
console.log("********************************")
objecto2 = new Persona("",89)
objecto2.printPersona()