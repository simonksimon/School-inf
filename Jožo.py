import random
vstup=[]
for i in range(10):
    vstup.append(random.randrange(0,21))
print(vstup)
p=0
n=0
for i in range(len(vstup)):
    if (vstup[i] % 2)==0:
        p+=1
    if (vstup[i] % 2)!=0:
        n+=1
if p>n:
    v=True
else:
    v=False
print(v)
