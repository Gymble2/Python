
valor_sacado=int(input("Qual valor será sacado??"))

total=valor_sacado

qntd=50
qnt=0



while True:
    if total > qntd:
        total-=qntd
        qnt+=1
    else:
        if qnt>0:
            print(f"vão ser {qnt} otas de {qntd}")
        if qntd == 50:
            qntd = 20
        elif qntd == 20:
            qntd = 10
        elif qntd == 10:
            qntd = 1
        qnt = 0
        if qntd == 0:
            break


19




