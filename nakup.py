nakup=[]
nakup=str(input("Napíš číselný zoznam vecí na kúpenie vo formáte 'počet, cena, počet...': "))
c=False
cisla="0123456789"
ciarka=0
integer=""
integer2=""
vys=0
cely=str(nakup)
cely=f"{cely}#"
y="first"
i=0
while cely[i]!="#":
    if y=="":
        i+=1
    if y == "first":
        y=""
        i=0
    if i<len(cely):
        if c==False:
            if cely[i] in cisla:
                c=True
                ciarka=1
        elif cely[i] == ',':
            ciarka += 1
        if ciarka==1 and cely[i]!=" " and cely[i]!="," and cely[i]!="#":
            integer=f"{integer}{cely[i]}"
        if ciarka==2 and cely[i]!=" " and cely[i]!="," and cely[i]!="#":
            integer2=f"{integer2}{cely[i]}"
        if ciarka==3 or i==len(cely)-1:
            inte=float(integer)
            inte2=float(integer2)
            final=inte*inte2
            vys+=final
            c=False
            ciarka=1
            integer=""
            integer2=""
print(vys)