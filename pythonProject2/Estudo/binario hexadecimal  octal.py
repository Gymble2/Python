
while True:
    n = int(input("digite um numero:"))
    print("[1] binário")
    print("[2] octal")
    print("[3] hexadecimal")
    print("[x] sair")

    pergunta_num=str(input("digite qual o modo que você deseja converter: "))

    if pergunta_num == 'x' or pergunta_num == 'X':
        break
    elif pergunta_num == '1' or pergunta_num == '2' or pergunta_num == '3':
        if pergunta_num == '1':
            print('o valor em binário é {}'.format(bin(n)))
        elif pergunta_num == '2':
            print('o valor em octal é {}'.format(oct(n)))
        elif pergunta_num == '3':
            print('o valor em hexadecimal é {}'.format(hex(n)))

