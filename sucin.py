def sucin(zoznam):
    v=1
    print(zoznam)
    for i in range(len(zoznam)):
        v*=int(zoznam[i])
    return(v)

zoz=[]
i=0
vstup=""
while vstup!=",":
    i+=1
    vstup=(input("Zadaj mi prvok zoznamu. Ak chceš skončiť, napíš ','. "))
    if vstup!=",":
        zoz.append(vstup)
    if i==100:
        break
print(zoz)
vys=sucin(zoz)
print(vys)