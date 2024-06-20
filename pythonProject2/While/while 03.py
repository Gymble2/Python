
numA=int(input("Digite o 1º valor: "))
numB=int(input("Digite o 2º valor: "))
a=0

while a != 5 :
    print("""Menu
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
        """)

    a = int(input('Digite a opção desejada: '))

    if a == 1:
            print("A soma dos números é {}".format(numA + numB))

    elif a == 2:
            print("A multiplicação dos numeros é {}".format(numA * numB))
    elif a == 3:
        if numB > numA:
                print("O maior valor é {}".format(numB))

        elif numA > numB:
                print("O maior valor é {}".format(numA))


    elif a == 4:
            numA = int(input("Digite um novo primeiro valor: "))
            numb = int(input("Digite um novo primeiro valor: "))
print("Finalizado")





