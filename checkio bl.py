a=""
d=""
c=""
b=""
e=""
output=""
input=str(input("Bird spoke: "))
vowels="aeiyou"
a=len(input)
for i in range(a+1):
    d=i
    if c==True:
        d+=1
    if d==True:
        d+=2
    if i<len(input):
        b=input[d]
        if b not in vowels:
            c=True
        if b in vowels:
            e=True
    output=(f"{output}{b}")
print(output)
