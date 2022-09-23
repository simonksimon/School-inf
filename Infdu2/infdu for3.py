a=(int(input("Write a number until which we should count:")))
b=1
e=0
for i in range (1,a+1):
    if b<a+1:
        c=b%4
        d=b%7
        if c==0 and d==0:
            e=e+1
        b=b+1

print(e)
input("To exit, press enter.")