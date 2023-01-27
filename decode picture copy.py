from PIL import Image
sprava = "Ahoj svet#"

obr = Image.open("picturefordecoding.jpg")
pixels=obr.load()

dlzka = 8

def priprav(sprava:str)->list:
    res=[]
    for pismeno in sprava:
        cislo=bin(ord(pismeno))[2::]
        pn = dlzka - len(cislo)
        cislo = pn * "0" + cislo
        # print(cislo)
        for j in cislo:
            res.append(int(j))
        return res

#print(priprav(sprava))

def dekodecka(sprava):
    dvojkovasustava=priprav(sprava)
    for i in range(len(dvojkovasustava)):
        #toto tam ideme dávať  dvojkova sustava[i]
        sirka=obr.size[0]
        vyska=obr.size[1]
        x=i%(sirka)
        y=i//(sirka)
        pixelblue=pixels[x,y][2]
        #print(pixels)
        newblue=int(bin(pixelblue)[2:-1:] + str(dvojkovasustava[i]),2)
        newcolor=(pixels[x,y][0],pixels[x,y][1],newblue)
        print(pixels[x,y],newcolor)
        pixels[x,y]=newcolor
        obr.save("picturefordecrypting.jpg")

dekodecka(sprava)

obr.show()