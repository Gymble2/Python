def voto(ano):
    hoje=2023
    media=hoje-ano
    if media >= 18 and media <= 65 :
        print("é Obrigatório")
    if media >= 16 and media < 18:
        print("é opcional")
    if media < 16 and media > 0 :
        print("é proibido")
    if media > 65:
        print("é opicional")


idade=int(input("Digite a data do seu nascimento: "))

voto(idade)