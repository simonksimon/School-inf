kind="e"
od=False #once done
while kind !="x":
    if od==True:
        kind=str(input("Would you like to decode the previous message, encode a new one "
                       "or exit the program? (d/e/x)"))
    if kind=="e":
        vstup = str(input("What would you like to encode?"))
        key = str(input("Into what word would you like to encode it?"))
        k1 = ""
        v1 = ""
        e1 = ""
        t1 = ""
    elif kind=="x":
        continue
    elif kind!="d":
        print("Zlý vstup")
        continue

    def encoder(encoding):
        if kind == "e":
            kd=False #key done
            kvet = key[0]
            encode = ""
            d=0
            glob=""
            zoz=
            a=len(encoding)
            for i in range(a+1):
                if i<len(encoding):
                    i=d
                    b=len(key)
                    for y in range (b+1):
                        if y<len(key):
                            if d<len(encoding):
                                c=key[y]
                                if kd == False:
                                    globals()["0" + str(c)] = ""
                                encode=f"{encode}{kvet}"
                                glob=f"{glob}{encoding[d]}"
                                globals()["0" + str(c)]=glob
                                if y==len(key)-1:
                                    kvet=key[0]
                                else:
                                    kvet=key[y+1]
                                d+=1
            b=len(key)
                    for y in range (b+1):
                        if y<len(key):
                            zoz=globals()["0" + str(y)]
        vystup=encode

        if kind == "d":
        #     kvet = "k"
        #     decode = ""
        #     pozicia=0
        #     a = len(encoding)
        #     for i in range(a + 1):
        #         if i < len(encoding):
        #             if encoding[i] == "k":
        #                 decode = f"{decode}{k[pozicia]}"
        #             elif encoding[i] == "v":
        #                 decode = f"{decode}{v[pozicia]}"
        #             elif encoding[i] == "e":
        #                 decode = f"{decode}{e[pozicia]}"
        #             elif encoding[i] == "t":
        #                 decode = f"{decode}{t[pozicia]}"
        #                 pozicia += 1
        #     vystup=decode
        return(vystup,zoz)

    encoded=encoder(vstup)
    print(encoded)
    vstup = encoded
    od=True
