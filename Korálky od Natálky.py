import tkinter as tk
from tkinter import Canvas
import random

Width=500
Height=500
colors = ["pink","yellow","green","blue"]
count=40
safety=0
size=20
zise=0-size
ballnumber=0
#bx=5

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
    global processed,moveable,zise,ballnumber
    processed=[]
    zise += size
    zoz=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz)!=0 and zoz[0] in moveable:
        if len(processed)==0:
            processed.append(zoz[0])
            moveable.remove(zoz[0])
            if ballnumber<10:
                moveit()
            print("Stalo sa.")

def moveit():
    global processed, safety,zise,zoz,ballnumber#,bx
    safety+=1
    if safety==100:
        print("safety overloaded")
        exit
    if len(processed)!=0:
        print(canvas.coords(processed[0]))
        coor=canvas.coords(processed[0])
        #finalpos=(Width-size,Height-size)
        finalpos=[offs+zise,Height-offs-10]
        if coor[0]<finalpos[0]:
            dx=1
        elif coor[0]>finalpos[0]:
            dx=-1
        else:
            dx=0
        if coor[1]<finalpos[1]:
            dy=1
        else:
            dy=0
        #dx=offs+zise
        #dy=Height-offs
        canvas.move(processed[0],dx,dy)
        print("I will move it (that weird circly thing with some coloring).")
        if dx==0 and dy==0:
            #canvas.move(processed[0], bx, 0)
            #bx+=5
            print("Ball done.")
            ballnumber+=1
            exit
        else:
            canvas.after(5, moveit)

root=tk.Tk()
canvas: Canvas=tk.Canvas(root, width=Width, height=Height, bg="white")
canvas.bind("<Button-1>",checkit)
canvas.pack()

setup()
root.mainloop()
