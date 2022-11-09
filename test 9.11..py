#samohlasku o 2, spoluhlasku o 3
vstup = str(input("What would you like to encode?"))
abeceda="abcdefghijklmnopqrstuvwxyz"
samohlasky="aeiyou"
spoluhlasky="bcdfghjklmnpqrstvwxz"

def encode(input):
    vysledok=""
    a=len(vstup)
    for i in range(a+1):
        if i<len(vstup):
            letter=abeceda.find(input[i])
            if letter==24 or letter==23:
                vysledok=(f"{vysledok}a")
            elif letter==25:
                vysledok=(f"{vysledok}c")
            elif vstup[i] in samohlasky:
                vysledok=(f"{vysledok}{abeceda[letter+2]}")
            elif vstup[i] in spoluhlasky:
                vysledok=(f"{vysledok}{abeceda[letter+3]}")
    return(vysledok)


vys=encode(vstup)
print(vys)


