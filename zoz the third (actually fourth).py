import random
zoz=[]
for i in range(10):
    zoz.append(random.randrange(0,100))

def findmaximum(index:int)->int:
    max_value=zoz[index]
    max_value=index
    for i in range(index,len(zoz)):
        if i>max_value:
            max_value=zoz[i]
            max_index=i
    return max_index

print(*zoz)

for i in range(len(zoz)):
    max_index=findmaximum(i)
    zoz[i],zoz[max_index]=zoz[max_index],zoz[i]

print(*zoz)
