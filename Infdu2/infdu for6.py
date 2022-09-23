e=(int(input("Write a number from which we shall beging counting:")))
a=(int(input("Write a number until which we should count:")))
b=e
d=0
if a<e:
    print("The ending cannot be before the beginning, you philosopher.")
else:
    f=a-e
    for i in range (1,f+2):
        if b<a+1:
            c=b%8
            if c==0:
                d=d+1
            b=b+1

    print(d)
input("To exit, press enter.")