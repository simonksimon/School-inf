Priemer=int(input("Priemer?"))
Vyska=int(input("Výška?"))
Polomer=Priemer/2
#Sp=pí*r na druhú
Dno=3.14*(Polomer*Polomer)
#2*pí*r*v
Plast=2*3.14*Polomer*Vyska
ndDno=Dno*2
ndPlast=Plast*2
Spolu=(ndDno+ndPlast)/7.5
print("Potrebujeme ",Spolu," plechoviek.")
