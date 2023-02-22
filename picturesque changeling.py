from PIL import Image, ImageOps
obr=Image.open("imagined chameleon.jpg")
obr1=Image.new("RGB",(obr.size[0]*2,obr.size[1]*2),"white")

pixel_out=obr.load()
pixel_in=obr1.load

for x in range(obr.size[0]):
    for y in range(obr.size[1]):
        pixel_in[2+x,2*y]=pixel_out[x,y]
        pixel_in[2*x+1,2*y+1]=pixel_out[x,y]
        pixel_in[2*x,2*y+1]=pixel_out[x,y]
        pixel_in[2*x+1,2*y]=pixel_out[x,y]

obr1.show()


obr=Image.open("imagined chameleon.jpg")
obr1=ImageOps.grayscale(obr)
pixels=obr1.load()
fw=open("vysledok.txt","w",encoding="UTF-8")
fw.write(str(obr.size[0])+" "+str(obr.size[1])+"\n")
for y in range(obr1.size[1]):
    for x in range(obr1.size[0]):
        print(hex(pixels[x,y])[2::])
