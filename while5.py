a=" "
b=""
d=0
while a[0]!="x":
    #b=(""+str(b)+""+str(a)+"")
    b=(f"{b}{a}")
    a=input("Write a name. When it's done, use a name on x, and we'll count all symbols in the names.")
c=len(b)
c-=1
print(c)

input("Type enter to end program.")

#Next is the same thing, but the count counts in the last name with 'x'.
# a=" "
# b=""
# d=0
# while a[0]!="x":
#     a=input("Write a name. When it's done, use a name on x, and we'll count all symbols in the names.")
#     #b=(""+str(b)+""+str(a)+"")
#     b=(f"{b}{a}")
# c=len(b)
# print(c)
#
# input("Type enter to end program.")
