function proceso(){
    var num1=document.formulario.txt_valor_a.value;
    var num2=document.formulario.txt_valor_b.value;
    resultado = parseInt(num1) * parseInt(num2);
    alert("Multiplicacion es: "+ resultado);
}