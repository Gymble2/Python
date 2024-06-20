
n=int(input("digite"))

t1=0
t2=1
cont=3
print(t1,end=' ')
print(t2,end=' ')

while cont <= n:
    t3=t1+t2
    t1=t2
    t2=t3
    print(t3,end=' ')
    cont+=1