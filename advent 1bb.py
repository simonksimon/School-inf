fr = open("advent 1a txt.txt")
cur=0
a=0
zoz=[]
for row in fr:
    if row.strip().isdigit():
        cur+=int(row)
    else:
        globals()["0" + str(a)] = cur
        zoz.append(globals()["0" + str(a)])
        cur=0
    a+=1
zoz.sort
totalmax=zoz[-1]+zoz[-2]+zoz[-3]
print(totalmax)
