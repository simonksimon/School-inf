print("Ak 'a' na druhú plus 'b' na druhú je väčšie ako 'c' na druhú, je to acute.")

n1=(int(input("First side of the triangle:")))
n2=(int(input("Second side of the triangle:")))
n3=(int(input("Third side of the triangle:")))
a=n1*n1
b=n2*n2
c=n3*n3

if n1>n2+n3 or n2>n1+n3 or n3>n1+n2 or n1==0 or n2==0 or n3==0 or n1<0 or n2<0 or n3<0:
    print("Not valid values.")
else:
    print("Congratulations for a successful triangle.")\

    if n1==n2 and n2==n3:
        print("Rovnostranný trojuholník.")
    else:
        if n1==n3 and n2!=n3:
            print("Rovnoramenný trojuholník.")
        else:
            if n3==n2 and n2!=n1:
                print("Rovnoramenný trojuholník.")
            else:
                if n1>n2 and n1>n3:
                    d=b+c
                    if d>a:
                        print("Ostrouhlý trojuholník.")
                    else:
                        if d<a:
                            print("Tupouhlý trojuholník.")
                        else:
                            print("Pravouhlý trojuholník.")
                else:
                    if n2>n1 and n2>n3:
                        e=a+c
                        if e>b:
                            print("Ostrouhlý trojuholník.")
                        else:
                            if e<b:
                                print("Tupouhlý trojuholník.")
                            else:
                                print("Pravouhlý trojuholník.")
                    else:
                        if n3>n2 and n1<n3:
                            f=a+b
                            if f>c:
                                print("Ostrouhlý trojuholník.")
                            else:
                                if f<c:
                                    print("Tupouhlý trojuholník.")
                                else:
                                    print("Pravouhlý trojuholník.")


input("Click enter to end program.")
