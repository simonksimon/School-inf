from PIL import Image
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
c=False
img2 = Image.open('th.jpg')
pixels = img2.load() # create the pixel map

for i in range(img2.size[0]): # for every col:
    c = not c
    for j in range(img2.size[1]):    # For every row
        c = not c
#       print(pixels[i,j,166])
        if c:
            pixels[i,j] = (0, 0, 0)
            #        else:
        #           sf=int(sum(pixels[i,j])/3)
            #           pixels[i,j] = (sf, sf, sf) # set the colour accordingly
img2.show()