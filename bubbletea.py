import random
zoz=[]
for i in range(10):
    zoz.append(random.randrange(0,21))
print(zoz)
c=0
d=0
while c!=len(zoz)-1:
    c=0
    d+=1
    for i in range(len(zoz)-1):
        if int(zoz[i+1])>int(zoz[i]):
            zoz[i],zoz[i+1]=zoz[i+1],zoz[i]
        else:
            c+=1
        if d==10000:
            break
print(zoz)


