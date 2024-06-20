from random import randint

while True:
    comp=randint(1,3)
    #1 pedra 2 papel 3 tesoura
    print("""\n\033[1mJogue jokenpo contra o computador escolha um dos 3
[Pedra]
[Papel]
[Tesoura]""")
    escolha=str(input("")).upper().strip()

    if escolha == 'PEDRA':
        if comp == 1:
            print('Empatou')
        elif comp == 2:
            print('Você perdeu')
        elif comp == 3:
            print('Você ganhou')
        break
    elif escolha == 'PAPEL':
        if comp == 1:
            print('Parabéns você ganhou!!!')
        elif comp == 2:
            print('Empatou')
        elif comp == 3:
            print('Você perdeu')
        break
    elif escolha == 'TESOURA':
        if comp == 1:
            print('\033[1;31mGANHOU TCHU TCHU!!!')
        elif comp == 2:
            print('Você perdeu')
        elif comp == 3:
            print('EMPATOU')
        break
    else:
        print("Programa finalizando devido a erro de sintaxe: ")
        break