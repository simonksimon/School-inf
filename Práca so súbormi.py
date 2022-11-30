fr = open("data/udaje.txt","r",encoding="utf-8")
#mám súbor a ako ho prechádzať

#1. spôsob:
##for riadok in fr:
##    print(riadok.strip())

#2. spôsob - vytvorím megastring:
##ms = fr.read()
##print(ms)

#3. spôsob - Keď riadky potrebujem spracovať inak:
##prvy_riadok = fr.readline() #čítacia hlava - prečíta prvý a čaká na začiatku druhého
##print(prvy_riadok)

##druhy_riadok = fr.readline()
##print(druhy_riadok)

##for riadok in fr:
##    print(riadok)

#4. spôsob:
##zoz_riadok = fr.readlines()
##print(zoz_riadok)

md={}
ms=fr.read()
konriad=0
for znak in ms:
    if znak_isupper() or znak.islower():
        md[znak]=md.get(znal,0) + 1
    if znak == "\n":
        konriad += 1
print(md)
print(konriad)
