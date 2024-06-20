soma=0

for c in range(0,6):
    valor = int(input("digite os valores inteiros:"))
    por = valor%2
    if por == 0:
        soma = soma + valor
print(soma)