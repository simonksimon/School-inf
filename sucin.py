def suc(zoz):
    string=str(zoz)
    string=(string," ")
    cisla="0123456789"
    vys=1
    cis=""
    if string != "":
        for i in range(len(string)):
            if i<len(string):
                cislo=""
                y=0
                n=""
                m=str(string[i])
                while m in cisla:
                    cislo=f"{cislo}{string[i]}"
                    i+=1
                    m = str(string[i])
                    if y == 100 or i >= len(string):
                        break
                    if string[i]=="," or string[i]==" ":
                        n=cislo
                    y += 1
                if i >= len(string):
                    break
                if n!="":
                    cis=int(n)
                if n!="":
                        vys*=cis
    else:
        vys=1
    return vys

y=0
inp=" "
while inp!="":
    y+=1
    sucin=[]
    inp=input("Napíš radu znakov. My ti vypíšeme, aký typ je každý. "
              "Ak si želáš skončiť, stlač iba enter. ")
    print(suc(inp))
    if y==100:
        break