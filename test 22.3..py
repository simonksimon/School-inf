from PIL import Image,ImageOps
obr=Image.open("128x128.jpg")
obr1=Image.new("RGB",(128,128))
pixels=obr1.load()
pixels=obr.load()
pixel_out=obr.load()
pixel_in=obr.load()

#for x in range(obr.size[0]):
#    for y in range(obr.size[1]):
#        if x<64 and y>64:
#            pixel_in[x,128-y]=pixel_out[x,y]
#        if x>64 and y>64:
#             pixel_in[128-x,y]=pixel_out[x,y]
#        if x>64 and y<64:
#            pixel_in[x,128-y]=pixel_out[x,y]
#        if x<64 and y<64:
#            pixel_in[128-x,y]=pixel_out[x,y]

obrnew = obr.transpose(Image.ROTATE_90)

obr1 = ImageOps.invert(obrnew)

obr1.show()


