a = 1
valor=0
calculo=0
b = 0

num= int(input("Digite um numero inteiro para fatorizar: "))
valor = num
c= num-1
p=num

while a <= num:
    calculo = valor * (num-1)
    num = num - 1
    valor = calculo
    a+=1
    if a == c:
        print(valor)
        print("Se quiser sair digite 0 / para continuar é 1")
        b = int(input("quer continuar ? "))
        if b == 0:
            a = num
        elif b == 1:
            num = int(input("Digite o numero que você quer faturar: "))
            a = 0
            valor = num
            calculo = 0
        else:
            print("valor errado digitado")
            a = 1
            valor = p
            calculo = 0
            num = p

print("projeto finalizado o valor faturado é {}".format(valor))