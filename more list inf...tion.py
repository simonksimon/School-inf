import random
#vybrať náhodný prvok
index=random.randrange(0,10)
print(zoz[index])

print(random.choice(zoz))

#Utriedi sám sema:
zoz.sort()
print(zoz)

#vytvorý nový zoznam, ktorý je sorted verzia starého zoznamu
nov_zoz=sorted(zoz)
print(nov_zoz)
