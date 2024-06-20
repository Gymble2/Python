a = 1
valor=0
valora=0
calculo=0

num= int(input("Digite um numero inteiro para fatorizar: "))
valor = num

while a <= num:
    calculo = valor * (num-1)
    num = num - 1
    valor = calculo
    a+=1
print(valor)