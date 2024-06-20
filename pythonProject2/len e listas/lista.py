

nome=list()
peso=list()
pesado=list()
leve=list()
a=0
cont=0
c=0


while True:
    nome.append(str(input("Qual seu nome:")))

    peso.append(float(input("Digite seu peso:")))

    a= str(input("Deseja continuar ?? [S] [N]")).lower()


    if cont >= 1 and peso[cont] > peso[cont - 1]:
        pesado.append(nome[cont])

    elif cont == 1 and peso[0] > peso[1]:
        pesado.append(nome[0])
        leve.remove(leve[0])
        leve.append(nome[1])
    else:
        leve.append(nome[cont])

    cont += 1

    if a == "n" :
        break



print(f"as pessoas pesadas são{pesado}")
print(f"as pessoas leves são{leve}")
print(f"foram pegos os dados de {cont} pessoas")