
def leiaint(valor):
    """
    :param valor: serve para compara para ver se o numero é inteiro
    :return: o valor digitado caso seja um numero inteiro
    """
    while True:
        try:   #para testar algum parametro
           n = int(input(valor))
        except (ValueError, TypeError): #para testar tipo de erros
            print('\033[31mERRO: por favor, digite um número inteiro valido\033[m')
            continue
        except KeyboardInterrupt: #para testar tipo de erros
            print('O usuário não digitou nenhum valor, [valor atribuido = 0]')
            return 0
        else:
            return n #para retornar um valor completo

def linha(num=40):
    """
    :param num: quantidade de linhas
    :return: retornar linha
    """
    return "-" * num #definir uma divisória



def txt(msg ,cor = 0):  #formatação de texto
    """
    :param msg: mensagem recebida
    :param cor: comparação para cor de erros
    """
    if cor == 1:
        print(linha())
        print(f'\033[31m{msg.center(42)}\033[m')
        print(linha())
    else:
        print(linha())
        print(msg.center(42))
        print(linha())


def menu(lista): #menu de opções
    """
    :param lista: recebe o menu de opções
    :return: opção escolhida
    """
    txt("SISTEMA PRINCIPAL")
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc  #para retornar um valor completo





