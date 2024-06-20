def fatorial(fat):
    fatorizacao = 1

    for i in range(1, fat + 1):
        fatorizacao *= i

    return fatorizacao



fator = int(input("Digite o valor a ser fatorado: "))
print(f"{fator} x {fator-1} ", end="")
fato = fator - 2

for c in range (1, fator - 1):
    print(f"x {fato} ", end="")
    fato-=1



resultado = fatorial(fator)

print(f"""= {resultado} """)

print(f"""
O fatorial de {fator} é {resultado}""")
