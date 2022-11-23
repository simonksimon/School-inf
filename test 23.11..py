import random
zoz=[]
abeceda="abcdefghijklmnopqrstuvwxyz"
for i in range(10):
    string=""
    b=0
    a=random.randrange(0,21)
    while b!=a:
        b+=1
        c=random.randrange(0,len(abeceda)-1)
        string+=abeceda[c]
        if b==100:
            break
    zoz.append(string)
print(zoz)

sos=[]
for i in range (len(zoz)):
    sos.append(len(zoz[i]))
print(sos)
