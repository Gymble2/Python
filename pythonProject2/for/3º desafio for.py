soma=0

for c in range(1,501):
    d=c%2
    if d != 0:
        soma = soma+c
print('a soma de todos os impares é{}'.format(soma))