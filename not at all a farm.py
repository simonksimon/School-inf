import random

a="1"

for i in range(10):
    globals()["0" + str(a)] = []
    for y in range(5):
        n=str(random.randrange(1,10))
        globals()["0" + str(a)].append(n)
    print(globals()["0" + str(a)])
    b=int(a)
    b+=1
    a=str(b)

dict={}
for i in range(9):
    dict[i+1]=globals()["0" + str(i+1)]

d=0
for y in range(4):
    c = 100
    f = 1
    e=0
    d=100
    while c==100:
        test = dict.get(f)
        if test:
            c = dict[f][0] + dict[f][1] + dict[f][2] + dict[f][3] + dict[f][4]
            d=f
        else:
            f += 1
        e+=0
        if e==100:
            break
    for i in range(8):
        test2=dict.get(i+2)
        if test2:
            long=dict[i+2][0]+dict[i+2][1]+dict[i+2][2]+dict[i+2][3]+dict[i+2][4]
            if long>c:
                c=long
                d=i+2
        else:
            continue
    test3 = dict.get(d)
    if test3:
        del dict[d]
    else:
        continue

print(" ")
print("Left: ")
for i in range(9):
    test4 = dict.get(i+1)
    if test4:
        print(dict[i+1])
    else:
        continue

for i in range(5):
    ne1=0
    while ne1!=100:
        n1=int(random.randrange(1,10))
        test5 = dict.get(n1)
        ne1 += 1
        if test5:
            break
        else:
            continue

    n2=10
    ne2 = 0
    while ne2!=100:
        n2 = int(random.randrange(1, 10))
        if n2==n1:
            continue
        test6 = dict.get(n2)
        ne2 += 1
        if test6:
            break
        else:
            continue

    dict[11+i]=[]
    for y in range(5):
        n3 = str(random.randrange(1, 12))
        if n3==12:
            dict[11+i].append(str(random.randrange(0, 9)))
        else:
            if dict[n1][y]>dict[n2][y]:
                dict[11+i].append(int(dict[n1][y])-int(dict[n2][y]))
            else:
                dict[11+i].append(int(dict[n2][y])-int(dict[n1][y]))

print(" ")
print("New:")
for i in range(5):
    print(dict[11+i])