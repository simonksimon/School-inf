a=(int(input("Write a number until which we should count:")))
b=1+1
c=0
for i in range (1,a+1):
    if b<a+1:
        c=c+b
        b=b+2

print(c)

input("To exit, press enter.")