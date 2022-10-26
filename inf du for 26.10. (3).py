vstup=str(input("Magicky zistím, či to čo napíšete bude obsahovať iba samohlásky, alebo nie. "))
a=len(vstup)
b="aAeEiIyYoOuU"
c=True
d=True
for i in range(a+1):
    if i<len(vstup):
        if vstup[i] not in b:
            c=False
        if c==False:
            d=False
print(d)