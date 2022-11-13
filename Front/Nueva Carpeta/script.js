function validar() {
    // var es para defininir una variable para todas las funciones
    // let es solo para la funcion donde se declara
    let codigo = document.formulario.txt_codigo.value;
    let producto = document.formulario.opt_producto.value;
    let dimesiones = document.formulario.txt_dimensiones.value;
    let descripcion = document.formulario.txa_descripcion.value;
    let pais = document.formulario.txt_pais.value;
    let precio = document.formulario.txt_precio.value;
    let tienda = document.formulario.num_tienda.value;
    //
    if ((codigo.charAt(0) != 'A' && codigo.charAt(0) != 'H' && codigo.charAt(0) != 'X') || (codigo.length != 7)) {
        alert("Codigo debe comenzar con  A - H - X en mayusculas y con un largo de 7 caracteres");
        document.formulario.txt_codigo.focus();
        return false;
    }
    if (producto.length == 0) {
        alert("Debe selecionar un producto");
        document.formulario.txt_producto.focus();
        return false;
    }
    if (descripcion.length == 0) {
        alert("Debe ingresar una descripcion de producto");
        document.formulario.txa_descripcion.focus();
        return false;
    }
    if (dimesiones.length == 0) {
        alert("Debe ingresar las dimesiones del producto");
        document.formulario.txt_dimensiones.focus();
        return false;
    }
    //toUpperCase convierte un string a mayusculas
    //toLowerCase convierte un string a minusculas
    if (pais.toUpperCase() != "CHILE" && pais.toUpperCase() != "ARGENTINA" &&
        pais.toUpperCase() != "COLOMBIA" && pais.toUpperCase() != "BRASIL") {
        alert("Pais debe ser Chile, Colombia, Argentina o Brasil")
        document.formulario.txt_pais.focus();
        return false;
    }
    if ((parseInt(precio)) < 1000) {
        alert("Precio debe ser mayor o igual a 1000")
        document.formulario.txt_precio.focus();
        return false;
    }
    if (parseInt(tienda) < 1 || parseInt(tienda) > 7){
        alert("El numero de tienda debe ser entre 1 y 7")
        document.formulario.num_tienda.focus();
        return false
    }
        alert("Todo bien :D " + codigo)
}