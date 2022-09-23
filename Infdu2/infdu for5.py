a=(int(input("Write a number until which we should count:")))
b=1
d=0
for i in range (1,a+1):
    if b<a+1:
        c=b%2
        if c==0:
            d=d+1
        b=b+1

print(d)
input("To exit, press enter.")