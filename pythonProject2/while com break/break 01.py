from random import randint


b=0
escolha=''
pla=0
resultado=0
por=0
cont=0

while True:
    a = randint(0, 10)
    print(a)
    pla=int(input("""Brincando de par e impar com o computador 
digite um numero entre 0 a 10 contra o computador para ver quem ganha: """))
    if pla < 0 or pla > 10:

        pla=int(input("Valor fora dos parametros por favor digite novamente: "))

        if pla < 10 and pla > 0:
            escolha = str(input("Digite se você quer par ou impar: ")).upper()

            if escolha == 'IMPAR':
                b = 1
                resultado = pla + a
                por = resultado % 2
                if por != 0:
                    print("O jogador ganhou parabens!!!!")
                    cont += 1
                else:
                    print("quem ganhou foi o computador :(")
                    break
            elif escolha == 'PAR':
                b = 0
                if escolha == 'PAR':
                    b = 0
                    resultado = pla + a
                    por = resultado % 2
                    if por == 0:
                        print("O jogador ganhou parabens!!!!")
                        cont +=1
                    else:
                        print("quem ganhou foi o computador :(")
                        break
            else:
                print("Escolha de novo se vai ser par ou impar:",end='')
                escolha = str(input("")).upper()

                if escolha == 'PAR':
                    b = 0
                    resultado = pla + a
                    por = resultado % 2
                    if por == 0:
                        print("O jogador ganhou parabens!!!!")
                        cont +=1
                    else:
                        print("quem ganhou foi o computador :(")
                        break
                elif escolha == 'IMPAR':
                    b = 1
                    resultado = pla + a
                    por = resultado % 2
                    if por != 0:
                        print("O jogador ganhou parabens!!!!")
                        cont+=1
                    else:
                        print("quem ganhou foi o computador :(")
                        break

                else:
                    print("Você errou vezes demais, reinicie o algoritimo.")
                    break
        else:
            print("Você errou vezes demais, reinicie o algoritimo.")
            break
    else:
        escolha = str(input("Digite se você quer par ou impar: ")).upper()
        if escolha == 'PAR':
            b = 0
            if b == 0:
                resultado = pla + a
                por = resultado % 2
                if por == 0:
                    print("O jogador ganhou parabens!!!!")
                    cont += 1

                else:
                    print("quem ganhou foi o computador :(")
                    break
        elif escolha == 'IMPAR':
            b = 1
            if b == 1:
                resultado = pla + a
                por = resultado % 2
                if por != 0:
                    print("O jogador ganhou parabens!!!!")
                    cont += 1
                else:
                    print("quem ganhou foi o computador :(")
                    break

        else:
            print("Escolha se vai ser par ou impar de novo de novo:",end='')
            escolha = str(input("")).upper()
            if escolha == 'PAR':
                b = 0
                if b == 0:
                    resultado = pla + a
                    por = resultado % 2
                    if por == 0:
                        print("O jogador ganhou parabens!!!!")
                        cont += 1
                    else:
                        print("quem ganhou foi o computador :(")
                        break
            elif escolha == 'IMPAR':
                b = 1
                if b == 1:
                    resultado = pla + a
                    por = resultado % 2
                    if por != 0:
                        print("O jogador ganhou parabens!!!!")
                        cont += 1

                    else:
                        print("quem ganhou foi o computador :(")
                        break
            else:
                print("Você errou vezes demais, você tera que reiniciar o programa reinicie o algoritimo.")
                break


print(cont)
