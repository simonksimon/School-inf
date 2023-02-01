import random

hodnoty={}
p=10000

for i in range(p):
    c=random.randrange(1,1100)
    m=random.randrange(1,1000)
    vysledok=c**m
    cifra=int(str(vysledok)[0])
    hodnoty[cifra]=hodnoty.get(cifra,0)+1
print(hodnoty)

for i in hodnoty:
    print(i, hodnoty[i],(hodnoty[i]/p)*100)
