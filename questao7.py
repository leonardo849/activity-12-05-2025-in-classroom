import sys

A = int(input("mande um numero"))
B = int(input("mande outro "))
resultado = 0


if A % 2 == 0 and B % 2 == 0:
    resultado = A * B
elif A % 2 != 0 and B % 2 != 0:
    resultado = A + B
else:
    if A % 2 == 0:
        print("A é par")
    else:
        print("b é par")
    sys.exit(0)

print(resultado)
