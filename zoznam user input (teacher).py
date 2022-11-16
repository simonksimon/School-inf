zoz=[]
for i in range(10):
    zoz.append(input("Zadaj mi prvok zoznamu: "))

print(zoz)
print(*zoz)

for i in range(10):
  print(zoz[i])

for prvok in zoz: #prvok je takého typu, aký je uložený v zozname
  print(prvok,type(prvok))

for index,hodnota in enumerate(zoz): #v angličtine index a value
  print(index)
  print(hodnota)
