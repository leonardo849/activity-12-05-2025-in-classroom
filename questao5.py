import sys

meses = ["Jan", "Fev", "Marc", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
numeroDoMes = int(input("mes de qual numero voce quer"))

if (numeroDoMes > 12):
    print("coloque um mes valido ")
    sys.exit(1)

print(meses[numeroDoMes - 1])
