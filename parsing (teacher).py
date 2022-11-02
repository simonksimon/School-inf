tr="jano<jashdfjhd>sdfjksdjf<fero><miso>dsjhdjfh<fdfd>h"

def parsovacka(zdroj:str)->str:
    status=True
    nr=" "
    for i in zdroj:
        if i=="<":
            status=False
        if status:
            nr+=i
        if i==">":
            status=True
        return nr

print(parsovacka(tr))
