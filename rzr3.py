def priemer(text):
    b=0
    c=0
    d=0
    a=len(text)
    for i in range(a+1):
        if i<len(text):
            e=text[i].isdigit()
            if e==True:
                f=int(text[i])
                b+=f
                c+=1
    if c!=0:
        d=b/c
    return(d)

vstup=str(input("Vstup: "))
vysledok=priemer(vstup)
print(vysledok)
