# na zaciatku 2 body([a,b],[c,d]) a bez prikazov pixel po pixly vykreslit usecku
#a<c
#b<d
from PIL import Image#,ImageDraw
img=Image.new('RGB',(250,250),'white')
pixels=img.load()
a=input('Give point A as x,y:')
b=input('Give point B as x,y:')
a=a.split(',')
b=b.split(',')
a1=int(a[0])
a2=int(a[1])
b1=int(b[0])
b2=int(b[1])
#dr=ImageDraw.Draw(img)
#dr.point((a1,a2),fill=(0,0,0))
#bitmap[a1,a2] = 1
#pixels[a1,a2]=(0,0,0)
if a1<b1 or a1==b1:
    rozdielx=b1-a1
elif a1>b1:
    rozdielx=a1-b1
if a2<b2 or a2==b2:
    rozdiely=b2-a2
elif a2>b2:
    rozdiely=a2-b2
if rozdielx>rozdiely or rozdiely==rozdielx:
    pomer=rozdielx/rozdiely
    if a1<b1 and a2<b2:
        for i in range(rozdiely):
            pixels[a1+i,a2+i*pomer]=(0,0,0)
    if a1<b1 and a2>b2:
        for i in range(rozdiely):
            pixels[a1 + i, b2 + i * pomer]=(0,0,0)
    if a1>b1 and a2<b2:
        for i in range(rozdiely):
            pixels[b1+i,a2+i*pomer]=(0,0,0)
    if a1>b1 and a2>b2:
        for i in range(rozdiely):
            pixels[b1 + i, b2 + i * pomer]=(0,0,0)
elif rozdielx<rozdiely:
    pomer=rozdiely/rozdielx
    if a1<b1 and a2<b2:
        for i in range(rozdielx):
            pixels[a1+i,a2+i*pomer]=(0,0,0)
    if a1<b1 and a2>b2:
        for i in range(rozdielx):
            pixels[a1 + i, b2 + i * pomer]=(0,0,0)
    if a1>b1 and a2<b2:
        for i in range(rozdielx):
            pixels[b1+i,a2+i*pomer]=(0,0,0)
    if a1>b1 and a2>b2:
        for i in range(rozdielx):
            pixels[b1 + i, b2 + i * pomer]=(0,0,0)
img.show()