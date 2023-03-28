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

with open('hada.txt','r') as f1, open("hada_compressed.txt","w") as f2:
    old = ""
    count=0
    #while True:
    for line in f1:
        for i in range(len(line)):
        #    for ch in f1:
            ch = line[i]
            if old=="":
                old=ch
            if ch==old:
                count+=1
            elif ch!=old:
                f2.write(old)
                if old != "\n":
                    f2.write(str(count))
                count = 1
            old=ch
            if len(line)==1:
                count = False
    if count!=False:
        f2.write(old)
        f2.write(str(count))