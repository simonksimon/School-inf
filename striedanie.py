from PIL import Image
c=False
img=Image.new( 'RGB', (100,100), "black")
pixels = img.load()

for i in range(img.size[0]):
    c = not c
    for j in range(img.size[1]):
        c = not c
        if c:
            pixels[i,j] = (0, 0, 0)
        else:
            pixels[i,j] = (250, 250, 250)

img.show()
