import shutil
file1 = open("hada.txt","r")

zozriadok=file1.readlines()
numberoflines=len(zozriadok)
print("Počet hier:")
print(str(numberoflines))


najriadok=0
for i in range(numberoflines):
    if len(zozriadok[i])>najriadok:
        najriadok=len(zozriadok[i])
print("Dĺžka najdlhšej hry:")
print(najriadok)

with open('hada.txt','r') as firstfile, open('hadacopy.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)


