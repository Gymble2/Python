
contagem=0
soma=0
valor= 0
homem = ''
valor


for c in range(0, 4):
    print("Digite seu nome, idade e sexo em ordem abaixo: ")
    nome=str(input("Nome:")).strip()
    idade=int(input("Idade:"))
    sexo=str(input("Sexo:")).upper().strip()


    if idade == idade:
        soma = soma + idade

    if c==1 and sexo in 'HOMEM':
        valor= idade
        homem = nome

    if sexo in 'HOMEM' and idade > valor:
        valor =idade
        homem = nome

    if sexo in 'MULHER' and idade<20:
        contagem+=1

print('a idade média do grupo é {}, o homem mais velho é {} e tem apenas {} mulheres com menos de 18 anos no grupo'.format(soma/2, homem , contagem ))