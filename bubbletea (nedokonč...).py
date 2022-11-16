zoz=[]
for i in range(10):
    zoz.append(input("Zadaj mi prvok zoznamu: ")) #22 10 15 1 8
z=[]
for i in range(len(zoz)):
    z.append(zoz[i])
for i in range(len(zoz)):
    for y in range(len(z)-1):
        if zoz[y+1]>zoz[i]:
            z.append(zoz[i+1])
            z.append(zoz[i])
            for o in range(2,len(zoz)-2):
                z.append(zoz[o])
