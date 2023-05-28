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
moveable=[]
repeatances=""
moveable2=[]
randx=random.randrange(5,550,55)

def checkit(z):
    global moveable,repeatances
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    processed = []
    zoz = canvas.find_overlapping(z.x1, z.y1, z.x1 + 1, z.y1 + 1)
    if len(zoz) != 0 and zoz[0] in moveable:
        if len(processed) == 0:
            if z==1:
                a+=1
                if a==2:
                    repeatances=(repeatances+"a")
            if z==2:
                b+=1
                if b==2:
                    repeatances=(repeatances+"b")
            if z==3:
                c+=1
                if c==2:
                    repeatances=(repeatances+"c")
            if z==4:
                d+=1
                if d==2:
                    repeatances=(repeatances+"d")
            if z==5:
                e+=1
                if e==2:
                    repeatances=(repeatances+"e")
            if z==6:
                f+=1
                if f==2:
                    repeatances=(repeatances+"f")
            if z==7:
                g+=1
                if g==2:
                    repeatances=(repeatances+"g")
            if z==8:
                h+=1
                if h==2:
                    repeatances=(repeatances+"h")
            if z==9:
                i+=1
                if i==2:
                    repeatances=(repeatances+"i")
            if z==10:
                j+=1
                if j==2:
                    repeatances=(repeatances+"j")

def checkit2(z):
    global moveable2, repeatances
    processed2 = []
    zoz2 = canvas.find_overlapping(randx,y1,randx+size,y1+size)
    if len(zoz2)!=0 and zoz2[0] in moveable2:
        if len(processed2)==0:
            canvas.create_rectangle(0,0,555,55,fill="white")
            canvas.create_text(280,25,fill="darkblue",font="Times 19",text="Gratulations. Number of useless clicks (more than 1):"+repeatances)

moveable2.append(canvas.create_oval(randx,y1,randx+size,y1+size,fill='red'))
abeceda="abcdefghijklmnopqrstuvwxyz"
for i in range(10):
    moveable.append(canvas.create_oval(x1,y1,x1+size,y1+size,fill='blue'))
    x1 += size + 5
    currentl = abeceda[i]
    letters = canvas.create_text(x2, y2, fill="darkblue", font="Times 40", text=currentl)
    x2 += size + 5

canvas.bind("<Button-1>",checkit2,checkit)
canvas.pack()
root.mainloop()
