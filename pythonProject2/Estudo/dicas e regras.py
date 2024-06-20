#o valor da casa/ o salário e quantos anos
#valor da prestação / não pode ser <30% do salári

valor_casa = float(input("digite o valor da casa: "))
salário = float(input("digite o seu salário: "))
quantos_anos = int(input("digite em quantos anos você vai pagar:"))*12

mensalidade = valor_casa/quantos_anos
por = salário*0.030
resto = mensalidade-por


if mensalidade > por:
    print("impossivel realizar a compra falta {:.2f}R$".format(resto))
else:
    print("compra aprovada a mensalidade ficará: {:.2f}R$".format(mensalidade))