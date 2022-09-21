a=(int(input("Zadaj párne alebo nepárne číslo.")))
b=a-a-a
if a==0:
    print("Nula je veľmi nešťastné číslo. Skús nejaké iné.")
else:
    c=1/a
    print("Záporne brátené číslo je:")
    print(b)
    print("Desatinne obrátené číslo je:")
    print(c)

input("To exit, press enter.")