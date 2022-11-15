vypis_typy=[]
inp=input("Napíš radu znakov. My ti vypíšeme, aký typ je každý: ")
vypis_typy=inp.split()
cisla="0123456789.,"
abeceda="abcdefghijklmnopqrstuvwqyz,"
for i in range (len(vypis_typy)):
    clen=vypis_typy[i]
    c=False
    l=False
    for y in range (1,len(clen)-1):
        if i<len(clen):
            if clen[y] in cisla:
                c=True
            if clen[y] in abeceda:
                l=True
    if (clen[0]=="'" and clen[-2]=="'") or (clen[0]=="'" and clen[-1]=="'"):
        print(clen, " - Reťazec.")
    elif c == True and l == False:
        print(clen," - Číslo.")
    elif l == True and c == False:
        print(clen," - Reťazec.")
    else:
        print(clen, " - Iný typ.")