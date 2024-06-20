
print("obs: Letras maiusculas para o começo de cada nome\n\n ")

nome=str(input("""Por favor digite o seu nome completo:"""))
palavra=int(input("""Por favor digite a palavra escolhida:"""))
nome=nome

print(nome.upper())
print(nome.lower())

dividir=nome.split()
a=dividir[palavra]
a=a.strip()
print('a palavra escolhida foi {}'.format(dividir[palavra]))
print('o total de letras na {}º palavra é {}'.format(palavra,a.count('')-1))

spc:int =nome.count(' ')
name:int =nome.count('')
total= name-spc
print('A quantidade de espaços que tem é {}'.format(spc))
print('o total com espaço é {}'.format(name))
print('A quantidade total de letras sem espaço é {}'.format(total))


