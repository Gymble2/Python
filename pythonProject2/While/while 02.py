from random import  randint

a= randint(0,10)
num = 15
print(a)

while num != a:
    num = int(input("Adivinhe o computador que o numero esta pensando entre 0 e 10: "))
    if num > 10 or num < 0:
        print("Digite um valor entre *1 e 10*")
print("Parbéns você acertou o número pensado é: {} ".format(a))
