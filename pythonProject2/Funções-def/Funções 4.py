def maior (nume):
    qnt = len(nume)

    if qnt == 0:
        print("A lista está vazia.")
        return

    conteudo = nume[0]

    for c in range(1, qnt):
        if nume[c] > conteudo:
            conteudo = nume[c]

    print(f'Os valores digitados foram {nume}')
    print(f'O maior valor digitado foi {conteudo}')




lista = list()
case ='a'


while case != 'N' :
    lista.append(int(input("Digite os valores a serem atribuidos:")))
    case = str(input("Desesja continuar? [S] [N]")).upper()

maior(lista)
