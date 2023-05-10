
#---------------------------------------------------------------------------------------------------

# na zaciatku 2 body([a,b],[c,d]) a bez prikazov pixel po pixly vykreslit usecku
#a<c
#b<d


from PIL import Image, ImageDraw
img=Image.new('RGB',(250,250),'white')
draw = ImageDraw.Draw(img)
pixels=img.load()
a=input('Give point A as x,y:')
b=input('Give point B as x,y:')

a1=""
a2=""
comma=False
for i in range (len(a)):
    if comma==True:
        if i<len(a)+1:
            a2=(a2+a[i])
    if a[i]!="," and comma==False:
        a1=(a1+a[i])
    else:
        comma=True
b1=""
b2=""
comma=False
for i in range(len(b)):
    if comma == True:
        if i < len(b) + 1:
            b2 = (b2 + b[i])
    if b[i] != "," and comma==False:
        b1 = (b1 + b[i])
    else:
        comma = True
a1=int(a1)
a2=int(a2)
b1=int(b1)
b2=int(b2)

draw.line((a1, a2, b1, b2), fill=(0, 0, 0), width=10)
img.show()