function calcular_area()
{
    var radio = document.form_area_circulo.number_radio
    area = parseFloat( 2 * radio * Math.PI )
    document.form_area_circulo.txt_resultado_radio.value = area
}

function calcular_imc() {
    var peso = document.form_imc.number_estatura
    var estatura = document.form.number_peso
    imc = peso/(estatura*estatura)
    document.form_imc.txt_resultado_IMC.value = imc
} 