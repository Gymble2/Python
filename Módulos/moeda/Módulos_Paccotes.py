from Negóciozada import moeda
from Negóciozada import dado


p = dado.leiaint("Digite um valor: ")
juros = dado.leiaint("Digite a porcentagem de aumento: ")
juros2 = dado.leiaint("Digite a porcentagem de diminuição: ")

moeda.resumo(p, juros, juros2)


