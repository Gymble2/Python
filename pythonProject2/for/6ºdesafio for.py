num= int(input("Digite o numero para ver se ele é primo:"))
total=0

for c in range(1, num+1):
    if num % c ==0:
        print('\033[34m',end=' ')
        total+=1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end='')
print('\n\033[mO total de vezes que o numero foi divisivel por 0 foi {} vezes.'.format(total))

if total == 2:
    print("O numero é primo")
else:
    print("O numero não é primo")