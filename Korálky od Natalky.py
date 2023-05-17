import tkinter as tk
import random

Width=500
Height=500
colors = ["pink","yellow","green","blue"]
count=40
size=20

def setup():
    global moveable
    for i in range(40):
        x=random.randrange(0,Width-size)
        y=random.randrange(0,Height-size-40)
        moveable.append(canvas.create_oval(x,y,x+size,y+size,fill=colors[i//10]))
        image=tk.PhotoImage("koralik_nit.png")
        canvas.create_image(0,Width-80,image=image,anchor=tk.NW)

def checkit(e):
    global processed,moveable
    zoz=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz)!=0 and zoz[0] in moveable:
        if len(processed)==0:
            processed.append(zoz[0])
            moveable.remove(zoz[0])
            print("Stalo sa.")

def moveit():
    global processed
    if len(processed)!=0:
        print(canvas.coords(processed[0]))
        coor=canvas.coords(processed[0])
        finalpos=(Width-size,Height-size)
        dx=
        dy=
        canvas.move(processed[0],dx,dy)
    print("I will move it (that weird circly thing with some coloring).")
    canvas.after(5,moveit)

root=tk.Tk()
canvas=tk.Canvas(root, width=Width, height=Height, bg="white")
canvas.bind("<Button-1>",checkit)
canvas.pack()

setup()
root.mainloop()