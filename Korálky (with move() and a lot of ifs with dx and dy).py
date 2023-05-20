import tkinter as tk
from tkinter import Canvas
import random

Width=500
Height=500
colors = ["pink","yellow","green","blue"]
count=40
size=20
zise=0-size
yd=False

def setup():
    global moveable,offs
    moveable=[]
    offs = 40
    for i in range(40):
        x=random.randrange(0,Width-size)
        y=random.randrange(0,Height-size-offs)
        moveable.append(canvas.create_oval(x,y,x+size,y+size,fill=colors[i//10]))
    canvas.create_line(offs, Height - offs, Width - offs, Height - offs)

def checkit(e):
    global processed,moveable,zise
    processed=[]
    zise += size
    yd=False
    zoz=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz)!=0 and zoz[0] in moveable:
        if len(processed)==0:
            processed.append(zoz[0])
            moveable.remove(zoz[0])
            moveit()
            print("Stalo sa.")
safety=0
def moveit():
    global processed,safety,yd
    safety+=1
    if safety==100:
        exit
    if len(processed)!=0:
        print(canvas.coords(processed[0]))
        coor=canvas.coords(processed[0])
        finalpos=(Width-size,Height-size)
        if coor[0]!=offs+zise:
            dx=5
        else:
            dx=0
            yd=True
        if yd==True:
            if coor[1]!=Height-offs:
                dy=5
            else:
                return
        else:
            dy = 0
        canvas.move(processed[0],dx,dy)
    print("I will move it (that weird circly thing with some coloring).")
    if coor!=(offs+zise,Height-offs):
        canvas.after(5,moveit)

root=tk.Tk()
canvas: Canvas=tk.Canvas(root, width=Width, height=Height, bg="white")
canvas.bind("<Button-1>",checkit)
canvas.pack()

setup()
root.mainloop()
