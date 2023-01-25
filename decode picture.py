from PIL import Image
sprava = "Ahoj svet#"

obr = Image.open("picturefordecoding")
pixels=obr.load()

def priprav(sprava:str)->list:
    for pismenko in sprava:
        cislo=bin(ord(pismenko)) [2::]
        if len(cislo)<7:
            a=str(0)
            cislo=str(cislo)
            cislo=(a+str(cislo))
        print(cislo)


print(priprav(sprava))

def dekodecka(sprava):
    dvojkovasustava=priprav(sprava)
    for i in range(len(dvojkovasustava)):
        #toto tam ideme dávať  dvojkova sustava[i]
        sirka=obr.size[0]
        vyska=obr.size[1]
        x=i%(sirka)
        y=i//(sirka)
        pixelblue=pixels[x,y][2]
        print(pixels)
        newblue=int(bin(pixelblue)[2:-1:] + str(dvojkovasustava[i]),2)
        newcolor=(pixels[x,y][0],pixels[x,y][1],newblue)
        print(pixels[x,y],newcolor)
        pixels[x,y]=newcolor
        obr.save("a picture for decrypting.jpg")

dekodecka(sprava)
