primeiro=int(input('Digite o primeiro termo da PA: '))
razao=int(input("Digite agora a razão da PA: "))
lista=[0,0,0,0,0,0,0,0,0,0]


for c in range(0,10):
    lista[c]= primeiro
    primeiro = primeiro+razao
for d in range(0,10):
    print(lista[d])
