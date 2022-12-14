fr = open("advent 1a txt.txt")
cur=0
totalmax=0
b=0
for row in fr:
    if row.strip().isdigit():
        cur+=int(row)
    else:
        b+=1
        if cur>totalmax:
            totalmax=cur
            elf=('elf ',b)
        cur=0
print(totalmax)
print(elf)
