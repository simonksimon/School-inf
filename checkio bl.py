a=""
d=0
c=""
b=""
e=""
output=""
input=str(input("Bird spoke: "))
vowels="aeiyou"
a=len(input)
for i in range(a+1):
    if d<len(input):
        b=input[d]
        if b in vowels:
            e=True
            c=False
        if b==" ":
            c=False
            e=False
            d+=1
        if b not in vowels and b!=" ":
            c=True
            e=False
        if c==True:
            d+=2
        if e==True:
            d+=3
        output=(f"{output}{b}")
print(output)
