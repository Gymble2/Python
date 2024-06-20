a=0
b=0
soma=0

while a!=999:
    print("--------------------PARA PARAR DIGITE 999--------------------")
    a=int(input("digite o valor a ser somado: "))
    soma = soma + a
    b+=1
    if a < 0:
        print("o valor digitado tem que ser positivo: ")
        a=0

print("A soma dos valores deu {} e foram digitados {}".format(soma-999, b-1))
