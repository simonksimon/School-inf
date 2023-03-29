file1 = open("meteo_stanice.txt","r")

zozriadok=file1.readlines()
numberoflines=len(zozriadok)
print("Počet meraní:")
print(str(numberoflines))

maxteplota=0
zozteplot=[]
for i in range (numberoflines):
    currentriadok=zozriadok[i]
    print("Teploty:")
    currentteplota=currentriadok[21:26]
    print(currentteplota)
    currentteplota=currentteplota.replace(",",".")
    if currentteplota[0]=="+":
        currentteplota=currentteplota[1:5]
        floatedteplota=float(currentteplota)
        if floatedteplota>maxteplota:
            maxteplota=floatedteplota
            max=currentteplota
            kod=currentriadok[0:4]
    zozteplot.append(float(currentteplota))
print("Najvyššia nameraná teplota:")
print(max)
print("Kód stanice, kde bola nameraná najvyššia teplota:")
print(kod)

spolu=0
for i in range(len(zozteplot)):
    spolu+=zozteplot[i]
priemer=spolu/len(zozteplot)
print("Priemerná teplota všetkých staníc:")
print(priemer)
