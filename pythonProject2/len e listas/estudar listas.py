

tuplas= ('hamburguer','lanche','pudim','suco')
print(tuplas[1])#lanche
print(tuplas[1:3]) #lanche e pudim por que ignora o ultimo fator
print(tuplas[-1])#suco
print(tuplas[1:])#do lanche ao fim
print(tuplas[:2])#hamburguer e lanche
print(tuplas[-2:])#pudim e suco




lista= ['hamburguer', 'lanche']
lanche= lista.insert(0,'hamburguer')#inserir um item em outra posição
lanche= lista.append('hamburguer2')#inserir no final da lista e uma posição nova
lanche= lista.pop(3)#elimina o elemento e a posição
lanche= lista.pop()#elimina o elemento e a posição final
lanche= lista.remove(lista[1])#remove o item da posição
if 'hamburguer' in lista:
    lanche.remove('hamburguer') #remover da lista caso esteja
valores = list(range(4,11))

valores2=[8,2,5,4,3,0]
valores2.sort()#ordena na ordem certa
valores2.sort(reverse=True)#na ordem inversa
len(valores2)

a=[2,3,4,7]
b=a[]#liga uma lista a outra
b=a[:]#faz uma cópia de uma lista0
b[2]=8
print(f'Lista a: {a}')
print(f'Lista b:{b}')

dados=list()#cria uma lista vazia
dados.append('scooby')#adiciona valor na lista vazia
dados.append('25')
pessoas=list()
pessoas.append(dados[:])#adiciona informações de uma lista a outra vazia

dicionario= {'hamburguer','lanche'}