a=(int(input("Write a number until which we should count:")))
b=0
c=0
for i in range (1,a+1):
    if b<a+1:
        b=b+1
        c=c+b

print(c)
input("To exit, press enter.")