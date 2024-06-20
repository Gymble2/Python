from random import randint

def aleatorio(espaco):
    lista = list()

    soma = 0
    for c in range (0 , espaco):

        lista.append(randint(0,10))

        a = lista [c] %2

        if a == 0 :

            soma = soma + lista[c]
    print(lista,soma)

espaco = 0

espaco = int(input("digite o valor dos parametros: "))

aleatorio(espaco)