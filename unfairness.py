import random

c=0
k=0

for i in range(525):
    n=random.randrange(0,1100)
    m=random.randrange(0,1000)
    a = pow(n, m)
    s=str(a)
    b=s[0]
    if b=='1' or b=='2' or b=='3':
        c+=1
    else:
        k+=1

print("c=",c,"and k=",k)
