import tkinter as tk
from tkinter import Canvas
import random
root=tk.Tk()
Width=555
Height=55
canvas: Canvas=tk.Canvas(root,width=Width, height=Height, bg="white")
x1=5
y1=5
size=50
x2=30
y2=27.5
randx=random.randrange(5,550,55)
midspe=[]
moveable=[]
moveable2=[]
repeatances=""
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0

def checkit(z):
    global moveable,repeatances,moveable2,repeatances,specor,a,b,c,d,e,f,g,h,i,j
    zoz = canvas.find_overlapping(z.x, z.y, z.x + 1, z.y + 1)
    cor=canvas.coords(zoz[0])
    if specor==cor:
        canvas.create_rectangle(0,0,555,55,fill="white")
        canvas.create_text(280,25,fill="darkblue",font="Times 15",text="Gratulations. Number of useless clicks (more than 1):"+repeatances)
    else:
        if cor == moveable2[0]:
            a+=1
            if a==2:
                repeatances=(repeatances+"a")
        if cor == moveable2[1]:
            b+=1
            if b==2:
                repeatances=(repeatances+"b")
        if cor == moveable2[2]:
            c+=1
            if c==2:
                repeatances=(repeatances+"c")
        if cor == moveable2[3]:
            d+=1
            if d==2:
                repeatances=(repeatances+"d")
        if cor == moveable2[4]:
            e+=1
            if e==2:
                repeatances=(repeatances+"e")
        if cor == moveable2[5]:
            f+=1
            if f==2:
                repeatances=(repeatances+"f")
        if cor == moveable2[6]:
            g+=1
            if g==2:
                repeatances=(repeatances+"g")
        if cor == moveable2[7]:
            h+=1
            if h==2:
                repeatances=(repeatances+"h")
        if cor == moveable2[8]:
            i+=1
            if i==2:
                repeatances=(repeatances+"i")
        if cor == moveable2[9]:
            j+=1
            if j==2:
                repeatances=(repeatances+"j")

midspe.append(canvas.create_oval(randx,y1,randx+size,y1+size,fill='red'))
specor=canvas.coords(midspe[0])
abeceda="abcdefghijklmnopqrstuvwxyz"
for i in range(10):
    moveable.append(canvas.create_oval(x1,y1,x1+size,y1+size,fill='blue'))
    moveable2.append(canvas.coords(moveable[i]))
    x1 += size + 5
    currentl = abeceda[i]
    letters = canvas.create_text(x2, y2, fill="darkblue", font="Times 40", text=currentl)
    x2 += size + 5

canvas.bind("<Button-1>",checkit)
canvas.pack()
root.mainloop()