fr = open("advent 1a txt.txt")
cur=0
totalmax1=0
totalmax2=0
totalmax3=0
b=0
for row in fr:
    if row.strip().isdigit():
        cur+=int(row)
    else:
        b+=1
        if cur>totalmax1:
            totalmax1=cur
            elf1=('elf1 ',b)
        elif cur>totalmax2:
            totalmax2=cur
            elf2=('elf2 ',b)
        elif cur>totalmax3:
            totalmax3=cur
            elf3=('elf3 ',b)
        cur=0
totalmax=totalmax1+totalmax2+totalmax3
print(elf1)
print(elf2)
print(elf3)
print(totalmax)

