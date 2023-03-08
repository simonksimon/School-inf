from PIL import Image
fr=open("kompresia_obrazka_3.txt",'r')
fl=fr.readline().split()
print(fl)
obr=Image.new("RGB",(int(fl[0]),int(fl[1])),"white")
pixels=obr.load()


#def mapping(a, b, c, d, x):
#    return int((d*(x-a)+c*(b-x))/(b-a))
