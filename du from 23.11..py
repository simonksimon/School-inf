slov={"item1": 45.5,"item2": 35,"item3": 41.3,"item4": 55,"item5": 24}
slov2={"1":[],"2":[],"3":[],"4":[],"5":[]}
for i in range (len(slov)-1):
    a=0
    for y in range(i,len(slov)-i):
        if a<slov("item",y):
            a=slov(y)
    slov2[i].append(a)
