def accum(slovo:str)->str:
    novoslovo=""
    for i in range(len(slovo)):
        novoslovo+=slovo[i].upper()
        for y in range(i):
            novoslovo+=slovo[i].lower()
        novoslovo+="-"
    nslovo=novoslovo[0:-1]
    return(nslovo)

sslovo=input("Tvoje slovo?")
pslovo=accum(sslovo)
print(pslovo)
