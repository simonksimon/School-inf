vypis_typy=[input("Napíš radu znakov. My ti vypíšeme, aký typ je každý: ")]
cisla="0123456789"
abeceda="abcdefghijklmnopqrstuvwqyz"

def isfloat(numeral):
    try:
        float(numeral)
        return True
    except ValueError:
        return False

def find_letter(letter, lst):
    return any(letter in word for word in lst)

for i in range(len(vypis_typy)):
    c=isfloat(vypis_typy[i])
    l=find_letter(cisla, vypis_typy[i])
    if c==True and l==False:
        print(vypis_typy[i]," Číslo\n")
    elif l==True and c==False:
        print(vypis_typy[i]," Reťazec\n")
    else:
        print(vypis_typy[i]," Iný typ\n")