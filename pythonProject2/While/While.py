'''for c in range(1,10):
    print(c)
print('fim')'''

'''for c in range (1,3):
    n= int(input('Digite o valor; '))
print('fim')

r='S'

while r== 'S':
    n= int(input('Digite um valor: '))
    r= str(input('Quer continuar [S/N] ')).upper()
print('fim')'''

n=1
par = impar = 0

while n !=0:
    n = int(input('Digite um valor: '))
    if n%2 == 0:
        par +=1
    else:
        impar +=1
print('Acabou')
print('Você digitou {} numeros pares e {} numeros impares.'.format(par-1,impar))

