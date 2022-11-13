
x = 1000

pesoTOdolar =(peso)=>{
    dolar = peso * 0.00099
    return dolar
}

pesoTOeuro =(peso)=>{
    euro = peso * 0.00095
    return euro
}

pesoTOyen =(peso)=>{
    yen = peso * 0.13
    return yen
}


console.log(pesoTOdolar(x))
console.log(pesoTOeuro(x))
console.log(pesoTOyen(x))