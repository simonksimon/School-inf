vstup=str(input("Text, v ktorom počítame cifry: "))
a=len(vstup)
c=0
for i in range(a+1):
    b=False
    if i<len(vstup):
        b=vstup[i].isdigit()
        if b==True:
            c+=1
print(c)