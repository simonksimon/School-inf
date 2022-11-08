kind="e"
od=False #once done
while kind !="x":
    if  od==True:
        kind=str(input("Would you like to decode the previous message, encode a new one "
                       "or exit the program? (d/e/x)"))
    if kind=="e":
        vstup = str(input("What would you like to encode?"))
        k1 = ""
        v1 = ""
        e1 = ""
        t1 = ""
    elif kind=="x":
        continue
    elif kind!="d":
        print("Zlý vstup")
        continue

    def encoder(encoding,k,v,e,t):
        od == False
        if kind == "e":
            kvet = "k"
            encode = ""
            a=len(encoding)
            for i in range(a+1):
                if i<len(encoding):
                    encode=f"{encode}{kvet}"
                    if kvet=="k":
                        k=f"{k}{encoding[i]}"
                        kvet="v"
                    elif kvet=="v":
                        v=f"{v}{encoding[i]}"
                        kvet="e"
                    elif kvet=="e":
                        e=f"{e}{encoding[i]}"
                        kvet="t"
                    elif kvet=="t":
                        t=f"{t}{encoding[i]}"
                        kvet="k"
            vystup=encode

        if kind == "d":
            kvet = "k"
            decode = ""
            pozicia=0
            a = len(encoding)
            for i in range(a + 1):
                if i < len(encoding):
                    if encoding[i] == "k":
                        decode = f"{decode}{k[pozicia]}"
                    elif encoding[i] == "v":
                        decode = f"{decode}{v[pozicia]}"
                    elif encoding[i] == "e":
                        decode = f"{decode}{e[pozicia]}"
                    elif encoding[i] == "t":
                        decode = f"{decode}{t[pozicia]}"
                        pozicia += 1
            vystup=decode
        return(vystup,k,v,e,t)

    encoded,k1,v1,e1,t1=encoder(vstup,k1,v1,e1,t1)
    print(encoded)
    vstup = encoded
    od=True
