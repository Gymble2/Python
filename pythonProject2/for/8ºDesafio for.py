a=0

for c in range(0,7):
    ano=int(input("digite o seu ano de nascimento: "))
    conta=2023-ano
    if conta<18:
        a+=1

print("os nenem são apenas {}.".format(a))