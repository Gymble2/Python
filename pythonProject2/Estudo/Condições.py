from random import randint

numero_ale= randint(0, 5)
print(numero_ale)
a = int(input("Digite o valor adivinhado pelo computador: "))

if a == numero_ale:
    print("parabens você acertou")
else:
    print("errou")



