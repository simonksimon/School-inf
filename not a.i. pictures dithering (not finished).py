from PIL import Image
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
a=0
img2 = Image.open('th.jpg')
pixels = img2.load() # create the pixel map

for i in range(img2.size[0]):    # for every col:
    a=+1
    b=0
    for j in range(img2.size[1]):    # For every row
        b=+1
        if (a%2)==0:
            b=+1
#       print(pixels[i,j,166])
        if (b%2)!=0:
            pixels[i,j] = (250, 250, 250)
        else:
            sf=int(sum(pixels[i,j])/3)
            pixels[i,j] = (sf, sf, sf) # set the colour accordingly
        if (a % 2) == 0:
            b=-1
img2.show()