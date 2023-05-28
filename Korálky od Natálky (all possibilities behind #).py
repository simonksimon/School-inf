import tkinter as tk
from tkinter import Canvas
import random
import math

Width=500
Height=500
colors = ["pink","yellow","green","blue"]
count=40
safety=0
size=20
zise=0-size
ballnumber=0

def setup():
    global moveable,offs
    moveable=[]
    offs = 40
    canvas.create_line(offs, Height - offs, Width - offs, Height - offs)
    for i in range(40):
        x=random.randrange(0,Width-size)
        y=random.randrange(0,Height-size-offs)
        moveable.append(canvas.create_oval(x,y,x+size,y+size,fill=colors[i//10]))

def checkit(e):
    global processed,moveable,zise,ballnumber,firstpos,counter,mvdone
    processed=[]
    zise +=size+5
    zoz=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz)!=0 and zoz[0] in moveable:
        if len(processed)==0:
            processed.append(zoz[0])
            moveable.remove(zoz[0])
            if ballnumber<10:
                firstpos=False
                counter=0
                mvdone=False
                moveit()
            print("Stalo sa.")

def moveit():
    global processed, safety,zise,zoz,ballnumber,mv1,mv2,firstpos,counter,mvdone
    safety+=1
    if safety==100:
        print("safety overloaded")
        exit
    if len(processed)!=0:
        print(canvas.coords(processed[0]))
        coor=canvas.coords(processed[0])
        #finalpos=(Width-size,Height-size)
        if mvdone==False:
            finalpos1 = [Width - offs, Height - offs - 10]
            mv1 = (finalpos1[0] - coor[0]) / 20
            mv2 = (finalpos1[1] - coor[1]) / 20
            mvdone=True
        print("That weird circly thing with some coloring has been moved.")
        if firstpos==False:
            canvas.move(processed[0], mv1, mv2)
            counter += 1
            if counter == 20:
                firstpos=True
            canvas.after(5, moveit)
        else:
            finalpos2=[offs+zise,Height-offs-10]
            dy = 0
            if coor[0]<finalpos2[0]:
                dx=1
            elif coor[0]>finalpos2[0]:
                dx=-1
            else:
                dx=0
            #if coor[1]<finalpos2[1]:
                #dy=2
            #else:
                #dy = 0
            #dx=offs+zise
            #dy=Height-offs
            canvas.move(processed[0],dx,dy)
            #if dx==0 and dy==
            # if -1<dx<1:
            #if coor[0]==finalpos2[0]:
            if abs(coor[0] - finalpos2[0]) <= 1:
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
