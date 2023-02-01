import random

a="1"

for i in range(10):
    globals()["0" + str(a)] = []
    for y in range(5):
        n=str(random.randrange(0,9))
        globals()["0" + str(a)].append(n)
    print(globals()["0" + str(a)])
    b=int(a)
    b+=1
    a=str(b)

a=int(a)
zoz=[]
for i in range(a):
    zoz.append(globals()["0" + str(i+1)])
zoz.sort
print("")
print(zoz)
