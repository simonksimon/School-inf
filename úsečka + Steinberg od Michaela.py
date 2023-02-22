from PIL import Image

img=Image.open('cat.png')
pixels=img.load()

def find_closest_palette_colour(oldP):
    return (round(oldP[0]/255)*255,round(oldP[1]/255)*255,round(oldP[2]/255)*255)

def twotuplesminus(t1,t2):
    return (t1[0]-t2[0],t1[1]-t2[1],t1[2]-t2[2])

def twotuplesplus(t1,t2,cons):
    return (int(t1[0]+t2[0]*cons),int(t1[1]+t2[1]*cons),int(t1[2]+t2[2]*cons))

for y in range(img.size[1]-1):
    for x in range(1,img.size[0]-1):
        oldP=pixels[x,y]
        Npixel=find_closest_palette_colour(oldP)
        pixels[x,y]=Npixel
        quant_error=twotuplesminus(oldP,Npixel)
        pixels[x + 1,y    ] = twotuplesplus(pixels[x + 1,y    ], quant_error , 7 / 16)
        pixels[x - 1,y + 1] = twotuplesplus(pixels[x - 1,y + 1], quant_error , 3 / 16)
        pixels[x    ,y + 1] = twotuplesplus(pixels[x    ,y + 1], quant_error , 5 / 16)
        pixels[x + 1,y + 1] = twotuplesplus(pixels[x + 1,y + 1], quant_error , 1 / 16)
pixels=img.show()

----------------------------------------------------------------------------------------------------

# na zaciatku 2 body([a,b],[c,d]) a bez prikazov pixel po pixly vykreslit usecku
#a<c
#b<d


from PIL import Image
img=Image.new('RGB',(250,250),'white')
pixels=img.load()
a=input('Give point A as x,y:')
b=input('Give point B as x,y:')
a=a.split(',')
b=b.split(',')
a=list(map(lambda x: int(x), a))
b=list(map(lambda x: int(x), b))

k=(b[1]-a[1])/(b[0]-a[0])
q=a[1]-k*a[0]

for x in range(a[0],b[0]):
    y=int(k*x+q)
    pixels[x,y]=(255,0,0)
img.show()
