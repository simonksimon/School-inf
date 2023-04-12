import tkinter as tk
import random

win=tk.Tk()
farby=["cervena","oranzova","modra","zelena","fialova","tyrkysova/turquoise"]
width=300
height=15
hx=100
hy=100
kable=[]
vybuch=0

def nakreslikable():
    global kable
    for i in range(len(farby)):
        farby.append(canvas.create_rectangle(hx,hy+height*i,hx+width,hy+height*(i+1)))
        vybuch=random.\
            choice(kable)

def stlacac(e):
    print("stlacil")

def menic():
    global ftime
    ftime -=1
    canvas.itemconfig(t,text=ftime)
    #if status:
    canvas.after(100,menic)

canvas=tk.Canvas(win,height=500,width=500,bg="white")
canvas.pack()
t=canvas.create_text(10,10,text=ftime)
canvas.bind("<Button-1>",stlacac)
nakreslikable()
win.mainloop()
