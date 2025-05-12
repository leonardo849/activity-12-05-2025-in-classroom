import sys

valor = float(input("hey mano manda um valor aí de um produto"))
meiosDePagamento = input("meios de pagamento, a vista (AV), cartão a vista (CA) e cartão parcelado (CP)").upper()
juros = 0
resultado = 0



if (meiosDePagamento == "AV"):
    juros = 0.9
elif (meiosDePagamento == "CA"):
    juros = 0.95
elif (meiosDePagamento == "CP"):
    juros = 1
else: 
    print("não existe esse meio não mano")
    sys.exit(1)

resultado = valor*juros

print(f"valor final {resultado}")
    