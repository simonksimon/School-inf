vypis_typy=[]
vypis_typy=input("Napíš radu znakov. My ti vypíšeme, aký typ je každý: ")
cisla="0123456789"
abeceda="abcdefghijklmnopqrstuvwqyz"
cely=str(vypis_typy)
for i in range (len(cely)):
    while cely[i]!=",":
        if cely[i] in cisla:
            c=True
        if cely[i] in abeceda:
            l=True
    if c==True and l==False:
        print(vypis_typy[i]," Číslo")
    elif l==True and c==False:
        print(vypis_typy[i]," Reťazec")
    else:
        print(vypis_typy[i]," Iný typ")