Cena=int(input("Cena?"))
kusy=int(input("Počet kusov?"))
vyskaDPH=int(input("Výška DPH?"))
základnáC=Cena*kusy
DPH=základnáC*(vyskaDPH/100)
zdrazenaC=základnáC+DPH
print("Základná cena: ",základnáC)
print("S DPH: ",zdrazenaC)
