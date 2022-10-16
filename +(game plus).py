priklad=str(input("Input priklad: "))
a = "0"
b=1
i=0
c=0
if "+" in priklad:
    while b==(len(priklad)+1):
        u=i
        globals()["0" + str(u)] = "0"
        while a != "+":
            a = (priklad[b])
            if a!="x":
                e=globals()["0" + str(u)]
                globals()["0" + str(u)]=(f"{e}{a}")
            b+=1
        i += 1
    for y in range(i+1):
        globals()["0" + str(y)]=int(globals()["0" + str(y)])
        c=c+globals()["0" + str(y)]
    print(c)
else:
    print(priklad)