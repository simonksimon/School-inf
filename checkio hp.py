vstup=str(input("New password?" ))
a=""
k=""
c=""
d=""
c2=""
d2=""
f=""
g=""
Safe=""
if len(vstup)>8:
    for i in range(9):
        h=str(i)
        if h in vstup:
            a=True
    if a==True:
        b=len(vstup)
        for i in range(b+1):
            if i<len(vstup):
                k=vstup[i].isdigit()
                if k==False:
                    c=vstup[i].isupper()
                    d=vstup[i].islower()
                    if c==True:
                        c2=True
                    if d==True:
                        d2=True
        if c2==True and d2==True:
            e=len(vstup)
            for i in range(e+1):
                if i<len(vstup):
                    f=ord(vstup[i])
                if f>127:
                    g=False
            if g!=False:
                Safe=True
if Safe==True:
    print("Safe enough")
else:
    print("Don't you even care about your safety? That's weak.")
