from random import choice

aluno1=str(input('digite o 1º nome:'))
aluno2=str(input('digite o 2º nome:'))
aluno3=str(input('digite o 3º nome:'))
aluno4=str(input('digite o 4º nome:'))

lista= [aluno1,aluno2,aluno3,aluno4]
escolhido= choice(lista)
escolhido2= choice(lista)
escolhido3= choice(lista)
print('o aluno escolhido foi: {} {} {}'.format(escolhido,escolhido2,escolhido3))

