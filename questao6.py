kmPercorrida = float(input("quantos km passaageiro vai percorrer?"))

custoPorKM = 0
if kmPercorrida < 500:
    custoPorKM = 0.75
else:
    custoPorKM = 0.65


valorFinal = 20 + (custoPorKM * kmPercorrida)

print(f"valor final: {valorFinal}")
