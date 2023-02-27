from PIL import Image

img=Image.open('robotpicture.jpg')
pixels=img.load()

def mydef(x1y,x2y,divides):
    return (int(x1y[0]+x2y[0]*divides),int(x1y[1]+x2y[1]*divides),int(x1y[2]+x2y[2]*divides))

for y in range(img.size[1]-1):
    for x in range(1,img.size[0]-1):
        opixel=pixels[x,y]
        pnew=(round(opixel[0]/255)*255,round(opixel[1]/255)*255,round(opixel[2]/255)*255)
        pixels[x,y]=pnew
        quantumania=(opixel[0]-pnew[0],opixel[1]-pnew[1],opixel[2]-pnew[2])
        pixels[x+1,y  ]=mydef(pixels[x+1,y  ], quantumania, 7/16)
        pixels[x-1,y+1]=mydef(pixels[x-1,y+1], quantumania, 3/16)
        pixels[x  ,y+1]=mydef(pixels[x  ,y+1], quantumania, 5/16)
        pixels[x+1,y+1]=mydef(pixels[x+1,y+1], quantumania, 1/16)

pixels=img.show()