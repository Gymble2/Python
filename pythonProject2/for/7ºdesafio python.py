frase=str(input("Digite a frase: ")).strip().upper()
espace=frase.split()
noespace=''.join(espace)
inverso=''

for c in range(len(noespace) -1,-1,-1):
    inverso+=noespace[c]
print(noespace,inverso)

if noespace == inverso:
    print('é um polimendro!!!!')
else:
    print('não é um polimendro. ;-;')