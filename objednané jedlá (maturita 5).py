import shutil
file1 = open("objednane_jedla.txt","r")

zozriadok=file1.readlines()
numberoflines=len(zozriadok)
print("Počet objednávok:")
print(str(numberoflines))

#pocetjedal=0
#currentletter=""
#abeceda=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#knownletters=[]
#for i in range (numberoflines):
    #currentline=file1.readline()
    #for y in range (len(currentline)):
        #if currentline[y] in abeceda:
            #if globals()["0" + str(abeceda[y])] not in locals():
                #pocetjedal += 1
                #globals()["0" + str(abeceda[y])]=0
                #globals()["0" + str(pocetjedal)]=abeceda[y]
                #knownletters.append(abeceda[y])
            #globals()["0" + str(abeceda[y])]+=1
#
#for i in range(pocetjedal):
    #print("\n")
    #print (globals()["0" + str(i+1)])
    #lettertowrite=(globals()["0" + str(i+1)])
    #print (globals()["0" + str(lettertowrite)])
    #print("\n")

z,c,m,o=0,0,0,0
for i in range (len(zozriadok)):
        if "z" in zozriadok[i]:
            z += 1
        if "c" in zozriadok[i]:
            c += 1
        if "m" in zozriadok[i]:
            m += 1
        if "o" in zozriadok[i]:
            o += 1

print("z:",z)
print("c:",c)
print("m:",m)
print("o:",o)

if z < 20:
    print("Jedlo z si vybralo menej ako 20 študentov.")
else:
    print("Dostatok študentov si objednalo Jedlo z.")
if c < 20:
    print("Jedlo c si vybralo menej ako 20 študentov.")
else:
    print("Dostatok študentov si objednalo Jedlo c.")
if m < 20:
    print("Jedlo m si vybralo menej ako 20 študentov.")
else:
    print("Dostatok študentov si objednalo Jedlo m.")
if o < 20:
    print("Jedlo o si vybralo menej ako 20 študentov.")
else:
    print("Dostatok študentov si objednalo Jedlo o.")



