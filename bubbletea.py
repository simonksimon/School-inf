zoz=[]
zoz.append(" ")
y=0
while zoz[y]!="":
    zoz.append(input("Give a number, or just press 'enter' to continue into the next part of this program:"))
    y+=1
    if y==100:
        break
del zoz[0]
del zoz[y-1]
print(zoz)
c=0
d=0
while c!=len(zoz)-1:
    d+=1
    if d == 100:
        break
    c=0
    for i in range(len(zoz)-1):
        if int(zoz[i+1])>int(zoz[i]):
            zoz[i],zoz[i+1]=zoz[i+1],zoz[i]
        else:
            c+=1
final=""
for i in range(len(zoz)):
    final=(str(final)+str(zoz[i]))
    final=int(final)
print(final)
