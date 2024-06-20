frase:str = (input("Digite a 1º frase "))
frase2:str = (input("Digite a 2º frase "))

valor = int(frase.count('',0))
valor2 = int(frase.count('',0))

if valor >= valor2:
    print('o primeiro valor é maior e tem {}'.format(valor))
else:
    print('o segundo valor é maior e tem {}'.format(valor2))


palavra =str(input("Digite a palavra a ser procurada na 1 frase: "))
palavra2 =str(input("Digite a letra a ser procurada na 1 frase: "))

a=frase.split(' ')
b=frase.count(palavra2)

print(a.count(palavra))
print(b)





