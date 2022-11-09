import random
zoz=[]
for i in range(10):
    zoz.append(random.randrange(0,21))
print(zoz)

maxi=zoz[0]
a=len(zoz)
#for i in range(a+1):
for i in range(1,a+1):
    if i<len(zoz):
#       if i==0:
#            i=1
        if zoz[i]>maxi:
            maxi=zoz[i]
print(maxi)

parny=0
neparny=0
b=len(zoz)
for i in range(b+1):
    if i<len(zoz):
        if (zoz[i] % 2)==0:
            parny+=1
        else:
            neparny+=1
print("Párnych čísel je: ",parny)
print("Nepárnych čísel je: ",neparny)

parpar=0
c=len(zoz)
for i in range(c+1):
    if i<len(zoz):
        if (zoz[i] % 2)==0 and (i % 2)==0:
            parpar+=1
print("Párnych čísel na párnych pozíciach: ",parpar)


zoz1=[]
for i in range(10):
    zoz1.append(random.randrange(0,21))
print(zoz1)

zoz2=[]
for i in range(10):
    zoz2.append(random.randrange(0,21))
print(zoz2)

def merge(zoz3,zoz4):
    zoz5=f"{zoz3}{zoz4}"
    maxi1=zoz5[0]
    a=len(zoz5)
    for i in range(1,a+1):
        if i<len(zoz5):
            if zoz5[i]>maxi1:
                maxi1=zoz5[i]
    return(maxi1)

maxi2=merge(zoz1,zoz2)
print(maxi2)
