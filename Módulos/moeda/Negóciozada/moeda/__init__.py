def aumentar(num,valor, formato=False):
    """
    :param num: Recebe o valor
    :param valor: Recebe o valor de desconto
    :param formato: Vai indicar caso tenha que executar a formatação
    :return: retorna o valor e se vai ser efetuado a formatação com o valor do formato
    """
    r = num + ((num * valor)/100)
    return r if not formato else moeda(r)


def diminuir(num,valor, formato=False):
    """
    :param num: Recebe o valor
    :param valor: Recebe o valor de desconto
    :param formato: Vai indicar caso tenha que executar a formatação
    :return: retorna o valor e se vai ser efetuado a formatação com o valor do formato
    """
    r = num - ((num * valor)/100)
    return r if not formato else moeda(r)


def dobro(num, formato= False):
    """
    :param num: Recebe o valor
    :param formato: Vai indicar caso tenha que executar a formatação
    :return: retorna o valor e se vai ser efetuado a formatação com o valor do formato
    """
    num *= 2
    return num if not formato else moeda(num)


def metade(num, formato=False):
    """
    :param num: Recebe o valor
    :param formato: Vai indicar caso tenha que executar a formatação
    :return: retorna o valor e se vai ser efetuado a formatação com o valor do formato
    """
    r = num/2
    return r if not formato else moeda(r)


def moeda(num=0, moeda="R$"):
    """
    :param num: valor recebido
    :param moeda: formatação de texto
    :return: A formatação completa
    """
    return f"{moeda} {num:>.2f}".replace(".",",")


def resumo(preço=0, taxa=10, taxar=5):
    """
    :param preço: valor inicial
    :param taxa: Valor a aumentar
    :param taxar: Valor a diminuir
    :return: 0
    """
    print("-"*30)
    print("Resumo total".center(30))
    print("-" * 30)
    print(f"o valor do dobro de {moeda(preço)} é {dobro(preço, True)}")
    print(f"o valor de aumento de {taxa}% do valor {moeda(preço)} é {aumentar(preço, taxa, True)}")
    print(f"o valor da diminuição de {taxar} % é {moeda(preço)} é {diminuir(preço, taxar, True)}")
    print(f"o valor de {moeda(preço)} é {metade(preço, True)}")