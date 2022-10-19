def uloha1(ret:str)->str:
    polka=len(ret)//2
    if polka%2==1:
        polka+=1
    1# cez rezy
    #pp=ret[0:polka].upper()
    #hp=ret[polka::]
    2# bez rezov
    pp=""
    hp=""
    for i in range(0,polka):
        pp+=ret[i].upper()
    for i in range(0,len(ret)):
        hp+=ret[i]
    return pp+hp

print(uloha1("{meno s párnym počtom písmen}"))
print(uloha1("{meno nes párnym počtom písmen}"))
