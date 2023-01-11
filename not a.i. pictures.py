from PIL import Image
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (250,250), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        pixels[i,j] = (i, j, 100) # set the colour accordingly
#img.show()

from PIL import Image
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img2 = Image.open('th.jpg')
pixels = img2.load() # create the pixel map

for i in range(img2.size[0]):    # for every col:
    for j in range(img2.size[1]):    # For every row
#      print(pixels[i,j,166])
        sf=int(sum(pixels[i,j])/3)
        pixels[i,j] = (sf, sf, sf) # set the colour accordingly
img2.show()

