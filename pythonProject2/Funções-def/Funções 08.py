def notas(notaz):
    quantidade = []

    for _ in range(notaz):
        quantidade.append(int(input("Valor da nota: ")))

    maior = max(quantidade)
    menor = min(quantidade)
    total = sum(quantidade)
    notas = len(quantidade)
    media = total / notas

    return maior, menor, total, notas, media


quantidade_notas = int(input("Digite quantas notas serão adicionadas: "))
maior, menor, total, notas, media = notas(quantidade_notas)

print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Total das notas: {total}")
print(f"Número de notas: {notas}")
print(f"Média das notas: {media}")