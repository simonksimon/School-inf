priklad=str(input("Input priklad: "))
a=""
b=0
c=""
while a != "+":
    c=(f"{c}{a}")
    a = (priklad[b])
    b+=1
d=priklad[b::]
c=int(c)
d=int(d)
e=c+d
print(e)