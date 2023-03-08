from PIL import Image

density = 'Ñ@#W$9876543210?!abc;:+=-,._ ' #https://play.ertdfgcvb.xyz/

fw=open("output.txt","w",encoding="UTF-8")

def mapping(a, b, c, d, x):                 #important vzorec
    return int((d*(x-a)+c*(b-x))/(b-a))     #dôležitá equation

obr = Image.open("128x128.jpg")
pixels=obr.load()


for y in range(obr.size[1]):
    for x in range(obr.size[0]):
        #print(pixels[x,y])
        avg=sum(pixels[x,y])/3
        pos=mapping(0,255,0,len(density)-1,avg)
        #print(density[pos])
        fw.write(density[pos])
    fw.write("\n")

print(mapping(0,255,0,38,10))
