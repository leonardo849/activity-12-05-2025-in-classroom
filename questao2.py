peso = float(input("mande teu peso"))
altura = float(input("manda tua altura em metros"))
imc = peso / (altura ** 2)

if imc <18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("peso normal")
elif imc >= 25 and imc < 30:
    print("sobrepeso")
elif imc >= 30 and imc < 35:
    print("obesidade grau I")
elif imc >= 35 and imc < 40:
    print("obesidade grau II")
elif imc >= 40:
    print("obesidade grau III")


