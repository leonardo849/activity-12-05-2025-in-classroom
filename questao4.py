somador = 0
contador = 0
while contador < 3:
    somador += int(input("manda nota aí"))
    contador+=1

media = somador / 3
print("média:", media)

if media >= 70:
    print("parabens foi aprovado")
elif media >= 50 and media < 70:
    print("ta de recuperação")
else:
    print("foi reprovado, sobrou nada pro beta")    
