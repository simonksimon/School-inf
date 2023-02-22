from PIL import Image
sprava = "Ahoj svet#"

obr=Image.open("robotpicture.jpg")
pixels=obr.load()

dlzka = 8

def priprav(sprava:str) ->list:
    res=[]
    for pismenko in sprava:
        cislo = (bin(ord(pismenko)))
        cislo = str(cislo[2::])
        #print(cislo)
        cislo = (dlzka-len(cislo))*"0" + cislo

        for j in cislo:
            res.append(int(j))
    return (res)

#print(priprav(sprava))

def dekodecka(sprava):
    dvojkovasustava = priprav(sprava)
    for i in range(len(dvojkovasustava)):
        w=obr.size[0]
        #vyska=obr.size[1]
        x=i%w
        y=i//w
        pixelblue=pixels[x,y][2]
        #print(pixels)
        newblue=int(bin(pixelblue)[2:-1:] + str(dvojkovasustava[i]),2)
        newcolor=(pixels[x,y][0],pixels[x,y][1],newblue)
        print(pixels[x,y],newcolor)
        pixels[x,y]=newcolor

dekodecka(sprava)

#_________________________________________________________________________

e = ord('A')
e = bin(e)
thecomplicated8thing=""
reťaz=""
for y in range(obr.size[1]):
    for x in range(obr.size[0]):
        if "#" in reťaz:
            themessagefromgod=reťaz
            break
        poslednablue=str(bin(pixels[x,y][2]))[-1]
        thecomplicated8thing+=poslednablue
        __=(bin(ord(" "))[2::])
        sotm=(bin(ord("#"))[2::])
        if len(thecomplicated8thing) == 8 or thecomplicated8thing[2::] == __ or thecomplicated8thing[2::] == sotm:
            reťaz+=chr(int((thecomplicated8thing),2))
            thecomplicated8thing=""
    if "#" in reťaz:
        break

for i in range (len(themessagefromgod)-1):
    print(str(themessagefromgod)[i])