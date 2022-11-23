from string import ascii_lowercase
print(ascii_lowercase)

fz={"a":6,"b":302,"auto":4018}
print(fz["a"])
print(fz["b"])
print(fz["auto"])

for keys in fz:
    print(fz[keys])

#Zisti, ko¾ko sa v inpute nachádzajú ktoré písmená abecedy (anglickej a lowercase)
vstup=input("Zadaj mi reazec: ")
poc={}

for i in vstup:
    if i in ascii_lowercase:
        poc[i]=poc.get(i,0)+1
        #if i in poc.keys():
        #   poc[i]+=1
        #else:
        #   poc[i]=1
print[poc]

slov={"item1": 45.5,"item2": 35,"item3": 41.3,"item4": 55,"item5": 24} #du zotriedi a vypísa prvé 3 (bez sorted)

#nájs maximálny prvok v dictionary
#for j in range(3):
#    index_max=list(slov.keys())[0]
#    print(dir(index_max))
#    moj_max=slov[index_max]
#    for prvok in slov:
#        if slov[prvok]>moj_max:
#            moj_max=slov[prvok]
#            index_max=prvok
#    print(moj_max, index_max)
#    temp=slov.pop(index_max)

