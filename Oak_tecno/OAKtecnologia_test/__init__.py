from time import sleep
from OAKtecnologia_test.Arquivo import *

arq = 'produtos_lista'

#Para mostrar a lista em ordem crescente é necessario utilizar a segunda opção para mostrar todo o conteudo
#O cadastro mostra apenas a lista ja existente mas o item adicionado no final na lista
#caso o arquivo esteja vazio ele ira mostrar um aviso na primeira vez que for executado

if not existeArquivo(arq):
    criarArquivo(arq)

while True:

    resposta = menu(['Cadastrar produtos', 'Lista completa de produtos', 'Sair do sistema'])

    if resposta == 1:
        txt("NOVO CADASTRO DE PRODUTO")
        nome_Produto = str(input("Produto: "))
        cod_Produto = leiaint("Valor do produto: ")
        cadastrar(arq, nome_Produto, cod_Produto)

    elif resposta == 2:
        reescreveArquivo(arq, organizaCrescente(arq))
        lerArquivo(arq)

    elif resposta == 3:
        txt('Saindo do sistema', 1)
        break

    else:
        txt("Erro", 1)

    sleep(2)