import random
monsters=[]
dlzka=5
lst=[]

def create_monster()->list:
    temp=[]
    for i in range(dlzka):
        temp.append(random.randint(0,10))
    return temp

def test(monster:list)->int:
    return monster.count(1)

def process(monster1,monster2):
    temp=[]
    for i in range(dlzka):
        nahoda=random.randrange(1,101)
        if nahoda>7:                        #normal combination
            nahoda1=random.randrange(1,101)
            if nahoda1>50:
                temp.append(monster1[i])
            else:
                temp.append(monster2[i])
        else:                                  #mutácia
            temp.append(random.randrange(0,10))
    return temp

for i in range(10):
    lst.append(create_monster())
print(lst)

def manualne_triedenie(c):
    for i in range(len(c),0,-1):
        for j in range(0,i-1):
            if test(c[j])>test(c[j+1]):
                c[j],c[j+1]=c[j+1],c[j]

for i in range(10):
    lst.append(create_monster())

print(lst)
manualne_triedenie(lst)
lst=lst[len(lst)//2::]
for i in range(len(lst)):
    lst.append(process(lst[random.randrange(0,5)],lst[random.randrange(0,5)]))
print(lst)
input()
