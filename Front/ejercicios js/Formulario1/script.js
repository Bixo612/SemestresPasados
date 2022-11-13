function validar() {
    var codigo = document.formulario.txt_codigo.value;
    var tienda = document.formulario.num_tienda.value;
    var precio = document.formulario.txt_precio.value;
    if ((codigo.charAt(0) != 'A' && codigo.charAt(0) != 'X' && codigo.charAt(0) != 'H') || codigo.length != 7) {
        alert("El codigo debe comenzar con A, H o X mayuscula y contener 7 caracteres");
        document.formulario.txt_codigo.focus()
        return false;
    }
    if (parseInt(tienda) < 1 || parseInt(tienda) > 7) {
        alert("Debe ingresar un numero entre 1 y 7");
        document.formulario.num_tienda.focus();
        return false;
    }
    if (parseInt(precio) <= 1000) {

    }

}