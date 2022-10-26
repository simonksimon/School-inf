#vytvotrte/napíšte funkciu 'vypis', ktorá má jeden vstupný parameter(reťazec), funkcia vypíše (print) pre každý znak tohto reťazca 4 údaje: poradové číslo,je Ascii/ordinálnu hodnotu, samotný znak, znak ktorý nasleduje za ním.
vstup=str(input("Váš vstup: "))
a=len(vstup)
b=1
for i in range(a+1):
    if i<len(vstup):
        f=""
        c=(vstup[i])
        d=ord(c)
        f=(f"{b} {d} {c}")
        if i<len(vstup)-1:
            e=vstup[i+1]
            f=(f"{f} {e}")
        print(f)
        b+=1
