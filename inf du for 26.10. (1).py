vstup1=""
vstup2=""
vstup1=int(input("Číslo znaku (počíta sa od 0): "))
vstup2=str(input("Slovo, z ktorého vyberáme."))
if vstup1=="" or vstup2=="" or vstup1>len(vstup2)-1:
    print("Zlý index.")
else:
    print(vstup2[vstup1])