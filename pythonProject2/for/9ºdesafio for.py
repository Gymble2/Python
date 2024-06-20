
valor = 0
valor2 = 0

for c in range(0,5):
    peso=float(input("digite seu peso em kg: "))
    if valor < peso:
        valor = peso
    elif valor2 < peso:
        valor2 = peso
    elif valor2 < valor:
        valor2 = peso

print(valor,valor2)