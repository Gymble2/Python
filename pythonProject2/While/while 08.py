a=''
num=0
v1=0
v2=0
maior=0
cont=0
x=0
menor=0


while a != 'S':
    num= int(input("Digite  o numero inteiro para efetuar as equações:"))
    a= str(input("Deseja sair? [S] ou [N]")).upper()
    v2=num
    maior=num
    v1=v1+v2
    cont+=1
    if x < maior:
        x = maior

    elif maior < x:
        menor = maior


media = v1/cont
print(f"a média é {media}, o maior é {x} e o menor é {menor}")

